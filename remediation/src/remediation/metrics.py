"""Run metrics.

Counts only what the run actually observed. Metrics are reported for human
judgment; they never expand permissions on their own — a successful execution
does not raise any autonomy tier.
"""

from __future__ import annotations

from collections import Counter
from typing import Any


def collect(issues: list[dict[str, Any]], run_flags: list[str], dry_run: bool) -> dict[str, Any]:
    tiers = Counter(issue.get("autonomy_tier") or "UNASSIGNED" for issue in issues)
    categories = Counter(issue["category"] for issue in issues)
    remediability = Counter(issue["remediable"] for issue in issues)
    states = Counter(issue["state"] for issue in issues)
    matched = [issue for issue in issues if (issue.get("playbook_match") or {}).get("playbook_id")]
    blocked = [issue for issue in issues if issue.get("guardrail_violations")]

    return {
        "issues_total": len(issues),
        "issues_by_category": dict(sorted(categories.items())),
        "issues_by_remediability": dict(sorted(remediability.items())),
        "issues_by_autonomy_tier": dict(sorted(tiers.items())),
        "issues_by_state": dict(sorted(states.items())),
        "playbook_match_rate": round(len(matched) / len(issues), 3) if issues else 0.0,
        "issues_without_playbook": [
            issue["issue_id"]
            for issue in issues
            if not (issue.get("playbook_match") or {}).get("playbook_id")
        ],
        "guardrail_blocked_count": len(blocked),
        "guardrail_rules_fired": dict(
            sorted(
                Counter(
                    violation["rule"]
                    for issue in issues
                    for violation in issue.get("guardrail_violations") or []
                ).items()
            )
        ),
        "missing_capabilities": dict(
            sorted(
                Counter(
                    skill for issue in issues for skill in issue.get("missing_skills") or []
                ).items()
            )
        ),
        "executions_performed": 0
        if dry_run
        else sum(1 for issue in issues if (issue.get("fix") or {}).get("executed")),
        "repositories_modified": [],
        "commits_created": 0,
        "pull_requests_created": 0,
        "human_decisions_recorded": sum(
            1 for issue in issues if issue.get("human_review_result") not in {None, "PENDING"}
        ),
        "awaiting_human_decision": [
            issue["issue_id"]
            for issue in issues
            if issue.get("human_review_result") in {None, "PENDING"}
        ],
        "run_flags": run_flags,
        "dry_run": dry_run,
    }
