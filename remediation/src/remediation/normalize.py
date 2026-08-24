"""Issue normalization.

Turns deduplicated report findings into schema-valid normalized issues. Unknown
values stay explicitly ``null``/``UNKNOWN`` — the normalizer never invents a
repository, path, branch, environment, owner, or security classification.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Any

from .dedupe import Cluster
from .discovery import RunContext
from .extract import RawFinding
from .naming import attempt_id, issue_id
from .states import State

SECURITY_MARKERS: tuple[tuple[str, str], ...] = (
    (r"\bphi\b|protected health", "PHI"),
    (r"tenant|rls\b|multi-?tenan|idor", "TENANT_ISOLATION"),
    (r"authoriz|permission|access control|rbac", "AUTHORIZATION"),
    (r"authenticat|login|session token|sso\b", "AUTHENTICATION"),
    (r"secret|credential|api key|token rotation", "SECRETS"),
    (r"billing|invoice|payment|pricing", "BILLING"),
)

PROCESS_CATEGORIES = frozenset({"PROCESS_PRACTICE", "REVIEW_FINDING"})
AUTOMATION_CATEGORIES = frozenset({"AUTOMATION_OPPORTUNITY"})
CODE_CATEGORIES = frozenset(
    {"MISSING_TEST", "MECHANICAL_MIGRATION", "CODE_DEFECT", "CODE_QUALITY", "SECURITY_TENANCY"}
)

_NUMBER = re.compile(r"\d+")


def security_scope(text: str, *, code_change: bool) -> str:
    lowered = text.lower()
    for pattern, scope in SECURITY_MARKERS:
        if re.search(pattern, lowered):
            return scope
    return "UNKNOWN" if code_change else "NONE"


def remediability(category: str, *, environment_signal: bool) -> str:
    if environment_signal or category == "CI_FAILURE":
        return "UNKNOWN"
    if category in CODE_CATEGORIES:
        return "CODE_CHANGE"
    if category in AUTOMATION_CATEGORIES:
        return "TOOLING_AUTOMATION"
    if category in PROCESS_CATEGORIES:
        return "NON_CODE_PROCESS"
    return "UNKNOWN"


def confidence(cluster: Cluster) -> float:
    if cluster.corroborating_only:
        return 0.3
    score = 0.5
    if cluster.support_count >= 2:
        score += 0.15
    if cluster.pr_references:
        score += 0.1
    if cluster.paths:
        score += 0.1
    if cluster.primary.frequency and _NUMBER.search(cluster.primary.frequency):
        score += 0.05
    if cluster.primary.prior_evidence:
        score += 0.05
    return round(min(score, 0.9), 2)


RATING_REDACTION = (
    "[rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]"
)


def _quote(finding: RawFinding, redact_ratings: bool) -> str:
    """Rating-card rows carry individual scores, so they are quoted by locator only."""
    if redact_ratings and finding.source_report_type == "EMPLOYEE_RATING_CARDS":
        return RATING_REDACTION
    return finding.quote


def _evidence(cluster: Cluster, redact_ratings: bool) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for finding in cluster.all_findings:
        items.append(
            {
                "kind": "REPORT_OBSERVATION",
                "locator": f"{finding.source_id}:{finding.source_line}",
                "excerpt": _quote(finding, redact_ratings),
            }
        )
        if finding.recommended_action:
            items.append(
                {
                    "kind": "RECOMMENDATION",
                    "locator": f"{finding.source_id}:{finding.source_line}",
                    "excerpt": finding.recommended_action,
                }
            )
        if finding.prior_evidence:
            items.append(
                {
                    "kind": "REPORT_OBSERVATION",
                    "locator": f"{finding.source_id}:{finding.source_line}",
                    "excerpt": f"previous evidence: {finding.prior_evidence}",
                }
            )
    return items


def _provenance(
    cluster: Cluster, run: RunContext, repository: str, redact_ratings: bool
) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for finding in cluster.all_findings:
        source = next(
            (s for s in run.sources if s.source_id == finding.source_id),
            None,
        )
        entries.append(
            {
                "source_id": finding.source_id,
                "report_date": run.report_date,
                "report_type": finding.source_report_type,
                "repository": repository,
                "repository_path": (
                    f"{run.source_directory}/{source.path.name}" if source else run.source_directory
                ),
                "section": finding.finding_key.split("|", 1)[0],
                "member": finding.subject,
                "finding_reference": f"line {finding.source_line}",
                "evidence_excerpt_or_locator": _quote(finding, redact_ratings),
            }
        )
    return entries


def _reproduction(cluster: Cluster) -> dict[str, Any]:
    if cluster.environment_signal:
        return {
            "available": False,
            "method": None,
            "notes": (
                "Environment signal, not a reproducible software defect. Requires infrastructure "
                "verification before any code conclusion is drawn."
            ),
        }
    if cluster.primary.category == "MISSING_TEST":
        return {
            "available": False,
            "method": "TEST_TO_BE_WRITTEN",
            "notes": (
                "No reproduction exists yet: the finding is absence of coverage. A generated test "
                "must first demonstrate the uncovered behavior."
            ),
        }
    return {
        "available": False,
        "method": None,
        "notes": (
            "Derived from a management report statement; no execution-level reproduction was "
            "attempted (dry-run pilot performs no repository work)."
        ),
    }


def normalize(
    clusters: list[Cluster],
    run: RunContext,
    mgmt_repository: str,
    *,
    redact_ratings: bool = True,
    allocate_id: Callable[[str], str] | None = None,
    attempt_number: Callable[[str], int] | None = None,
) -> list[dict[str, Any]]:
    """Emit schema-valid normalized issues with stable identities.

    ``allocate_id`` maps a dedupe signature to an issue id and defaults to
    positional allocation; pass an :class:`~remediation.ids.IssueRegistry` resolver
    so an id keeps its meaning across runs.
    """
    issues: list[dict[str, Any]] = []
    for index, cluster in enumerate(clusters, start=1):
        primary = cluster.primary
        identifier = allocate_id(cluster.signature) if allocate_id is not None else issue_id(index)
        attempt = attempt_number(identifier) if attempt_number is not None else 1
        code_change = primary.category in CODE_CATEGORIES
        text = " ".join(
            filter(None, [primary.title, primary.description, primary.recommended_action])
        )
        issues.append(
            {
                "issue_id": identifier,
                "run_id": run.run_id,
                "attempt_id": attempt_id(identifier, attempt),
                "source": "MGMT_REPORT",
                "source_reference": f"{run.report_date}:{primary.source_id}:{primary.source_line}",
                "source_provenance": _provenance(cluster, run, mgmt_repository, redact_ratings),
                "repository": primary.repository,
                "branch": None,
                "environment": "CI" if cluster.environment_signal else None,
                "product": primary.product,
                "component": primary.component,
                "title": primary.title,
                "description": primary.description,
                "category": primary.category,
                "defect_type": "ENVIRONMENT_BLOCKER" if cluster.environment_signal else None,
                "security_scope": security_scope(text, code_change=code_change),
                "files": cluster.paths,
                "related_change": ", ".join(cluster.pr_references) or None,
                "evidence": _evidence(cluster, redact_ratings),
                "reproduction": _reproduction(cluster),
                "state": State.DISCOVERED.value,
                "confidence": confidence(cluster),
                "owner": ", ".join(cluster.subjects) or None,
                "detected_at": run.report_date,
                "remediable": remediability(
                    primary.category, environment_signal=cluster.environment_signal
                ),
                "candidate_repositories": cluster.candidate_repositories,
                "corroborating_only": cluster.corroborating_only,
                "environment_signal": cluster.environment_signal,
                "frequency": primary.frequency,
                "recommended_action": primary.recommended_action,
                "duplicate_of": None,
                "merged_sources": sorted(
                    {f"{f.source_id}:{f.source_line}" for f in cluster.all_findings}
                ),
                "dedupe_signature": cluster.signature,
                "corroboration": cluster.merge_reasons,
            }
        )
    return issues
