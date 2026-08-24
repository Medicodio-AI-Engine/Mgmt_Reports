"""Issue normalization.

Turns deduplicated report findings into schema-valid normalized issues. Unknown
values stay explicitly ``null``/``UNKNOWN`` — the normalizer never invents a
repository, path, branch, environment, owner, or security classification.

The issue record is assembled from small single-purpose builders (identity,
target, classification, evidence, dedupe) so a wrong field is traced to one
function.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Any

from . import scope as scope_module
from . import taxonomy
from .dedupe import Cluster
from .discovery import RunContext
from .extract import RawFinding
from .naming import attempt_id, issue_id
from .scope import RepositoryScope
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

RATING_REDACTION = (
    "[rating detail redacted; see the employee rating card at this locator in Mgmt_Reports]"
)

_NUMBER = re.compile(r"\d+")


def security_scope(text: str, *, code_change: bool) -> str:
    lowered = text.lower()
    for pattern, marker in SECURITY_MARKERS:
        if re.search(pattern, lowered):
            return marker
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


def _support_bonus(cluster: Cluster) -> float:
    """Corroborating support and concrete references raise confidence."""
    bonus = 0.15 if cluster.support_count >= 2 else 0.0
    bonus += 0.1 if cluster.pr_references else 0.0
    return bonus + (0.1 if cluster.paths else 0.0)


def _detail_bonus(cluster: Cluster) -> float:
    """A quantified frequency or prior evidence raises confidence."""
    frequency = cluster.primary.frequency
    bonus = 0.05 if frequency and _NUMBER.search(frequency) else 0.0
    return bonus + (0.05 if cluster.primary.prior_evidence else 0.0)


def confidence(cluster: Cluster) -> float:
    if cluster.corroborating_only:
        return 0.3
    return round(min(0.5 + _support_bonus(cluster) + _detail_bonus(cluster), 0.9), 2)


def _quote(finding: RawFinding, redact_ratings: bool) -> str:
    """Rating-card rows carry individual scores, so they are quoted by locator only."""
    if redact_ratings and finding.source_report_type == "EMPLOYEE_RATING_CARDS":
        return RATING_REDACTION
    return finding.quote


def _locator(finding: RawFinding) -> str:
    return f"{finding.source_id}:{finding.source_line}"


def _observation(finding: RawFinding, redact_ratings: bool) -> dict[str, str]:
    return {
        "kind": "REPORT_OBSERVATION",
        "locator": _locator(finding),
        "excerpt": _quote(finding, redact_ratings),
    }


def _extra_evidence(finding: RawFinding) -> list[dict[str, str]]:
    """The report's own recommendation and any previously reported evidence."""
    items: list[dict[str, str]] = []
    if finding.recommended_action:
        items.append(
            {
                "kind": "RECOMMENDATION",
                "locator": _locator(finding),
                "excerpt": finding.recommended_action,
            }
        )
    if finding.prior_evidence:
        items.append(
            {
                "kind": "REPORT_OBSERVATION",
                "locator": _locator(finding),
                "excerpt": f"previous evidence: {finding.prior_evidence}",
            }
        )
    return items


def _evidence(cluster: Cluster, redact_ratings: bool) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for finding in cluster.all_findings:
        items.append(_observation(finding, redact_ratings))
        items += _extra_evidence(finding)
    return items


def _source_path(run: RunContext, finding: RawFinding) -> str:
    source = next((s for s in run.sources if s.source_id == finding.source_id), None)
    if source is None:
        return run.source_directory
    return f"{run.source_directory}/{source.path.name}"


def _provenance_entry(
    finding: RawFinding, run: RunContext, repository: str, redact_ratings: bool
) -> dict[str, Any]:
    return {
        "source_id": finding.source_id,
        "report_date": run.report_date,
        "report_type": finding.source_report_type,
        "repository": repository,
        "repository_path": _source_path(run, finding),
        "section": finding.finding_key.split("|", 1)[0],
        "member": finding.subject,
        "finding_reference": f"line {finding.source_line}",
        "evidence_excerpt_or_locator": _quote(finding, redact_ratings),
    }


def _provenance(
    cluster: Cluster, run: RunContext, repository: str, redact_ratings: bool
) -> list[dict[str, Any]]:
    return [
        _provenance_entry(finding, run, repository, redact_ratings)
        for finding in cluster.all_findings
    ]


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


def _finding_text(primary: RawFinding) -> str:
    parts = [primary.title, primary.description, primary.recommended_action]
    return " ".join(filter(None, parts))


def resolve_repository(primary: RawFinding, text: str, repo_scope: RepositoryScope) -> str | None:
    """The reported repository, or a single unambiguous name found in the text."""
    if primary.repository:
        return primary.repository
    named = scope_module.mentions(repo_scope, text)
    return named[0] if len(named) == 1 else None


def _identity(cluster: Cluster, run: RunContext, identifier: str, attempt: int) -> dict[str, Any]:
    primary = cluster.primary
    return {
        "issue_id": identifier,
        "run_id": run.run_id,
        "attempt_id": attempt_id(identifier, attempt),
        "source": "MGMT_REPORT",
        "source_reference": f"{run.report_date}:{primary.source_id}:{primary.source_line}",
        "state": State.DISCOVERED.value,
        "detected_at": run.report_date,
    }


def _target(
    cluster: Cluster, repository: str | None, repo_scope: RepositoryScope
) -> dict[str, Any]:
    primary = cluster.primary
    return {
        "repository": repository,
        "branch": None,
        "environment": "CI" if cluster.environment_signal else None,
        "product": primary.product,
        "component": primary.component,
        "files": cluster.paths,
        "candidate_repositories": cluster.candidate_repositories,
        "analysis_scope": scope_module.classify(repo_scope, repository),
        "scope_reason": scope_module.reason(repo_scope, repository),
    }


def _classification(cluster: Cluster, text: str) -> dict[str, Any]:
    primary = cluster.primary
    code_change = primary.category in CODE_CATEGORIES
    return {
        "title": primary.title,
        "description": primary.description,
        "category": primary.category,
        "defect_type": "ENVIRONMENT_BLOCKER" if cluster.environment_signal else None,
        "security_scope": security_scope(text, code_change=code_change),
        "remediable": remediability(
            primary.category, environment_signal=cluster.environment_signal
        ),
        "corroborating_only": cluster.corroborating_only,
        "environment_signal": cluster.environment_signal,
        **taxonomy.evaluate(primary.category, text).as_dict(),
    }


def _support(
    cluster: Cluster, run: RunContext, mgmt_repository: str, redact: bool
) -> dict[str, Any]:
    primary = cluster.primary
    return {
        "source_provenance": _provenance(cluster, run, mgmt_repository, redact),
        "evidence": _evidence(cluster, redact),
        "reproduction": _reproduction(cluster),
        "confidence": confidence(cluster),
        "owner": ", ".join(cluster.subjects) or None,
        "frequency": primary.frequency,
        "recommended_action": primary.recommended_action,
        "related_change": ", ".join(cluster.pr_references) or None,
    }


def _dedupe_fields(cluster: Cluster) -> dict[str, Any]:
    return {
        "duplicate_of": None,
        "merged_sources": sorted({_locator(f) for f in cluster.all_findings}),
        "dedupe_signature": cluster.signature,
        "corroboration": cluster.merge_reasons,
    }


def build_issue(
    cluster: Cluster,
    run: RunContext,
    mgmt_repository: str,
    *,
    identifier: str,
    attempt: int,
    redact_ratings: bool,
    repo_scope: RepositoryScope,
) -> dict[str, Any]:
    """Assemble one normalized issue from its builders."""
    text = _finding_text(cluster.primary)
    repository = resolve_repository(cluster.primary, text, repo_scope)
    return {
        **_identity(cluster, run, identifier, attempt),
        **_target(cluster, repository, repo_scope),
        **_classification(cluster, text),
        **_support(cluster, run, mgmt_repository, redact_ratings),
        **_dedupe_fields(cluster),
    }


def normalize(
    clusters: list[Cluster],
    run: RunContext,
    mgmt_repository: str,
    *,
    redact_ratings: bool = True,
    allocate_id: Callable[[str], str] | None = None,
    attempt_number: Callable[[str], int] | None = None,
    repo_scope: RepositoryScope | None = None,
) -> list[dict[str, Any]]:
    """Emit schema-valid normalized issues with stable identities.

    ``allocate_id`` maps a dedupe signature to an issue id and defaults to
    positional allocation; pass an :class:`~remediation.ids.IssueRegistry` resolver
    so an id keeps its meaning across runs.
    """
    active_scope = repo_scope or RepositoryScope()
    issues: list[dict[str, Any]] = []
    for index, cluster in enumerate(clusters, start=1):
        identifier = allocate_id(cluster.signature) if allocate_id is not None else issue_id(index)
        attempt = attempt_number(identifier) if attempt_number is not None else 1
        issues.append(
            build_issue(
                cluster,
                run,
                mgmt_repository,
                identifier=identifier,
                attempt=attempt,
                redact_ratings=redact_ratings,
                repo_scope=active_scope,
            )
        )
    return issues
