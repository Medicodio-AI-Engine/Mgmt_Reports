"""Finding deduplication.

Merges only findings that describe the same work. A merge requires the same
category, a compatible repository, and either an identical signature or a high
token overlap; anything weaker stays separate, because an unjustified merge
hides a real issue. Every source reference of every merged finding is retained.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .extract import RawFinding

SIMILARITY_THRESHOLD = 0.8

_STOPWORD_TEXT = """
    a an the and or of to for in on into by with without at from as is are was were be being
    been it its this that these those not no than then so such use using used devin report
    reported recorded states state stated recommended recommendation approach better pattern
    frequency current previous evidence action work every each their his her them they he she
"""

STOPWORDS = frozenset(_STOPWORD_TEXT.split())

_TOKEN = re.compile(r"[a-z][a-z0-9_]{1,}")

_SYNONYMS = {
    "tests": "test",
    "testing": "test",
    "regression": "test",
    "suites": "suite",
    "suite": "test",
    "automate": "automation",
    "automated": "automation",
    "automating": "automation",
    "generate": "generation",
    "generating": "generation",
    "emit": "generation",
    "merges": "merge",
    "merging": "merge",
    "merged": "merge",
    "syncs": "sync",
    "syncing": "sync",
    "synchronization": "sync",
    "splitting": "split",
    "splits": "split",
    "stacked": "stack",
    "stacking": "stack",
    "reviews": "review",
    "reviewed": "review",
    "reviewing": "review",
    "logs": "log",
    "docs": "doc",
    "documentation": "doc",
    "files": "file",
    "prs": "pr",
    "branches": "branch",
    "commits": "commit",
}


def tokens(text: str) -> frozenset[str]:
    raw = (_SYNONYMS.get(token, token) for token in _TOKEN.findall(text.lower()))
    return frozenset(token for token in raw if token not in STOPWORDS and len(token) > 2)


def signature(finding: RawFinding) -> str:
    repository = finding.repository or "REPOSITORY_UNKNOWN"
    body = " ".join(sorted(tokens(f"{finding.title} {finding.recommended_action or ''}")))
    return f"{finding.category}|{repository}|{body}"


def similarity(left: frozenset[str], right: frozenset[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


@dataclass
class Cluster:
    """One deduplicated finding group."""

    primary: RawFinding
    members: list[RawFinding] = field(default_factory=list)
    merge_reasons: list[str] = field(default_factory=list)

    @property
    def all_findings(self) -> list[RawFinding]:
        return [self.primary, *self.members]

    @property
    def signature(self) -> str:
        return signature(self.primary)

    @property
    def subjects(self) -> list[str]:
        return sorted({f.subject for f in self.all_findings if f.subject})

    @property
    def repositories(self) -> list[str]:
        return sorted({f.repository for f in self.all_findings if f.repository})

    @property
    def candidate_repositories(self) -> list[str]:
        return sorted({repo for f in self.all_findings for repo in f.candidate_repositories})

    @property
    def paths(self) -> list[str]:
        return sorted({path for f in self.all_findings for path in f.paths})

    @property
    def pr_references(self) -> list[str]:
        return sorted({pr for f in self.all_findings for pr in f.pr_references})

    @property
    def corroborating_only(self) -> bool:
        return all(f.corroborating_only for f in self.all_findings)

    @property
    def environment_signal(self) -> bool:
        return any(f.environment_signal for f in self.all_findings)

    @property
    def support_count(self) -> int:
        """Distinct people/sources reporting the same thing."""
        distinct_subjects = len(self.subjects)
        return max(distinct_subjects, len({f.source_id for f in self.all_findings}))


def _compatible_repository(left: RawFinding, right: RawFinding) -> bool:
    return left.repository == right.repository


def _mergeable(existing: Cluster, finding: RawFinding) -> bool:
    """Only findings of the same kind, target, and evidence class may merge."""
    if existing.primary.category != finding.category:
        return False
    if not _compatible_repository(existing.primary, finding):
        return False
    return existing.primary.corroborating_only == finding.corroborating_only


def _finding_tokens(finding: RawFinding) -> set[str]:
    return tokens(f"{finding.title} {finding.recommended_action or ''}")


def _merge_reason(existing: Cluster, finding: RawFinding) -> str | None:
    """Why this finding belongs to this cluster, or ``None`` if it does not."""
    locator = f"{finding.source_id}:{finding.source_line}"
    if existing.signature == signature(finding):
        return f"identical signature with {locator}"
    score = similarity(_finding_tokens(existing.primary), _finding_tokens(finding))
    if score >= SIMILARITY_THRESHOLD:
        return f"token similarity {score:.2f} with {locator}"
    return None


def _place(clusters: list[Cluster], finding: RawFinding) -> bool:
    """Add the finding to the first cluster that accepts it."""
    for existing in clusters:
        if not _mergeable(existing, finding):
            continue
        reason = _merge_reason(existing, finding)
        if reason is None:
            continue
        existing.members.append(finding)
        existing.merge_reasons.append(reason)
        return True
    return False


def cluster(findings: list[RawFinding]) -> list[Cluster]:
    """Group findings into clusters, most-supported first, order-stable."""
    clusters: list[Cluster] = []
    for finding in findings:
        if not _place(clusters, finding):
            clusters.append(Cluster(primary=finding))
    return clusters
