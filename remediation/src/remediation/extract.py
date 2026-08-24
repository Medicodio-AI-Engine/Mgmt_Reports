"""Evidence extraction from the management reports.

Produces ``RawFinding`` objects that quote the report line they came from. This
layer never decides remediability or priority; it only records what the report
states, together with the provenance needed to justify any later action.

Two rules from the specification are enforced here:

* Employee rating cards are corroborating signal only. Card-derived findings are
  emitted as ``PROCESS_PRACTICE`` support records that cannot themselves justify
  a code change.
* Nothing is inferred beyond the text. Unknown repository, component, or path
  stay ``None`` rather than being guessed.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from . import markdown
from .discovery import ReportType, SourceFile

PRODUCT_REPOSITORIES: dict[str, tuple[str, ...]] = {
    "global codio": ("globalcodio-monorepo",),
    "medicodio (integration)": ("medicodio-nextgen-integration",),
    "medicodio (app)": ("medicodio-nextgen-app-nodejs", "medicodio-nextgen-app-react"),
    "medicodio": (),
}

PR_REFERENCE = re.compile(r"#(\d{2,6})")
_NUMBER = re.compile(r"\d+")
BACKTICKED = re.compile(r"`([^`]+)`")
CI_ZERO_SUCCESS = re.compile(
    r"zero successful ci runs in `?(?P<repo>[\w./-]+)`?[^.]*?\((?P<counts>[^)]*)\)",
    re.IGNORECASE,
)
CI_BLOCK_CAUSE = re.compile(r"(billing|spending[- ]limit|quota|runner)", re.IGNORECASE)
FILE_COUNT = re.compile(r"(\d{2,4})\s*files?", re.IGNORECASE)
PATHISH = re.compile(r"^[\w./*-]+/[\w./*-]+$")

TEST_WORDS = (
    "regression test",
    "test suite",
    "test matrix",
    "regression suite",
    "tests for",
    "harness",
)
SECURITY_PATTERN = re.compile(
    r"tenant isolation|cross-tenant|row[- ]level security|\brls\b|\bidor\b|access[- ]control",
    re.IGNORECASE,
)
MIGRATION_WORDS = ("split", "stack", "carve", "sync", "promotion", "fast-forward", "merge queue")
AUTOMATION_WORDS = ("automate", "generate", "emit", "auto-generate", "script", "tooling")


@dataclass
class RawFinding:
    """One report statement, with provenance, before normalization."""

    finding_key: str
    title: str
    description: str
    category: str
    source_id: str
    source_report_type: str
    source_line: int
    quote: str
    subject: str | None = None
    product: str | None = None
    repository: str | None = None
    candidate_repositories: tuple[str, ...] = ()
    component: str | None = None
    paths: tuple[str, ...] = ()
    pr_references: tuple[str, ...] = ()
    frequency: str | None = None
    recommended_action: str | None = None
    prior_evidence: str | None = None
    corroborating_only: bool = False
    environment_signal: bool = False
    detail: dict[str, Any] = field(default_factory=dict)

    def evidence(self) -> list[dict[str, Any]]:
        return [
            {
                "type": "REPORT_STATEMENT",
                "source_id": self.source_id,
                "report_type": self.source_report_type,
                "line": self.source_line,
                "quote": self.quote,
            }
        ]


def _repositories_for_product(product: str | None) -> tuple[str, ...]:
    if not product:
        return ()
    return PRODUCT_REPOSITORIES.get(product.strip().lower(), ())


def _single_repository(candidates: tuple[str, ...]) -> str | None:
    return candidates[0] if len(candidates) == 1 else None


def _paths_in(text: str) -> tuple[str, ...]:
    return tuple(
        sorted({token for token in BACKTICKED.findall(text) if PATHISH.match(token.strip())})
    )


def _prs_in(text: str) -> tuple[str, ...]:
    return tuple(sorted({f"#{number}" for number in PR_REFERENCE.findall(text)}))


def _category_for_opportunity(text: str) -> str:
    lowered = text.lower()
    if SECURITY_PATTERN.search(text):
        return "SECURITY_TENANCY"
    if any(word in lowered for word in TEST_WORDS):
        return "MISSING_TEST"
    if any(word in lowered for word in MIGRATION_WORDS):
        return "MECHANICAL_MIGRATION"
    if any(word in lowered for word in AUTOMATION_WORDS):
        return "AUTOMATION_OPPORTUNITY"
    return "PROCESS_PRACTICE"


def _clean(text: str) -> str:
    collapsed = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"\*\*|\*|__", "", collapsed)


def _key(*parts: str) -> str:
    joined = "|".join(part.strip().lower() for part in parts if part)
    return re.sub(r"[^a-z0-9|]+", "_", joined)[:220]


def _member_product(sections: list[markdown.Section], member: str) -> str | None:
    for section in markdown.member_sections(sections, member):
        match = re.search(r"\*\*Product:\*\*\s*(.+)", section.text)
        if match:
            return _clean(match.group(1))
    return None


def _is_member_heading(section: markdown.Section) -> bool:
    if section.level != 2 or not section.path[:1]:
        return False
    return section.path[0].lower() == "individual reviews"


def _member_name(section: markdown.Section) -> str:
    return section.title.split("(")[0].split("—")[0].strip()


def _members(sections: list[markdown.Section]) -> list[str]:
    """Reviewed team members, in report order, without duplicates."""
    seen: list[str] = []
    for section in sections:
        name = _member_name(section) if _is_member_heading(section) else ""
        if name and name not in seen:
            seen.append(name)
    return seen


SectionExtractor = Callable[[SourceFile, "markdown.Section", "MemberScope"], list[RawFinding]]


@dataclass(frozen=True)
class MemberScope:
    """Which member a finding belongs to, and the repository it may target."""

    member: str
    product: str | None
    candidates: tuple[str, ...]
    repository: str | None


def _member_scope(sections: list[markdown.Section], member: str) -> MemberScope:
    product = _member_product(sections, member)
    candidates = _repositories_for_product(product)
    return MemberScope(
        member=member,
        product=product,
        candidates=candidates,
        repository=_single_repository(candidates),
    )


def _ci_description(repository: str, counts: str, cause: re.Match[str] | None) -> str:
    reported = f" Reported cause: {_clean(cause.group(1))}." if cause else ""
    return (
        f"The report states {repository} had zero successful CI runs ({counts}). "
        "Verification evidence (fail-before, pass-after) cannot be produced in this "
        f"repository until CI is restored.{reported}"
    )


def _ci_finding(source: SourceFile, number: int, line: str, match: re.Match[str]) -> RawFinding:
    repository = match.group("repo").strip("`")
    counts = _clean(match.group("counts"))
    cause = CI_BLOCK_CAUSE.search(line)
    return RawFinding(
        finding_key=_key("ci_blackout", repository),
        title=f"CI has no successful runs in {repository}",
        description=_ci_description(repository, counts, cause),
        category="CI_FAILURE",
        source_id=source.source_id,
        source_report_type=source.report_type.value,
        source_line=number,
        quote=_clean(line),
        repository=repository,
        candidate_repositories=(repository,),
        environment_signal=True,
        detail={"counts": counts, "reported_cause": _clean(cause.group(1)) if cause else None},
    )


def _ci_findings(source: SourceFile, text: str) -> list[RawFinding]:
    """CI blackouts are recorded as environment signals, never as code defects."""
    numbered = enumerate(text.splitlines(), start=1)
    matched = [(number, line, CI_ZERO_SUCCESS.search(line)) for number, line in numbered]
    return [_ci_finding(source, number, line, match) for number, line, match in matched if match]


def _rows(section: markdown.Section) -> list[markdown.Row]:
    return [row for table in section.tables() for row in table.rows]


def _repetitive_finding(
    source: SourceFile, row: markdown.Row, scope: MemberScope
) -> RawFinding | None:
    activity = row.get("Activity")
    if not activity:
        return None
    frequency = row.get("Frequency / Pattern", "Frequency")
    approach = row.get("Better Approach")
    combined = " ".join(filter(None, (activity, frequency or "", approach or "")))
    return RawFinding(
        finding_key=_key("repetitive", activity),
        title=_clean(activity),
        description=(
            f"Repetitive work reported for {scope.member}: {_clean(activity)}. "
            f"Reported pattern: {_clean(frequency or 'not stated')}. "
            f"Report's recommended approach: {_clean(approach or 'not stated')}."
        ),
        category=_category_for_opportunity(combined),
        source_id=source.source_id,
        source_report_type=source.report_type.value,
        source_line=row.line,
        quote=_clean(activity),
        subject=scope.member,
        product=scope.product,
        repository=scope.repository,
        candidate_repositories=scope.candidates,
        paths=_paths_in(combined),
        pr_references=_prs_in(combined),
        frequency=_clean(frequency) if frequency else None,
        recommended_action=_clean(approach) if approach else None,
    )


def _repetitive_rows(
    source: SourceFile, section: markdown.Section, scope: MemberScope
) -> list[RawFinding]:
    found = [_repetitive_finding(source, row, scope) for row in _rows(section)]
    return [finding for finding in found if finding is not None]


def _opportunity_finding(
    source: SourceFile, line_number: int, item: str, scope: MemberScope
) -> RawFinding:
    text = _clean(item)
    return RawFinding(
        finding_key=_key("opportunity", text[:120]),
        title=text[:160],
        description=f"Delegation opportunity recorded for {scope.member}: {text}",
        category=_category_for_opportunity(text),
        source_id=source.source_id,
        source_report_type=source.report_type.value,
        source_line=line_number,
        quote=text,
        subject=scope.member,
        product=scope.product,
        repository=scope.repository,
        candidate_repositories=scope.candidates,
        paths=_paths_in(item),
        pr_references=_prs_in(item),
        detail={"largest_file_count": _largest_file_count(item)},
    )


def _opportunity_items(
    source: SourceFile, section: markdown.Section, scope: MemberScope
) -> list[RawFinding]:
    return [
        _opportunity_finding(source, line_number, item, scope)
        for line_number, item in section.ordered_items()
    ]


def _repeat_pattern_finding(
    source: SourceFile, row: markdown.Row, scope: MemberScope
) -> RawFinding | None:
    pattern = row.get("Pattern")
    if not pattern:
        return None
    current = row.get("Current Evidence")
    action = row.get("Recommended Action")
    previous = row.get("Previous Evidence")
    combined = " ".join(filter(None, (pattern, current or "", action or "")))
    return RawFinding(
        finding_key=_key("repeat_pattern", pattern),
        title=_clean(pattern),
        description=(
            f"Recurring pattern flagged for {scope.member}: {_clean(pattern)}. "
            f"Current evidence: {_clean(current or 'not stated')}. "
            f"Recommended action: {_clean(action or 'not stated')}."
        ),
        category=_category_for_opportunity(combined),
        source_id=source.source_id,
        source_report_type=source.report_type.value,
        source_line=row.line,
        quote=_clean(f"{pattern} — {current or ''}"),
        subject=scope.member,
        product=scope.product,
        repository=scope.repository,
        candidate_repositories=scope.candidates,
        paths=_paths_in(combined),
        pr_references=_prs_in(combined),
        prior_evidence=_clean(previous) if previous else None,
        recommended_action=_clean(action) if action else None,
        detail={"largest_file_count": _largest_file_count(combined)},
    )


def _repeat_pattern_rows(
    source: SourceFile, section: markdown.Section, scope: MemberScope
) -> list[RawFinding]:
    found = [_repeat_pattern_finding(source, row, scope) for row in _rows(section)]
    return [finding for finding in found if finding is not None]


SECTION_EXTRACTORS: dict[str, SectionExtractor] = {
    "repetitive work identified": _repetitive_rows,
    "opportunities for devin": _opportunity_items,
    "repeat patterns requiring attention": _repeat_pattern_rows,
}


def _section_findings(
    source: SourceFile, section: markdown.Section, scope: MemberScope
) -> list[RawFinding]:
    """Findings from one recognized member subsection."""
    extractor = SECTION_EXTRACTORS.get(section.title.lower())
    return extractor(source, section, scope) if extractor else []


def _member_findings(
    source: SourceFile, sections: list[markdown.Section], member: str
) -> list[RawFinding]:
    scope = _member_scope(sections, member)
    return [
        finding
        for section in markdown.member_sections(sections, member)
        for finding in _section_findings(source, section, scope)
    ]


def extract_detail_report(source: SourceFile, text: str) -> list[RawFinding]:
    """Extract findings from the daily engineering detail report."""
    sections = markdown.sections(text)
    findings = _ci_findings(source, text)
    for member in _members(sections):
        findings.extend(_member_findings(source, sections, member))
    return findings


def _largest_file_count(text: str) -> int | None:
    counts = [int(value) for value in FILE_COUNT.findall(text)]
    return max(counts) if counts else None


def _is_rating_table(table: markdown.Table) -> bool:
    return "Automation" in table.headers and "Member" in table.headers


def _low_automation(score: str) -> bool:
    """Only a below-midpoint score corroborates an automation finding."""
    numeric = _NUMBER.search(_clean(score))
    return bool(numeric) and int(numeric.group()) <= 5


def _card_finding(source: SourceFile, row: markdown.Row) -> RawFinding | None:
    member = row.get("Member")
    score = row.get("Automation")
    if not member or not score or not _low_automation(score):
        return None
    return RawFinding(
        finding_key=_key("card_automation", member),
        title=f"Low automation-adoption signal for {member}",
        description=(
            "The employee rating card records a below-midpoint automation score for "
            f"{member}. Corroborating signal only: it supports prioritization of automation "
            "findings but is not evidence of any software defect."
        ),
        category="PROCESS_PRACTICE",
        source_id=source.source_id,
        source_report_type=source.report_type.value,
        source_line=row.line,
        quote=_clean(" | ".join(row.cells.values())),
        subject=_clean(member),
        product=_clean(row.get("Product") or "") or None,
        corroborating_only=True,
        detail={"automation_score": _clean(score)},
    )


def _rating_rows(sections: list[markdown.Section]) -> list[markdown.Row]:
    return [
        row
        for section in sections
        for table in section.tables()
        if _is_rating_table(table)
        for row in table.rows
    ]


def extract_rating_cards(source: SourceFile, text: str) -> list[RawFinding]:
    """Extract corroborating signal only — ratings never prove a software defect."""
    rows = _rating_rows(markdown.sections(text))
    found = [_card_finding(source, row) for row in rows]
    return [finding for finding in found if finding is not None]


def extract(source: SourceFile) -> list[RawFinding]:
    text = source.path.read_text(encoding="utf-8", errors="replace")
    if source.report_type is ReportType.DAILY_ENGINEERING_DETAIL:
        return extract_detail_report(source, text)
    if source.report_type is ReportType.EMPLOYEE_RATING_CARDS:
        return extract_rating_cards(source, text)
    return []
