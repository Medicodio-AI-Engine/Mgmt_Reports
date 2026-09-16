"""The supervisor report: required columns, scope handling, and honesty about the dry run."""

from __future__ import annotations

import csv
import io
from typing import Any

from remediation import scope, supervisor

EXPECTED_HEADERS = [
    "Task_ID",
    "Task_Name",
    "Task_Description",
    "Task_Owner",
    "Task_Type",
    "Category",
    "Revised_Category",
    "Category_Match",
    "Complexity",
    "Time_Human",
    "Time_AI",
    "Time_Human_AI",
    "Comments",
]


def _issue(**overrides: Any) -> dict[str, Any]:
    issue: dict[str, Any] = {
        "issue_id": "ISSUE-0001",
        "title": "Manual claim export repeated daily",
        "owner": "Asha",
        "remediable": "TOOLING_AUTOMATION",
        "complexity": {"score": 3},
        "priority": {"score": 7},
        "autonomy_tier": "B",
        "state": "DEV_REVIEW",
        "human_review_result": "PENDING",
        "analysis_scope": scope.IN_SCOPE,
        "scope_reason": "medicodio library in the pilot",
        "reported_category": "BUG",
        "revised_category": "ENHANCEMENT",
        "category_match": False,
        "category_rationale": "no prior implementation existed",
        "fix": {"executed": False},
        "guardrail_violations": [],
    }
    issue.update(overrides)
    return issue


def test_row_carries_every_supervisor_field() -> None:
    row = supervisor.row_for(_issue())
    assert row.task_owner == "Asha"
    assert row.task_type == "Tooling / automation"
    assert (row.category, row.revised_category, row.category_match) == ("BUG", "ENHANCEMENT", "no")
    assert row.complexity == "3"
    assert row.comments.startswith("no prior implementation existed")


def test_matching_categories_render_yes() -> None:
    row = supervisor.row_for(_issue(revised_category="BUG", category_match=True))
    assert row.category_match == "yes"


def test_unassigned_owner_is_stated_not_blank() -> None:
    assert supervisor.row_for(_issue(owner=None)).task_owner == "Unassigned"


def test_markdown_has_the_required_header_row() -> None:
    report = supervisor.markdown_report(
        [_issue()], report_date="2026_08_23", run="RUN-1", dry_run=True
    )
    header = next(line for line in report.splitlines() if line.startswith("| Task_ID"))
    assert [cell.strip() for cell in header.strip("|").split("|")] == EXPECTED_HEADERS


def test_markdown_states_that_nothing_was_changed() -> None:
    report = supervisor.markdown_report(
        [_issue()], report_date="2026_08_23", run="RUN-1", dry_run=True
    )
    assert "no repository was modified" in report
    assert "planning estimates" in report


def test_out_of_scope_issues_are_listed_but_not_rows() -> None:
    excluded = _issue(
        issue_id="ISSUE-0002",
        title="CI has no successful runs in globalcodio-monorepo",
        analysis_scope=scope.OUT_OF_SCOPE,
        scope_reason="globalcodio-monorepo is outside the pilot",
    )
    report = supervisor.markdown_report(
        [_issue(), excluded], report_date="2026_08_23", run="RUN-1", dry_run=True
    )
    assert "## Out of pilot scope (1)" in report
    assert "outside the pilot" in report
    assert [row.task_id for row in supervisor.rows([_issue(), excluded])] == ["ISSUE-0001"]


def test_rows_are_ordered_by_priority() -> None:
    low = _issue(issue_id="ISSUE-LOW", priority={"score": 2})
    high = _issue(issue_id="ISSUE-HIGH", priority={"score": 9})
    assert [row.task_id for row in supervisor.rows([low, high])] == ["ISSUE-HIGH", "ISSUE-LOW"]


def test_csv_matches_the_markdown_rows() -> None:
    issues = [_issue(), _issue(issue_id="ISSUE-0003", priority={"score": 1})]
    parsed = list(csv.reader(io.StringIO(supervisor.csv_report(issues))))
    assert parsed[0] == EXPECTED_HEADERS
    assert [line[0] for line in parsed[1:]] == [row.task_id for row in supervisor.rows(issues)]
    assert parsed[1][1:] == supervisor.rows(issues)[0].values()


def test_guardrail_block_is_explained_in_comments() -> None:
    blocked = _issue(
        guardrail_violations=[{"stop_reason": "security scope requires a human owner"}],
    )
    assert "blocked by guardrail" in supervisor.row_for(blocked).comments


def test_description_leads_with_the_work_that_was_carried_out() -> None:
    issue = _issue(
        description="KB wizard changes are mirrored across backend and UI by hand.",
        recommended_action="Use Devin for the paired backend/UI propagation.",
        code_review=[
            {
                "repository": "medicodio-nextgen-app-react",
                "checkout_available": True,
                "present_paths": ["src/kb/wizard.tsx"],
                "missing_paths": [],
                "source_file_count": 812,
                "work_done": {
                    "date": "2026_08_23",
                    "author": "hitesh",
                    "commit_count": 4,
                    "subjects": ["Add payer specialty guidelines"],
                    "files_changed": 11,
                    "insertions": 240,
                    "deletions": 18,
                    "history_available": True,
                },
            }
        ],
    )
    described = supervisor.row_for(issue).task_description
    assert described.startswith(
        "Work carried out: medicodio-nextgen-app-react: 4 commit(s) by hitesh"
    )
    assert "11 file(s) (240 insertion(s), 18 deletion(s)) against the previous version" in described
    assert '"Add payer specialty guidelines"' in described
    assert (
        "Code now: medicodio-nextgen-app-react reviewed read-only (812 source file(s))" in described
    )
    assert "Reported: KB wizard changes are mirrored" in described
    assert "Recommended: Use Devin for the paired" in described
    assert "Steps:" not in described
    assert "\n" not in described and "|" not in described


def test_corroborating_signal_is_counted_not_listed_as_a_task() -> None:
    card = _issue(
        issue_id="ISSUE-CARD",
        title="Low automation-adoption signal for a member",
        corroborating_only=True,
        priority={"score": 9},
    )
    issues = [_issue(), card]
    assert [row.task_id for row in supervisor.rows(issues)] == ["ISSUE-0001"]
    report = supervisor.markdown_report(issues, report_date="2026_08_23", run="RUN-1", dry_run=True)
    assert "## Corroborating signals (1)" in report
    assert "no individual rating is reproduced" in report


def test_column_order_matches_row_fields() -> None:
    assert len(supervisor.row_for(_issue()).values()) == len(supervisor.COLUMNS)
