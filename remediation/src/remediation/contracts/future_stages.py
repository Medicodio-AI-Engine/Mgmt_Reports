"""QA, UAT, release, and learning interface contracts (disabled in Version 1).

Each builder produces a document validated against
``future_stage_contracts.schema.json``, so the shape downstream stages will
consume is fixed now. Every entry point requires an explicit ``enabled`` flag,
which the Version 1 pipeline never sets.
"""

from __future__ import annotations

from typing import Any

from .. import schema
from . import require_enabled

SCHEMA = schema.FUTURE_STAGE_CONTRACTS


def qa_result(
    issue: dict[str, Any],
    qa_cases: list[dict[str, Any]],
    executions: list[dict[str, Any]],
    verdict: str,
    *,
    failure_category: str | None = None,
    enabled: bool = False,
) -> dict[str, Any]:
    require_enabled("06_QA", enabled)
    document = {
        "run_id": issue["run_id"],
        "issue_id": issue["issue_id"],
        "attempt_id": issue["attempt_id"],
        "promoted": True,
        "promotion_reference": None,
        "qa_cases": qa_cases,
        "executions": executions,
        "verdict": verdict,
        "failure_category": failure_category,
        "evidence": [],
        "routes_back_to_dev": verdict == "FAIL" and failure_category == "CODE_DEFECT",
        "summary": None,
    }
    schema.validate(document, SCHEMA, "qa_result")
    return document


def uat_result(
    issue: dict[str, Any],
    verdict: str,
    *,
    enabled: bool = False,
) -> dict[str, Any]:
    require_enabled("07_UAT", enabled)
    document = {
        "run_id": issue["run_id"],
        "issue_id": issue["issue_id"],
        "attempt_id": issue["attempt_id"],
        "verdict": verdict,
        "returns_to": "QA_TESTING" if verdict == "FAIL" else "RELEASE_READY",
        "evidence": [],
        "notes": None,
    }
    schema.validate(document, SCHEMA, "uat_result")
    return document


def release_readiness(
    issue: dict[str, Any],
    *,
    approvals_complete: bool,
    tests_passed: bool,
    qa_passed: bool,
    uat_passed: bool,
    unresolved_blockers: list[str],
    rollback_plan: str | None,
    deployment_procedure: str | None,
    change_references: list[str],
    enabled: bool = False,
) -> dict[str, Any]:
    require_enabled("08_RELEASE", enabled)
    document = {
        "run_id": issue["run_id"],
        "issue_id": issue["issue_id"],
        "attempt_id": issue["attempt_id"],
        "approvals_complete": approvals_complete,
        "tests_passed": tests_passed,
        "qa_passed": qa_passed,
        "uat_passed": uat_passed,
        "unresolved_blockers": unresolved_blockers,
        "rollback_plan": rollback_plan,
        "deployment_procedure": deployment_procedure,
        "change_references": change_references,
        "evidence": [],
        "release_ready": all(
            [approvals_complete, tests_passed, qa_passed, uat_passed, not unresolved_blockers]
        ),
        "rollback_evidence": [],
    }
    schema.validate(document, SCHEMA, "release_readiness")
    return document


def learning_record(
    issue: dict[str, Any], attempts: int, *, enabled: bool = False
) -> dict[str, Any]:
    """Learning records are observational. They never widen permissions."""
    require_enabled("09_LEARNING", enabled)
    document = {
        "issue_id": issue["issue_id"],
        "playbook_id": (issue.get("playbook_match") or {}).get("playbook_id"),
        "category": issue["category"],
        "priority": (issue.get("priority") or {}).get("score"),
        "complexity": (issue.get("complexity") or {}).get("score"),
        "autonomy_tier": issue.get("autonomy_tier"),
        "attempts": attempts,
        "rejections": len(issue.get("rejection_history") or []),
        "questions": len(issue.get("questions") or []),
        "time_to_fix_seconds": None,
        "time_to_qa_seconds": None,
        "time_to_uat_seconds": None,
        "qa_first_pass": None,
        "uat_first_pass": None,
        "rolled_back": None,
        "false_positive": None,
        "human_intervention": True,
        "playbook_outcome": "UNKNOWN",
    }
    schema.validate(document, SCHEMA, "learning_record")
    return document
