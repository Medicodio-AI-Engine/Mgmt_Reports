"""The supervisor report: what needs fixing, and what this run changed.

One row per in-scope issue with the columns a supervisor signs off against: task,
description, owner, task type, reported category, revised category, whether they
match, complexity, the three time estimates, and a comment. Written as markdown
(review and diff in the pull request) and as CSV (open in a spreadsheet); the two
are generated from the same rows so they cannot disagree.

Out-of-scope issues are listed separately and counted, never silently dropped.
"""

from __future__ import annotations

import csv
import io
from dataclasses import dataclass
from typing import Any

from . import describe, effort, scope

COLUMNS = (
    ("task_name", "Task_Name"),
    ("task_description", "Task_Description"),
    ("task_owner", "Task_Owner"),
    ("task_type", "Task_Type"),
    ("category", "Category"),
    ("revised_category", "Revised_Category"),
    ("category_match", "Category_Match"),
    ("complexity", "Complexity"),
    ("time_human", "Time_Human"),
    ("time_ai", "Time_AI"),
    ("time_human_ai", "Time_Human_AI"),
    ("comments", "Comments"),
)

TASK_TYPES: dict[str, str] = {
    "CODE_CHANGE": "Code fix",
    "TOOLING_AUTOMATION": "Tooling / automation",
    "NON_CODE_PROCESS": "Process change",
    "UNKNOWN": "Investigation",
}

ESTIMATE_NOTE = (
    "Time columns are planning estimates derived from the analysed complexity, remediability and "
    "autonomy tier — not measurements. `Time_Human` is how long the task takes a person working "
    "alone; `Time_AI` is how long it takes Devin working alone, and for a tier C or D task it "
    "covers investigation and a proposal only, because policy forbids the AI from making that "
    "change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a "
    "person directs and reviews — so it is not the sum of the other two and is usually shorter "
    "than `Time_Human`. `Task_Description` states what was observed, what is proposed, and what a "
    "read-only look at the code found."
)


@dataclass(frozen=True)
class Row:
    """One supervisor line. Field order is the column order."""

    task_id: str
    task_name: str
    task_description: str
    task_owner: str
    task_type: str
    category: str
    revised_category: str
    category_match: str
    complexity: str
    time_human: str
    time_ai: str
    time_human_ai: str
    comments: str

    def values(self) -> list[str]:
        """Cell values in the column order supervisors expect."""
        return [
            self.task_name,
            self.task_description,
            self.task_owner,
            self.task_type,
            self.category,
            self.revised_category,
            self.category_match,
            self.complexity,
            self.time_human,
            self.time_ai,
            self.time_human_ai,
            self.comments,
        ]


def _owner(issue: dict[str, Any]) -> str:
    return str(issue.get("owner") or "Unassigned")


def _task_type(issue: dict[str, Any]) -> str:
    return TASK_TYPES.get(str(issue.get("remediable") or "UNKNOWN"), "Investigation")


def _complexity(issue: dict[str, Any]) -> str:
    score = (issue.get("complexity") or {}).get("score")
    return str(score) if score is not None else "—"


def _state_note(issue: dict[str, Any]) -> str:
    decision = issue.get("human_review_result") or "PENDING"
    return f"state {issue.get('state', '—')}, review {decision}"


def _blocked_note(issue: dict[str, Any]) -> str | None:
    violations = issue.get("guardrail_violations") or []
    if not violations:
        return None
    return "blocked by guardrail: " + "; ".join(v["stop_reason"] for v in violations)


def _change_note(issue: dict[str, Any]) -> str:
    fix = issue.get("fix") or {}
    if fix.get("executed"):
        return f"changed {len(fix.get('changed_files') or [])} file(s)"
    return "nothing changed (dry run)"


def _comments(issue: dict[str, Any]) -> str:
    parts = [issue.get("category_rationale") or "", _state_note(issue), _change_note(issue)]
    blocked = _blocked_note(issue)
    if blocked:
        parts.insert(1, blocked)
    return ". ".join(part for part in parts if part) + "."


def row_for(issue: dict[str, Any]) -> Row:
    """Build the supervisor row for one analysed issue."""
    estimate = effort.for_issue(issue)
    return Row(
        task_id=str(issue["issue_id"]),
        task_name=str(issue["title"]),
        task_description=str(issue.get("task_description") or describe.describe(issue)),
        task_owner=_owner(issue),
        task_type=_task_type(issue),
        category=str(issue.get("reported_category") or "—"),
        revised_category=str(issue.get("revised_category") or "—"),
        category_match="yes" if issue.get("category_match") else "no",
        complexity=_complexity(issue),
        time_human=estimate.human,
        time_ai=estimate.ai,
        time_human_ai=estimate.joint,
        comments=_comments(issue),
    )


def _in_scope(issue: dict[str, Any]) -> bool:
    return str(issue.get("analysis_scope") or scope.UNRESOLVED) != scope.OUT_OF_SCOPE


def _is_task(issue: dict[str, Any]) -> bool:
    """Corroborating signal is not work: it prioritises tasks, it is not one."""
    return _in_scope(issue) and not issue.get("corroborating_only")


def rows(issues: list[dict[str, Any]]) -> list[Row]:
    """Supervisor rows for the in-scope tasks, highest priority first."""
    selected = [issue for issue in issues if _is_task(issue)]
    selected.sort(key=lambda issue: -int((issue.get("priority") or {}).get("score", 0)))
    return [row_for(issue) for issue in selected]


def _header_lines() -> list[str]:
    return [
        "| Task_ID | " + " | ".join(label for _, label in COLUMNS) + " |",
        "| ------- | " + " | ".join("---" for _ in COLUMNS) + " |",
    ]


def _row_line(row: Row) -> str:
    cells = [cell.replace("|", "\\|") for cell in row.values()]
    return f"| `{row.task_id}` | " + " | ".join(cells) + " |"


def _totals(built: list[Row]) -> list[str]:
    bugs = sum(1 for row in built if row.revised_category == "BUG")
    mismatched = sum(1 for row in built if row.category_match == "no")
    return [
        f"- Tasks in scope: **{len(built)}** — {bugs} bug(s), {len(built) - bugs} enhancement(s)",
        f"- Reported category revised after analysis: **{mismatched}**",
    ]


def _corroborating_lines(issues: list[dict[str, Any]]) -> list[str]:
    """Count the support records without naming the individuals behind them."""
    count = sum(1 for issue in issues if _in_scope(issue) and issue.get("corroborating_only"))
    if not count:
        return []
    return [
        "",
        f"## Corroborating signals ({count})",
        "",
        f"{count} support record(s) from the rating cards helped prioritise the tasks above. "
        "They are not tasks, and no individual rating is reproduced here.",
    ]


def _out_of_scope_lines(issues: list[dict[str, Any]]) -> list[str]:
    excluded = [issue for issue in issues if not _in_scope(issue)]
    if not excluded:
        return []
    listed = [
        f"- `{issue['issue_id']}` {issue['title']} — {issue.get('scope_reason')}"
        for issue in excluded
    ]
    return ["", f"## Out of pilot scope ({len(excluded)})", "", *listed]


def _preamble(report_date: str, run: str, dry_run: bool) -> list[str]:
    return [
        "# Supervisor report — remediation tasks",
        "",
        f"**Run:** `{run}` · **Report date:** {report_date.replace('_', '-')}",
        "",
        "> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request "
        "was created. Every row is a task awaiting a human decision."
        if dry_run
        else "",
        "",
    ]


def markdown_report(
    issues: list[dict[str, Any]], *, report_date: str, run: str, dry_run: bool
) -> str:
    """Render the supervisor report as markdown."""
    built = rows(issues)
    lines = _preamble(report_date, run, dry_run)
    lines += _totals(built)
    lines += ["", *_header_lines(), *[_row_line(row) for row in built]]
    lines += _corroborating_lines(issues)
    lines += _out_of_scope_lines(issues)
    lines += ["", "---", "", ESTIMATE_NOTE, ""]
    return "\n".join(line for line in lines if line is not None)


def csv_report(issues: list[dict[str, Any]]) -> str:
    """Render the same rows as CSV for spreadsheet use."""
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["Task_ID", *[label for _, label in COLUMNS]])
    for row in rows(issues):
        writer.writerow([row.task_id, *row.values()])
    return buffer.getvalue()
