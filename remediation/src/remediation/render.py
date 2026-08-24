"""Human-facing stage documents (``OUTPUT_PEOPLE_ENGINEER.md``).

Written for the engineer or manager who has to decide something: what was found,
what the evidence is, what would be done, what is deliberately not being done,
and where to record the decision.
"""

from __future__ import annotations

from typing import Any

from .naming import Stage
from .review import decision_block

DRY_RUN_BANNER = (
    "> **Dry run.** No repository was modified, no commit or pull request was created, nothing "
    "was deployed, and no external system was changed. Everything below is analysis and proposal."
)


def _header(document: dict[str, Any], stage: Stage, title: str) -> list[str]:
    lines = [
        f"# {title}",
        "",
        f"**Run:** `{document['run_id']}` · **Report date:** {document['report_date'].replace('_', '-')} "
        f"· **Stage:** `{stage.value}` · **Status:** {document['status']}",
        "",
    ]
    if document.get("dry_run"):
        lines += [DRY_RUN_BANNER, ""]
    if document.get("warnings"):
        lines += ["**Warnings**", ""]
        lines += [f"- {warning}" for warning in document["warnings"]]
        lines += [""]
    return lines


def _issue_line(issue: dict[str, Any]) -> str:
    priority = (issue.get("priority") or {}).get("score", "—")
    complexity = (issue.get("complexity") or {}).get("score", "—")
    tier = issue.get("autonomy_tier") or "—"
    repository = issue.get("repository") or "unresolved"
    return (
        f"| `{issue['issue_id']}` | {issue['title']} | {issue['category']} | {repository} | "
        f"{priority} | {complexity} | {tier} | {issue['remediable']} |"
    )


def _issue_table(issues: list[dict[str, Any]]) -> list[str]:
    if not issues:
        return ["_No issues in this stage._", ""]
    return [
        "| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |",
        "| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |",
        *[_issue_line(issue) for issue in issues],
        "",
    ]


def intake(document: dict[str, Any], manifest: dict[str, Any]) -> str:
    lines = _header(document, Stage.INTAKE, "Intake — normalized findings")
    lines += [
        "## Sources",
        "",
        "| Source | Type | File | Date verified |",
        "| ------ | ---- | ---- | ------------- |",
    ]
    for source in manifest["source_files"]:
        lines.append(
            f"| {source['source_id']} | {source['report_type']} | `{source['filename']}` | "
            f"{'yes' if source['date_verified'] else 'no'} |"
        )
    lines += [
        "",
        f"Completeness: **{manifest['completeness']}**"
        + (
            f" — missing {', '.join(manifest['missing_sources'])}"
            if manifest["missing_sources"]
            else ""
        ),
        "",
        "## Normalized issues",
        "",
    ]
    lines += _issue_table(document["issues"])
    lines += [
        "Findings derived only from employee rating cards are marked corroborating-only and cannot "
        "justify a code change on their own.",
        "",
    ]
    return "\n".join(lines)


def triage(document: dict[str, Any]) -> str:
    lines = _header(document, Stage.TRIAGE, "Triage — priority and complexity")
    lines += _issue_table(document["issues"])
    lines += ["## Scoring rationale", ""]
    for issue in document["issues"]:
        lines += [
            f"### `{issue['issue_id']}` {issue['title']}",
            "",
            f"- Priority: {(issue.get('priority') or {}).get('rationale', '—')}",
            f"- Complexity: {(issue.get('complexity') or {}).get('rationale', '—')}",
            f"- Confidence: {issue.get('confidence')}",
            "",
        ]
    lines += [
        "Ordering confers no permission: what may actually be done is decided by the autonomy tier "
        "and the guardrail engine.",
        "",
    ]
    return "\n".join(lines)


def playbook_match(document: dict[str, Any]) -> str:
    lines = _header(document, Stage.PLAYBOOK_MATCH, "Playbook match and capability check")
    lines += [
        "| Issue | Playbook | Scope | Source | Confidence | Missing capabilities |",
        "| ----- | -------- | ----- | ------ | ---------- | -------------------- |",
    ]
    for issue in document["issues"]:
        match = issue.get("playbook_match") or {}
        lines.append(
            f"| `{issue['issue_id']}` | {match.get('playbook_id') or '—'} | "
            f"{match.get('playbook_scope') or '—'} | {match.get('source') or '—'} | "
            f"{match.get('confidence', 0)} | "
            f"{', '.join(issue.get('missing_skills') or []) or 'none'} |"
        )
    lines += [""]
    unmatched = [
        i for i in document["issues"] if not (i.get("playbook_match") or {}).get("playbook_id")
    ]
    if unmatched:
        lines += [
            "## Escalated: no approved playbook matched",
            "",
            *[f"- `{issue['issue_id']}` {issue['title']}" for issue in unmatched],
            "",
            "These need either human direction or a new approved playbook.",
            "",
        ]
    return "\n".join(lines)


def plan(document: dict[str, Any]) -> str:
    lines = _header(document, Stage.PLAN, "Plan — proposed actions and stop conditions")
    for issue in document["issues"]:
        planned = issue.get("plan") or {}
        lines += [
            f"## `{issue['issue_id']}` {issue['title']}",
            "",
            f"- Repository: {issue.get('repository') or 'unresolved'}",
            f"- Autonomy tier: **{issue.get('autonomy_tier')}** "
            f"({'execution permitted' if planned.get('execution_allowed') else 'no execution'})",
            f"- Proposed action: {planned.get('proposed_action')}",
            f"- Rollback: {planned.get('rollback_plan')}",
            "",
        ]
        if planned.get("implementation_plan"):
            lines += ["**Steps**", ""]
            lines += [f"{n}. {step}" for n, step in enumerate(planned["implementation_plan"], 1)]
            lines += [""]
        if planned.get("stop_conditions"):
            lines += ["**Stop conditions**", ""]
            lines += [f"- {condition}" for condition in planned["stop_conditions"]]
            lines += [""]
        if issue.get("guardrail_violations"):
            lines += ["**Guardrail violations**", ""]
            for violation in issue["guardrail_violations"]:
                lines += [
                    f"- `{violation['rule']}` — {violation['stop_reason']}",
                    f"  - Evidence: {'; '.join(violation['evidence'])}",
                    f"  - Required human action: {violation['required_human_action']}",
                ]
            lines += [""]
    return "\n".join(lines)


def dev_fix(document: dict[str, Any]) -> str:
    lines = _header(document, Stage.DEV_FIX, "Dev fix — dry-run record")
    for issue in document["issues"]:
        fix = issue.get("fix") or {}
        lines += [
            f"## `{issue['issue_id']}` {issue['title']}",
            "",
            f"- Attempt: `{issue['attempt_id']}`",
            f"- {fix.get('statement', 'No execution record.')}",
            "",
        ]
        if fix.get("suppression_reasons"):
            lines += ["**Why nothing was executed**", ""]
            lines += [f"- {reason}" for reason in fix["suppression_reasons"]]
            lines += [""]
        if fix.get("would_have_done"):
            lines += ["**What would have been done**", ""]
            lines += [f"- {item}" for item in fix["would_have_done"]]
            lines += [""]
    return "\n".join(lines)


def dev_review(document: dict[str, Any]) -> str:
    lines = _header(document, Stage.DEV_REVIEW, "Dev review — decisions required")
    lines += [
        "Record each decision in the block under the issue: set `DECISION:` to exactly one of "
        "`APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. "
        "The next run reads it back.",
        "",
        "Version 1 stops here. Approval does not promote anything to QA, UAT, or production.",
        "",
    ]
    for issue in document["issues"]:
        planned = issue.get("plan") or {}
        match = issue.get("playbook_match") or {}
        lines += [
            f"## `{issue['issue_id']}` {issue['title']}",
            "",
            f"- Category: {issue['category']} · Remediability: {issue['remediable']} · "
            f"Security scope: {issue['security_scope']}",
            f"- Priority: {(issue.get('priority') or {}).get('score')} · Complexity: "
            f"{(issue.get('complexity') or {}).get('score')} · Tier: {issue.get('autonomy_tier')}",
            f"- Playbook: {match.get('playbook_id') or 'none matched'}",
            f"- Proposed action: {planned.get('proposed_action')}",
            "",
            "**Evidence**",
            "",
        ]
        for item in issue["evidence"][:6]:
            lines.append(f"- [{item['kind']}] `{item['locator']}` — {item['excerpt']}")
        lines += [""]
        if issue.get("questions"):
            lines += ["**Open questions**", "", *[f"- {q}" for q in issue["questions"]], ""]
        if issue.get("rejection_history"):
            lines += ["**Rejection history**", ""]
            for record in issue["rejection_history"]:
                lines.append(
                    f"- `{record['attempt_id']}` rejected by {record.get('reviewer') or 'unknown'}: "
                    f"{'; '.join(record.get('comments') or []) or 'no comment'}"
                )
            lines += [""]
        if issue.get("human_review_result") and issue["human_review_result"] != "PENDING":
            lines += [
                f"**Recorded decision:** {issue['human_review_result']}"
                + (f" by {issue['reviewer']}" if issue.get("reviewer") else ""),
                "",
            ]
        lines += [decision_block(issue["attempt_id"], issue["title"]), ""]
    return "\n".join(lines)


def run_summary(document: dict[str, Any], metrics: dict[str, Any]) -> str:
    lines = [
        "# Remediation run summary",
        "",
        f"**Run:** `{document['run_id']}` · **Report date:** "
        f"{document['report_date'].replace('_', '-')} · **Status:** {document['status']}",
        "",
        DRY_RUN_BANNER,
        "",
        "| Metric | Value |",
        "| ------ | ----- |",
        f"| Issues normalized | {metrics['issues_total']} |",
        f"| Playbook match rate | {metrics['playbook_match_rate']} |",
        f"| Guardrail-blocked issues | {metrics['guardrail_blocked_count']} |",
        f"| Awaiting human decision | {len(metrics['awaiting_human_decision'])} |",
        f"| Commits created | {metrics['commits_created']} |",
        f"| Pull requests created | {metrics['pull_requests_created']} |",
        f"| Repositories modified | {len(metrics['repositories_modified'])} |",
        "",
        "## By autonomy tier",
        "",
        *[f"- {tier}: {count}" for tier, count in metrics["issues_by_autonomy_tier"].items()],
        "",
        "## By remediability",
        "",
        *[f"- {kind}: {count}" for kind, count in metrics["issues_by_remediability"].items()],
        "",
    ]
    if metrics["missing_capabilities"]:
        lines += [
            "## Missing capabilities",
            "",
            *[
                f"- {skill}: blocks {count} issue(s)"
                for skill, count in metrics["missing_capabilities"].items()
            ],
            "",
        ]
    return "\n".join(lines)
