"""Stage orchestration for the Version 1 flow.

``PRE_STAGE`` → ``00_INTAKE`` → ``01_TRIAGE`` → ``02_PLAYBOOK_MATCH`` →
``03_PLAN`` → ``04_DEV_FIX`` → ``05_DEV_REVIEW``, then stop.

Every stage writes ``INPUT.json`` (what it consumed), ``OUTPUT_DEVIN_AI.json``
(schema-validated machine output) and ``OUTPUT_PEOPLE_ENGINEER.md`` (the human
document). A stage never runs on data that failed validation.

Each stage is one function that does one thing, so a wrong artifact is traced to
one place. :class:`Session` carries the per-run collaborators (paths, audit log,
attempt store, identity registry) so the stage functions stay small.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from . import (
    autonomy,
    codebase,
    dedupe,
    describe,
    devfix,
    discovery,
    effort,
    extract,
    guardrails,
    history,
    ids,
    normalize,
    planner,
    playbooks,
    render,
    review,
    schema,
    scoring,
    supervisor,
)
from . import (
    metrics as metrics_module,
)
from .attempts import AttemptStore
from .audit import AuditLog
from .config import Config
from .naming import Audience, Stage, artifact_name, run_id
from .states import State, transition

QUOTED = re.compile(r"[\"\u201c]([^\"\u201c\u201d]{4,120})[\"\u201d]")


class PipelineError(RuntimeError):
    """Raised when a stage cannot produce a valid artifact."""


@dataclass
class RunPaths:
    root: Path

    def stage_dir(self, stage: Stage) -> Path:
        path = self.root / stage.value
        path.mkdir(parents=True, exist_ok=True)
        return path


@dataclass
class Result:
    run_context: discovery.RunContext
    manifest: dict[str, Any]
    issues: list[dict[str, Any]]
    metrics: dict[str, Any]
    paths: RunPaths
    written: list[Path]


@dataclass
class Session:
    """Per-run collaborators shared by the stage functions."""

    config: Config
    context: discovery.RunContext
    paths: RunPaths
    audit: AuditLog
    attempts: AttemptStore
    issue_ids: ids.IssueRegistry
    artifact_root: Path
    written: list[Path] = field(default_factory=list)

    @property
    def date(self) -> str:
        return self.context.report_date

    @property
    def run(self) -> str:
        return self.context.run_id


def next_run_id(root: Path) -> str:
    """Allocate the next run id by inspecting existing run directories."""
    existing = [
        int(path.name.removeprefix("RUN_"))
        for path in root.glob("*/RUN_*")
        if path.is_dir() and path.name.removeprefix("RUN_").isdigit()
    ]
    return run_id(max(existing, default=0) + 1)


def _write_input(paths: RunPaths, stage: Stage, date: str, run: str, payload: Any) -> Path:
    path = paths.stage_dir(stage) / artifact_name(date, run, stage, "INPUT")
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _write_machine(paths: RunPaths, stage: Stage, date: str, run: str, doc: dict[str, Any]) -> Path:
    name = artifact_name(date, run, stage, "OUTPUT", Audience.DEVIN_AI)
    return schema.write_json(doc, paths.stage_dir(stage) / name, schema.STAGE_OUTPUT)


def _write_human(paths: RunPaths, stage: Stage, date: str, run: str, body: str) -> Path:
    name = artifact_name(date, run, stage, "OUTPUT", Audience.PEOPLE_ENGINEER, extension="md")
    path = paths.stage_dir(stage) / name
    path.write_text(body, encoding="utf-8")
    return path


def _write_stage(
    paths: RunPaths,
    stage: Stage,
    report_date: str,
    run: str,
    stage_input: Any,
    machine: dict[str, Any],
    human: str,
) -> list[Path]:
    return [
        _write_input(paths, stage, report_date, run, stage_input),
        _write_machine(paths, stage, report_date, run, machine),
        _write_human(paths, stage, report_date, run, human),
    ]


def _input_reference(
    paths: RunPaths, stage: Stage, report_date: str, run: str, previous: Stage
) -> dict[str, Any]:
    """A stage's input is the previous stage's machine output, referenced by digest.

    Copying it would duplicate every issue once per stage and make the daily artifact
    directory unreadable in a diff.
    """
    path = paths.stage_dir(previous) / artifact_name(
        report_date, run, previous, "OUTPUT", Audience.DEVIN_AI
    )
    return {
        "run_id": run,
        "report_date": report_date,
        "stage": stage.value,
        "source_stage": previous.value,
        "source_artifact": str(path.relative_to(paths.root)),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def _document(
    run: discovery.RunContext,
    stage: Stage,
    issues: list[dict[str, Any]],
    config: Config,
    next_state: str,
    next_input: str | None,
    status: str | None = None,
) -> dict[str, Any]:
    return {
        "run_id": run.run_id,
        "report_date": run.report_date,
        "stage": stage.value,
        "status": status
        or ("OK" if run.completeness is discovery.Completeness.COMPLETE else "PARTIAL_SOURCE_DATA"),
        "dry_run": config.dry_run_mode,
        "run_flags": run.run_flags,
        "warnings": run.warnings,
        "issues": issues,
        "next_state": next_state,
        "next_expected_input_file": next_input,
    }


def _stage_issue_view(issue: dict[str, Any], stage: Stage, next_state: str) -> dict[str, Any]:
    """The per-issue record embedded in a stage's machine output."""
    view = dict(issue)
    view["stage"] = stage.value
    view["status"] = "BLOCKED" if issue.get("guardrail_violations") else "OK"
    view["next_state"] = next_state
    return view


def _next_input_name(session: Session, stage: Stage | None) -> str | None:
    if stage is None:
        return None
    return artifact_name(session.date, session.run, stage, "INPUT")


def _advance(issue: dict[str, Any], source: State, target: State, reason: str) -> None:
    """Move one issue through a permitted transition."""
    issue["state"] = transition(source, target, reason).to_state.value


def _open_session(config: Config, repository_root: Path, report_date: str | None) -> Session:
    """Discover sources, allocate the run, and open the run's stores."""
    artifact_root = config.artifact_root_directory
    artifact_root.mkdir(parents=True, exist_ok=True)
    directory = repository_root / config.mgmt_reports_directory
    context = discovery.assemble(
        config, directory, next_run_id(artifact_root), requested_report_date=report_date
    )
    paths = RunPaths(artifact_root / context.report_date / context.run_id)
    paths.root.mkdir(parents=True, exist_ok=True)
    return Session(
        config=config,
        context=context,
        paths=paths,
        audit=AuditLog(paths.root / "audit.jsonl", context.run_id),
        # Identity and history live above the per-run directory: an issue id and its
        # attempts must keep their meaning across runs and report dates.
        attempts=AttemptStore(artifact_root / "attempts.jsonl"),
        issue_ids=ids.IssueRegistry.load(artifact_root / "issue_registry.json"),
        artifact_root=artifact_root,
    )


def _publish(
    session: Session,
    stage: Stage,
    *,
    stage_input: Any,
    issues: list[dict[str, Any]],
    next_state: State,
    next_stage: Stage | None,
    human: Any,
) -> dict[str, Any]:
    """Write a stage's three artifacts and return its machine document."""
    views = [_stage_issue_view(issue, stage, next_state.value) for issue in issues]
    doc = _document(
        session.context,
        stage,
        views,
        session.config,
        next_state.value,
        _next_input_name(session, next_stage),
    )
    session.written += _write_stage(
        session.paths, stage, session.date, session.run, stage_input, doc, human(doc)
    )
    return doc


def _write_manifest(session: Session, manifest: dict[str, Any]) -> None:
    name = artifact_name(session.date, session.run, Stage.PRE_STAGE, "MANIFEST")
    path = session.paths.stage_dir(Stage.PRE_STAGE) / name
    session.written.append(schema.write_json(manifest, path, schema.PRE_STAGE_MANIFEST))


def _require_processable(context: discovery.RunContext) -> None:
    if context.processable:
        return
    raise PipelineError(
        f"source discovery is {context.completeness.value} for {context.report_date}: "
        + "; ".join(context.warnings)
    )


def pre_stage(session: Session) -> dict[str, Any]:
    """Record what sources were found, and refuse to continue on unusable data."""
    manifest = session.context.manifest(session.config)
    _write_manifest(session, manifest)
    session.audit.record(
        "SOURCE_DISCOVERY",
        stage=Stage.PRE_STAGE.value,
        detail={
            "completeness": session.context.completeness.value,
            "sources": [s.path.name for s in session.context.sources],
            "warnings": session.context.warnings,
        },
    )
    _require_processable(session.context)
    return manifest


def _extract_findings(session: Session) -> list[extract.RawFinding]:
    return [finding for source in session.context.sources for finding in extract.extract(source)]


def _normalize_findings(
    session: Session, findings: list[extract.RawFinding]
) -> list[dict[str, Any]]:
    issues = normalize.normalize(
        dedupe.cluster(findings),
        session.context,
        session.config.mgmt_reports_repository,
        redact_ratings=session.config.redact_employee_ratings,
        allocate_id=session.issue_ids.resolve,
        attempt_number=session.attempts.current_number,
        repo_scope=session.config.repository_scope,
    )
    session.issue_ids.save()
    return issues


def _review_targets(issue: dict[str, Any]) -> tuple[str, ...]:
    """The repository the finding names, or every repository it could mean."""
    repository = issue.get("repository")
    if repository:
        return (str(repository),)
    return tuple(str(name) for name in (issue.get("candidate_repositories") or []))


def _quoted_subjects(issue: dict[str, Any]) -> tuple[str, ...]:
    """Commit subjects the finding itself quoted, so history can be narrowed."""
    stated = str(issue.get("description") or "")
    return tuple(match.strip() for match in QUOTED.findall(stated) if len(match.strip()) > 8)


def _review_one(session: Session, issue: dict[str, Any], target: str | None) -> dict[str, object]:
    """Read one target repository: its current state, and the day's work in it."""
    root = session.config.repository_root
    paths = tuple(str(path) for path in (issue.get("files") or []))
    state = codebase.inspect(root, target, paths)
    local = codebase.checkout(root, target)
    done = history.work_done(local, session.date, issue.get("owner"), _quoted_subjects(issue))
    return {**state.as_dict(), "work_done": done.as_dict()}


def _attach_code_review(session: Session, issues: list[dict[str, Any]]) -> None:
    """Record what a read-only look at each target repository found."""
    for issue in issues:
        targets = _review_targets(issue) or (None,)
        issue["code_review"] = [_review_one(session, issue, target) for target in targets]


def _validate_issues(issues: list[dict[str, Any]]) -> None:
    for issue in issues:
        schema.validate(issue, schema.ISSUE)


def intake(session: Session, manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract, deduplicate, normalize, and validate the report findings."""
    findings = _extract_findings(session)
    issues = _normalize_findings(session, findings)
    _attach_code_review(session, issues)
    _validate_issues(issues)
    session.audit.record(
        "INTAKE",
        stage=Stage.INTAKE.value,
        detail={"findings": len(findings), "issues": len(issues)},
    )
    for issue in issues:
        _advance(issue, State.DISCOVERED, State.TRIAGED, "normalized from report evidence")
    _publish(
        session,
        Stage.INTAKE,
        stage_input=manifest,
        issues=issues,
        next_state=State.TRIAGED,
        next_stage=Stage.TRIAGE,
        human=lambda doc: render.intake(doc, manifest),
    )
    return issues


def _score_issues(issues: list[dict[str, Any]], limit: int) -> list[str]:
    for issue in issues:
        issue.update(scoring.score(issue))
    return planner.select_candidates(issues, limit)


def triage(session: Session, issues: list[dict[str, Any]], limit: int) -> list[str]:
    """Score priority and complexity, then order the in-scope issues."""
    selected = _score_issues(issues, limit)
    for issue in issues:
        issue["selected_for_attention"] = issue["issue_id"] in selected
        _advance(issue, State.TRIAGED, State.PLAYBOOK_MATCHED, "scored and ordered")
    _publish(
        session,
        Stage.TRIAGE,
        stage_input=_input_reference(
            session.paths, Stage.TRIAGE, session.date, session.run, Stage.INTAKE
        ),
        issues=issues,
        next_state=State.PLAYBOOK_MATCHED,
        next_stage=Stage.PLAYBOOK_MATCH,
        human=render.triage,
    )
    session.audit.record("TRIAGE", stage=Stage.TRIAGE.value, detail={"selected": selected})
    return selected


def _apply_match(issue: dict[str, Any], match: playbooks.Match) -> None:
    issue["playbook_match"] = match.as_dict()
    issue["skills_required"] = match.skills_required
    issue["skills_available"] = match.skills_available
    issue["missing_skills"] = match.missing_skills
    _advance(issue, State.PLAYBOOK_MATCHED, State.PLANNED, "playbook resolved")


def _matched_playbooks(issues: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        issue["issue_id"]: (issue.get("playbook_match") or {}).get("playbook_id")
        for issue in issues
    }


def playbook_match(
    session: Session, issues: list[dict[str, Any]]
) -> tuple[playbooks.Registry, dict[str, playbooks.Match]]:
    """Match every issue against the approved playbooks."""
    registry = playbooks.load_registry(session.config)
    matches: dict[str, playbooks.Match] = {}
    for issue in issues:
        matches[issue["issue_id"]] = playbooks.match(issue, registry, session.config)
        _apply_match(issue, matches[issue["issue_id"]])
    _publish(
        session,
        Stage.PLAYBOOK_MATCH,
        stage_input=_input_reference(
            session.paths, Stage.PLAYBOOK_MATCH, session.date, session.run, Stage.TRIAGE
        ),
        issues=issues,
        next_state=State.PLANNED,
        next_stage=Stage.PLAN,
        human=render.playbook_match,
    )
    session.audit.record(
        "PLAYBOOK_MATCH",
        stage=Stage.PLAYBOOK_MATCH.value,
        detail=_matched_playbooks(issues),
    )
    return registry, matches


def _record_block(session: Session, issue: dict[str, Any]) -> None:
    issue["state"] = State.BLOCKED.value
    session.audit.record(
        "GUARDRAIL_BLOCK",
        issue_id=issue["issue_id"],
        attempt_id=issue["attempt_id"],
        stage=Stage.PLAN.value,
        detail={"violations": issue["guardrail_violations"]},
    )


def _copy_plan_fields(issue: dict[str, Any]) -> None:
    """Promote the fields a reviewer reads out of the nested plan."""
    issue["rollback_plan"] = issue["plan"]["rollback_plan"]
    issue["proposed_action"] = issue["plan"]["proposed_action"]
    issue["implementation_plan"] = issue["plan"]["implementation_plan"]


def _apply_plan(
    session: Session,
    issue: dict[str, Any],
    match: playbooks.Match,
    decision: autonomy.Decision,
    violations: list[guardrails.Violation],
) -> None:
    """Record the decision, the guardrail outcome, the plan, and the effort estimate."""
    issue.update(decision.as_dict())
    issue["guardrail_violations"] = [violation.as_dict() for violation in violations]
    issue["plan"] = planner.plan(issue, match, decision, violations, session.config)
    issue.update(effort.for_issue(issue).as_dict())
    issue["task_description"] = describe.describe(issue)
    _copy_plan_fields(issue)


def _plan_issue(
    session: Session,
    issue: dict[str, Any],
    match: playbooks.Match,
    registry: playbooks.Registry,
) -> None:
    decision = autonomy.classify(issue, match, registry, session.config)
    violations = guardrails.evaluate(issue, match, decision, session.config)
    _apply_plan(session, issue, match, decision, violations)
    if violations:
        _record_block(session, issue)
        return
    _advance(issue, State.PLANNED, State.DEV_FIXING, "plan produced")


def _plan_views(issues: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        _stage_issue_view(
            issue,
            Stage.PLAN,
            State.BLOCKED.value if issue["guardrail_violations"] else State.DEV_FIXING.value,
        )
        for issue in issues
    ]


def _publish_plan(session: Session, issues: list[dict[str, Any]]) -> None:
    doc = _document(
        session.context,
        Stage.PLAN,
        _plan_views(issues),
        session.config,
        State.DEV_FIXING.value,
        _next_input_name(session, Stage.DEV_FIX),
    )
    stage_input = _input_reference(
        session.paths, Stage.PLAN, session.date, session.run, Stage.PLAYBOOK_MATCH
    )
    session.written += _write_stage(
        session.paths, Stage.PLAN, session.date, session.run, stage_input, doc, render.plan(doc)
    )


def plan(
    session: Session,
    issues: list[dict[str, Any]],
    registry: playbooks.Registry,
    matches: dict[str, playbooks.Match],
) -> None:
    """Decide autonomy, enforce guardrails, and produce the reviewable plan."""
    for issue in issues:
        _plan_issue(session, issue, matches[issue["issue_id"]], registry)
    _publish_plan(session, issues)


FIX_FIELDS = (
    "changed_files",
    "commands_executed",
    "test_cases_generated",
    "test_results",
    "pre_fix_failure",
    "post_fix_success",
    "full_suite_result",
    "commit_sha",
    "pr_number",
)


def _copy_fix_fields(issue: dict[str, Any]) -> None:
    for name in FIX_FIELDS:
        issue[name] = issue["fix"][name]


def _fix_issue(session: Session, issue: dict[str, Any]) -> None:
    issue["fix"] = devfix.execute(issue, issue["plan"], session.config)
    _copy_fix_fields(issue)
    _advance(issue, State.DEV_FIXING, State.DEV_REVIEW, "dry-run attempt recorded")
    session.audit.record(
        "DEV_FIX_DRY_RUN",
        issue_id=issue["issue_id"],
        attempt_id=issue["attempt_id"],
        stage=Stage.DEV_FIX.value,
        detail={"suppression_reasons": issue["fix"]["suppression_reasons"]},
    )


def dev_fix(session: Session, issues: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Record what would be changed. In a dry run nothing is written anywhere."""
    actionable = [issue for issue in issues if not issue["guardrail_violations"]]
    for issue in actionable:
        _fix_issue(session, issue)
    _publish(
        session,
        Stage.DEV_FIX,
        stage_input=_input_reference(
            session.paths, Stage.DEV_FIX, session.date, session.run, Stage.PLAN
        ),
        issues=actionable,
        next_state=State.DEV_REVIEW,
        next_stage=Stage.DEV_REVIEW,
        human=render.dev_fix,
    )
    return actionable


def _find_decision(
    recorded: dict[str, review.Decision], issue: dict[str, Any], attempt: str
) -> review.Decision | None:
    """An unscoped block only ever addresses the first attempt.

    A decision written without an attempt id in its heading cannot travel to a later
    attempt, otherwise a stale rejection would be reapplied forever.
    """
    decision = recorded.get(attempt)
    if decision is None and attempt.endswith("_ATTEMPT_01"):
        return recorded.get(issue["issue_id"])
    return decision


REVIEW_OUTCOME_FIELDS = (
    "human_review_result",
    "reviewer",
    "reviewer_comments",
    "questions",
    "answers",
    "attempt_id",
    "state",
)


def _apply_outcome(issue: dict[str, Any], outcome: dict[str, Any]) -> None:
    issue.update({name: outcome[name] for name in REVIEW_OUTCOME_FIELDS})
    issue["review_notes"] = outcome["notes"]


def _attempt_base(issue: dict[str, Any], config: Config) -> dict[str, Any]:
    return {
        "issue_id": issue["issue_id"],
        "run_id": issue["run_id"],
        "autonomy_tier": issue.get("autonomy_tier"),
        "playbook_id": (issue.get("playbook_match") or {}).get("playbook_id"),
        "dry_run": config.dry_run_mode,
    }


def _record_decision(session: Session, issue: dict[str, Any], attempt: str) -> None:
    session.attempts.record_decision(
        attempt_id=attempt,
        issue_id=issue["issue_id"],
        run_id=issue["run_id"],
        result=issue["human_review_result"],
        reviewer=issue.get("reviewer"),
        comments=issue.get("reviewer_comments") or [],
        questions=issue.get("questions") or [],
    )


def _open_successor(session: Session, issue: dict[str, Any], attempt: str) -> None:
    """A rejection opens exactly one successor attempt, pending in DEV_FIXING."""
    session.attempts.open_attempt_if_absent(
        {
            **_attempt_base(issue, session.config),
            "attempt_id": issue["attempt_id"],
            "state": issue["state"],
            "supersedes_attempt_id": attempt,
        }
    )


def _persist_attempt(session: Session, issue: dict[str, Any], attempt: str) -> None:
    session.attempts.open_attempt_if_absent(
        {
            **_attempt_base(issue, session.config),
            "attempt_id": attempt,
            "state": State.DEV_REVIEW.value,
        }
    )
    if issue["human_review_result"] != "PENDING":
        _record_decision(session, issue, attempt)
    if issue["attempt_id"] != attempt:
        _open_successor(session, issue, attempt)
    issue["rejection_history"] = session.attempts.rejection_history(issue["issue_id"])


def _audit_decision(
    session: Session, issue: dict[str, Any], attempt: str, decision: review.Decision
) -> None:
    session.audit.record(
        "HUMAN_DECISION",
        issue_id=issue["issue_id"],
        attempt_id=attempt,
        stage=Stage.DEV_REVIEW.value,
        detail={"result": issue["human_review_result"], "source": decision.source_file},
    )


def _review_issue(
    session: Session, issue: dict[str, Any], recorded: dict[str, review.Decision]
) -> None:
    attempt = issue["attempt_id"]
    decision = _find_decision(recorded, issue, attempt)
    if decision is None:
        issue["human_review_result"] = "PENDING"
    else:
        _apply_outcome(issue, review.apply_decision(issue, decision))
        _audit_decision(session, issue, attempt, decision)
    _persist_attempt(session, issue, attempt)


def _publish_review(session: Session, issues: list[dict[str, Any]]) -> dict[str, Any]:
    views = [_stage_issue_view(issue, Stage.DEV_REVIEW, issue["state"]) for issue in issues]
    doc = _document(
        session.context, Stage.DEV_REVIEW, views, session.config, State.DEV_REVIEW.value, None
    )
    stage_input = _input_reference(
        session.paths, Stage.DEV_REVIEW, session.date, session.run, Stage.DEV_FIX
    )
    session.written += _write_stage(
        session.paths,
        Stage.DEV_REVIEW,
        session.date,
        session.run,
        stage_input,
        doc,
        render.dev_review(doc),
    )
    return doc


def dev_review(session: Session, issues: list[dict[str, Any]]) -> dict[str, Any]:
    """Apply any committed human decisions and stop. V1 promotes no further."""
    recorded = review.load_decisions(session.artifact_root)
    for issue in issues:
        _review_issue(session, issue, recorded)
    return _publish_review(session, issues)


def _write_text(session: Session, suffix: str, body: str) -> Path:
    path = session.paths.root / f"{session.date}_{session.run}_{suffix}"
    path.write_text(body, encoding="utf-8")
    session.written.append(path)
    return path


def _write_metrics(session: Session, issues: list[dict[str, Any]]) -> dict[str, Any]:
    run_metrics = metrics_module.collect(
        issues, session.context.run_flags, session.config.dry_run_mode
    )
    body = json.dumps(run_metrics, indent=2, sort_keys=True) + "\n"
    _write_text(session, "METRICS.json", body)
    return run_metrics


def _write_supervisor_report(session: Session, issues: list[dict[str, Any]]) -> None:
    """The supervisor's view: one row per in-scope task, in markdown and CSV."""
    markdown = supervisor.markdown_report(
        issues, report_date=session.date, run=session.run, dry_run=session.config.dry_run_mode
    )
    _write_text(session, "SUPERVISOR_REPORT.md", markdown)
    _write_text(session, "SUPERVISOR_REPORT.csv", supervisor.csv_report(issues))


def _finish(
    session: Session, issues: list[dict[str, Any]], review_doc: dict[str, Any]
) -> dict[str, Any]:
    run_metrics = _write_metrics(session, issues)
    _write_text(session, "SUMMARY.md", render.run_summary(review_doc, run_metrics))
    _write_supervisor_report(session, issues)
    session.audit.record("RUN_COMPLETE", detail={"metrics": run_metrics})
    return run_metrics


def run(
    config: Config,
    *,
    report_date: str | None = None,
    repository_root: Path,
    limit: int = planner.CANDIDATE_LIMIT,
) -> Result:
    """Execute the full Version 1 flow for one report date."""
    session = _open_session(config, repository_root, report_date)
    manifest = pre_stage(session)
    issues = intake(session, manifest)
    triage(session, issues, limit)
    registry, matches = playbook_match(session, issues)
    plan(session, issues, registry, matches)
    review_doc = dev_review(session, dev_fix(session, issues))
    run_metrics = _finish(session, issues, review_doc)
    return Result(
        run_context=session.context,
        manifest=manifest,
        issues=issues,
        metrics=run_metrics,
        paths=session.paths,
        written=session.written,
    )
