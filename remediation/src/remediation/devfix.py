"""Dev remediation execution (stage 04_DEV_FIX).

In the pilot every execution path is suppressed: dry-run mode is on and no
engineering repository is allowlisted, so this stage records precisely what would
have been done and why it was not done. The suppression is asserted here rather
than assumed, so a configuration mistake fails loudly instead of writing to a
repository.
"""

from __future__ import annotations

from typing import Any

from .config import Config
from .states import State


class ExecutionSuppressed(RuntimeError):
    """Raised if execution is reached while writes are not permitted."""


def _suppression_reasons(issue: dict[str, Any], config: Config) -> list[str]:
    reasons: list[str] = []
    if config.dry_run_mode:
        reasons.append(
            "DRY_RUN_MODE enabled: no branch, commit, PR, deployment, or external change"
        )
    repository = issue.get("repository")
    if repository is None:
        reasons.append("target repository unresolved")
    elif repository not in config.remediation_repository_allowlist:
        reasons.append(f"{repository} is not in remediation_repository_allowlist")
    return reasons


def execute(issue: dict[str, Any], plan: dict[str, Any], config: Config) -> dict[str, Any]:
    """Record the fix attempt. Performs no repository or external mutation."""
    reasons = _suppression_reasons(issue, config)
    if plan["execution_allowed"] and reasons:
        raise ExecutionSuppressed(
            f"{issue['attempt_id']}: plan requested execution while writes are not permitted: "
            + "; ".join(reasons)
        )
    if plan["execution_allowed"] and not reasons:
        # Real execution is intentionally not implemented in Version 1: the pilot is
        # dry-run only, and enabling writes must be a deliberate, reviewed change.
        raise ExecutionSuppressed(
            f"{issue['attempt_id']}: write execution is not implemented in Version 1; "
            "re-enable only with an explicit design change and human approval"
        )

    would_do = [
        f"create working branch devin/{issue['issue_id'].lower()}-attempt-"
        f"{issue['attempt_id'].rsplit('_', 1)[-1]}",
        *[f"plan step: {step}" for step in plan["implementation_plan"]],
        *[
            f"run {entry['phase']}: {entry['command']}"
            for entry in plan["verification_commands"]
            if entry.get("command")
        ],
    ]

    return {
        "executed": False,
        "dry_run": True,
        "suppression_reasons": reasons,
        "would_have_done": would_do,
        "branch": None,
        "changed_files": [],
        "commands_executed": [],
        "test_cases_generated": [
            case["test_id"] for case in plan["test_plan"] if not case["generated"]
        ],
        "test_results": [],
        "pre_fix_failure": None,
        "post_fix_success": None,
        "full_suite_result": None,
        "commit_sha": None,
        "pr_number": None,
        "external_systems_changed": [],
        "statement": (
            "DRY RUN: no repository was modified, no commit or pull request was created, nothing "
            "was deployed, and no external system was changed."
        ),
        "next_state": State.DEV_REVIEW.value,
    }
