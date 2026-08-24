"""Stage orchestration for the Version 1 flow.

``PRE_STAGE`` → ``00_INTAKE`` → ``01_TRIAGE`` → ``02_PLAYBOOK_MATCH`` →
``03_PLAN`` → ``04_DEV_FIX`` → ``05_DEV_REVIEW``, then stop.

Every stage writes ``INPUT.json`` (what it consumed), ``OUTPUT_DEVIN_AI.json``
(schema-validated machine output) and ``OUTPUT_PEOPLE_ENGINEER.md`` (the human
document). A stage never runs on data that failed validation.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from . import (
    autonomy,
    dedupe,
    devfix,
    discovery,
    extract,
    guardrails,
    ids,
    normalize,
    planner,
    playbooks,
    render,
    review,
    schema,
    scoring,
)
from . import (
    metrics as metrics_module,
)
from .attempts import AttemptStore
from .audit import AuditLog
from .config import Config
from .naming import Audience, Stage, artifact_name, run_id
from .states import State, transition


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


def next_run_id(root: Path) -> str:
    """Allocate the next run id by inspecting existing run directories."""
    existing = [
        int(path.name.removeprefix("RUN_"))
        for path in root.glob("*/RUN_*")
        if path.is_dir() and path.name.removeprefix("RUN_").isdigit()
    ]
    return run_id(max(existing, default=0) + 1)


def _write_stage(
    paths: RunPaths,
    stage: Stage,
    report_date: str,
    run: str,
    stage_input: Any,
    machine: dict[str, Any],
    human: str,
) -> list[Path]:
    directory = paths.stage_dir(stage)
    written: list[Path] = []
    input_path = directory / artifact_name(report_date, run, stage, "INPUT")
    input_path.write_text(
        json.dumps(stage_input, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    written.append(input_path)
    written.append(
        schema.write_json(
            machine,
            directory / artifact_name(report_date, run, stage, "OUTPUT", Audience.DEVIN_AI),
            schema.STAGE_OUTPUT,
        )
    )
    human_path = directory / artifact_name(
        report_date, run, stage, "OUTPUT", Audience.PEOPLE_ENGINEER, extension="md"
    )
    human_path.write_text(human, encoding="utf-8")
    written.append(human_path)
    return written


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


def run(
    config: Config,
    *,
    report_date: str | None = None,
    repository_root: Path,
    limit: int = planner.CANDIDATE_LIMIT,
) -> Result:
    """Execute the full Version 1 flow for one report date."""
    directory = repository_root / config.mgmt_reports_directory
    artifact_root = config.artifact_root_directory
    artifact_root.mkdir(parents=True, exist_ok=True)
    run_identifier = next_run_id(artifact_root)

    context = discovery.assemble(
        config, directory, run_identifier, requested_report_date=report_date
    )
    paths = RunPaths(artifact_root / context.report_date / context.run_id)
    paths.root.mkdir(parents=True, exist_ok=True)
    audit = AuditLog(paths.root / "audit.jsonl", context.run_id)
    # Identity and history live above the per-run directory: an issue id and its
    # attempts must keep their meaning across runs and report dates.
    attempts = AttemptStore(artifact_root / "attempts.jsonl")
    issue_ids = ids.IssueRegistry.load(artifact_root / "issue_registry.json")
    written: list[Path] = []

    # ---- PRE_STAGE: source discovery -------------------------------------
    manifest = context.manifest(config)
    written.append(
        schema.write_json(
            manifest,
            paths.stage_dir(Stage.PRE_STAGE)
            / artifact_name(context.report_date, context.run_id, Stage.PRE_STAGE, "MANIFEST"),
            schema.PRE_STAGE_MANIFEST,
        )
    )
    audit.record(
        "SOURCE_DISCOVERY",
        stage=Stage.PRE_STAGE.value,
        detail={
            "completeness": context.completeness.value,
            "sources": [s.path.name for s in context.sources],
            "warnings": context.warnings,
        },
    )
    if not context.processable:
        raise PipelineError(
            f"source discovery is {context.completeness.value} for {context.report_date}: "
            + "; ".join(context.warnings)
        )

    # ---- 00_INTAKE: extract, dedupe, normalize ---------------------------
    findings = [finding for source in context.sources for finding in extract.extract(source)]
    clusters = dedupe.cluster(findings)
    issues = normalize.normalize(
        clusters,
        context,
        config.mgmt_reports_repository,
        redact_ratings=config.redact_employee_ratings,
        allocate_id=issue_ids.resolve,
        attempt_number=attempts.current_number,
    )
    issue_ids.save()
    for issue in issues:
        schema.validate(issue, schema.ISSUE)
    audit.record(
        "INTAKE",
        stage=Stage.INTAKE.value,
        detail={"findings": len(findings), "issues": len(issues)},
    )
    for issue in issues:
        record = transition(State.DISCOVERED, State.TRIAGED, "normalized from report evidence")
        issue["state"] = record.to_state.value

    intake_doc = _document(
        context,
        Stage.INTAKE,
        [_stage_issue_view(issue, Stage.INTAKE, State.TRIAGED.value) for issue in issues],
        config,
        State.TRIAGED.value,
        artifact_name(context.report_date, context.run_id, Stage.TRIAGE, "INPUT"),
    )
    written += _write_stage(
        paths,
        Stage.INTAKE,
        context.report_date,
        context.run_id,
        manifest,
        intake_doc,
        render.intake(intake_doc, manifest),
    )

    # ---- 01_TRIAGE: priority and complexity ------------------------------
    for issue in issues:
        issue.update(scoring.score(issue))
    selected = planner.select_candidates(issues, limit)
    for issue in issues:
        issue["selected_for_attention"] = issue["issue_id"] in selected
        record = transition(State.TRIAGED, State.PLAYBOOK_MATCHED, "scored and ordered")
        issue["state"] = record.to_state.value
    triage_doc = _document(
        context,
        Stage.TRIAGE,
        [_stage_issue_view(issue, Stage.TRIAGE, State.PLAYBOOK_MATCHED.value) for issue in issues],
        config,
        State.PLAYBOOK_MATCHED.value,
        artifact_name(context.report_date, context.run_id, Stage.PLAYBOOK_MATCH, "INPUT"),
    )
    written += _write_stage(
        paths,
        Stage.TRIAGE,
        context.report_date,
        context.run_id,
        _input_reference(paths, Stage.TRIAGE, context.report_date, context.run_id, Stage.INTAKE),
        triage_doc,
        render.triage(triage_doc),
    )
    audit.record("TRIAGE", stage=Stage.TRIAGE.value, detail={"selected": selected})

    # ---- 02_PLAYBOOK_MATCH ----------------------------------------------
    registry = playbooks.load_registry(config)
    matches: dict[str, playbooks.Match] = {}
    for issue in issues:
        match = playbooks.match(issue, registry, config)
        matches[issue["issue_id"]] = match
        issue["playbook_match"] = match.as_dict()
        issue["skills_required"] = match.skills_required
        issue["skills_available"] = match.skills_available
        issue["missing_skills"] = match.missing_skills
        record = transition(State.PLAYBOOK_MATCHED, State.PLANNED, "playbook resolved")
        issue["state"] = record.to_state.value
    match_doc = _document(
        context,
        Stage.PLAYBOOK_MATCH,
        [_stage_issue_view(issue, Stage.PLAYBOOK_MATCH, State.PLANNED.value) for issue in issues],
        config,
        State.PLANNED.value,
        artifact_name(context.report_date, context.run_id, Stage.PLAN, "INPUT"),
    )
    written += _write_stage(
        paths,
        Stage.PLAYBOOK_MATCH,
        context.report_date,
        context.run_id,
        _input_reference(
            paths, Stage.PLAYBOOK_MATCH, context.report_date, context.run_id, Stage.TRIAGE
        ),
        match_doc,
        render.playbook_match(match_doc),
    )
    audit.record(
        "PLAYBOOK_MATCH",
        stage=Stage.PLAYBOOK_MATCH.value,
        detail={
            issue["issue_id"]: (issue["playbook_match"] or {}).get("playbook_id")
            for issue in issues
        },
    )

    # ---- 03_PLAN: autonomy, guardrails, plan -----------------------------
    for issue in issues:
        match = matches[issue["issue_id"]]
        decision = autonomy.classify(issue, match, registry, config)
        violations = guardrails.evaluate(issue, match, decision, config)
        issue.update(decision.as_dict())
        issue["guardrail_violations"] = [violation.as_dict() for violation in violations]
        issue["plan"] = planner.plan(issue, match, decision, violations, config)
        issue["rollback_plan"] = issue["plan"]["rollback_plan"]
        issue["proposed_action"] = issue["plan"]["proposed_action"]
        issue["implementation_plan"] = issue["plan"]["implementation_plan"]
        if violations:
            issue["state"] = State.BLOCKED.value
            audit.record(
                "GUARDRAIL_BLOCK",
                issue_id=issue["issue_id"],
                attempt_id=issue["attempt_id"],
                stage=Stage.PLAN.value,
                detail={"violations": issue["guardrail_violations"]},
            )
        else:
            record = transition(State.PLANNED, State.DEV_FIXING, "plan produced")
            issue["state"] = record.to_state.value
    plan_doc = _document(
        context,
        Stage.PLAN,
        [
            _stage_issue_view(
                issue,
                Stage.PLAN,
                State.BLOCKED.value if issue["guardrail_violations"] else State.DEV_FIXING.value,
            )
            for issue in issues
        ],
        config,
        State.DEV_FIXING.value,
        artifact_name(context.report_date, context.run_id, Stage.DEV_FIX, "INPUT"),
    )
    written += _write_stage(
        paths,
        Stage.PLAN,
        context.report_date,
        context.run_id,
        _input_reference(
            paths, Stage.PLAN, context.report_date, context.run_id, Stage.PLAYBOOK_MATCH
        ),
        plan_doc,
        render.plan(plan_doc),
    )

    # ---- 04_DEV_FIX: dry-run record --------------------------------------
    actionable = [issue for issue in issues if not issue["guardrail_violations"]]
    for issue in actionable:
        issue["fix"] = devfix.execute(issue, issue["plan"], config)
        issue["changed_files"] = issue["fix"]["changed_files"]
        issue["commands_executed"] = issue["fix"]["commands_executed"]
        issue["test_cases_generated"] = issue["fix"]["test_cases_generated"]
        issue["test_results"] = issue["fix"]["test_results"]
        issue["pre_fix_failure"] = issue["fix"]["pre_fix_failure"]
        issue["post_fix_success"] = issue["fix"]["post_fix_success"]
        issue["full_suite_result"] = issue["fix"]["full_suite_result"]
        issue["commit_sha"] = issue["fix"]["commit_sha"]
        issue["pr_number"] = issue["fix"]["pr_number"]
        record = transition(State.DEV_FIXING, State.DEV_REVIEW, "dry-run attempt recorded")
        issue["state"] = record.to_state.value
        audit.record(
            "DEV_FIX_DRY_RUN",
            issue_id=issue["issue_id"],
            attempt_id=issue["attempt_id"],
            stage=Stage.DEV_FIX.value,
            detail={"suppression_reasons": issue["fix"]["suppression_reasons"]},
        )
    fix_doc = _document(
        context,
        Stage.DEV_FIX,
        [_stage_issue_view(issue, Stage.DEV_FIX, State.DEV_REVIEW.value) for issue in actionable],
        config,
        State.DEV_REVIEW.value,
        artifact_name(context.report_date, context.run_id, Stage.DEV_REVIEW, "INPUT"),
    )
    written += _write_stage(
        paths,
        Stage.DEV_FIX,
        context.report_date,
        context.run_id,
        _input_reference(paths, Stage.DEV_FIX, context.report_date, context.run_id, Stage.PLAN),
        fix_doc,
        render.dev_fix(fix_doc),
    )

    # ---- 05_DEV_REVIEW: decisions ----------------------------------------
    recorded = review.load_decisions(artifact_root)
    for issue in actionable:
        reviewed_attempt = issue["attempt_id"]
        # An unscoped block (no attempt id in the heading) only ever addresses the
        # first attempt, so a stale decision cannot travel to a later one.
        decision = recorded.get(reviewed_attempt)
        if decision is None and reviewed_attempt.endswith("_ATTEMPT_01"):
            decision = recorded.get(issue["issue_id"])
        if decision is not None:
            outcome = review.apply_decision(issue, decision)
            issue.update(
                {
                    "human_review_result": outcome["human_review_result"],
                    "reviewer": outcome["reviewer"],
                    "reviewer_comments": outcome["reviewer_comments"],
                    "questions": outcome["questions"],
                    "answers": outcome["answers"],
                    "attempt_id": outcome["attempt_id"],
                    "state": outcome["state"],
                    "review_notes": outcome["notes"],
                }
            )
            audit.record(
                "HUMAN_DECISION",
                issue_id=issue["issue_id"],
                attempt_id=reviewed_attempt,
                stage=Stage.DEV_REVIEW.value,
                detail={"result": outcome["human_review_result"], "source": decision.source_file},
            )
        else:
            issue["human_review_result"] = "PENDING"

        base = {
            "issue_id": issue["issue_id"],
            "run_id": issue["run_id"],
            "autonomy_tier": issue.get("autonomy_tier"),
            "playbook_id": (issue.get("playbook_match") or {}).get("playbook_id"),
            "dry_run": config.dry_run_mode,
        }
        attempts.open_attempt_if_absent(
            {**base, "attempt_id": reviewed_attempt, "state": State.DEV_REVIEW.value}
        )
        # The decision is a fact about the attempt that was reviewed; a rejection
        # additionally opens a successor attempt, pending in DEV_FIXING.
        if issue["human_review_result"] != "PENDING":
            attempts.record_decision(
                attempt_id=reviewed_attempt,
                issue_id=issue["issue_id"],
                run_id=issue["run_id"],
                result=issue["human_review_result"],
                reviewer=issue.get("reviewer"),
                comments=issue.get("reviewer_comments") or [],
                questions=issue.get("questions") or [],
            )
        if issue["attempt_id"] != reviewed_attempt:
            attempts.open_attempt_if_absent(
                {
                    **base,
                    "attempt_id": issue["attempt_id"],
                    "state": issue["state"],
                    "supersedes_attempt_id": reviewed_attempt,
                }
            )
        issue["rejection_history"] = attempts.rejection_history(issue["issue_id"])
    review_doc = _document(
        context,
        Stage.DEV_REVIEW,
        [_stage_issue_view(issue, Stage.DEV_REVIEW, issue["state"]) for issue in actionable],
        config,
        State.DEV_REVIEW.value,
        None,
    )
    written += _write_stage(
        paths,
        Stage.DEV_REVIEW,
        context.report_date,
        context.run_id,
        _input_reference(
            paths, Stage.DEV_REVIEW, context.report_date, context.run_id, Stage.DEV_FIX
        ),
        review_doc,
        render.dev_review(review_doc),
    )

    # ---- metrics ---------------------------------------------------------
    run_metrics = metrics_module.collect(issues, context.run_flags, config.dry_run_mode)
    metrics_path = paths.root / f"{context.report_date}_{context.run_id}_METRICS.json"
    metrics_path.write_text(
        json.dumps(run_metrics, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    written.append(metrics_path)
    summary_path = paths.root / f"{context.report_date}_{context.run_id}_SUMMARY.md"
    summary_path.write_text(render.run_summary(review_doc, run_metrics), encoding="utf-8")
    written.append(summary_path)
    audit.record("RUN_COMPLETE", detail={"metrics": run_metrics})

    return Result(
        run_context=context,
        manifest=manifest,
        issues=issues,
        metrics=run_metrics,
        paths=paths,
        written=written,
    )
