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


def _members(sections: list[markdown.Section]) -> list[str]:
    seen: list[str] = []
    for section in sections:
        if (
            section.level == 2
            and section.path[:1]
            and section.path[0].lower() == "individual reviews"
        ):
            name = section.title.split("(")[0].split("—")[0].strip()
            if name and name not in seen:
                seen.append(name)
    return seen


def extract_detail_report(source: SourceFile, text: str) -> list[RawFinding]:
    """Extract findings from the daily engineering detail report."""
    sections = markdown.sections(text)
    findings: list[RawFinding] = []
    findings.extend(_ci_findings(source, text))

    for member in _members(sections):
        product = _member_product(sections, member)
        candidates = _repositories_for_product(product)
        repository = _single_repository(candidates)
        member_scoped = markdown.member_sections(sections, member)

        for section in member_scoped:
            title = section.title.lower()
            if title == "repetitive work identified":
                findings.extend(
                    _repetitive_rows(source, section, member, product, candidates, repository)
                )
            elif title == "opportunities for devin":
                findings.extend(
                    _opportunity_items(source, section, member, product, candidates, repository)
                )
            elif title == "repeat patterns requiring attention":
                findings.extend(
                    _repeat_pattern_rows(source, section, member, product, candidates, repository)
                )
    return findings


def _ci_findings(source: SourceFile, text: str) -> list[RawFinding]:
    """CI blackouts are recorded as environment signals, never as code defects."""
    findings: list[RawFinding] = []
    for number, line in enumerate(text.splitlines(), start=1):
        match = CI_ZERO_SUCCESS.search(line)
        if not match:
            continue
        repository = match.group("repo").strip("`")
        counts = _clean(match.group("counts"))
        cause = CI_BLOCK_CAUSE.search(line)
        findings.append(
            RawFinding(
                finding_key=_key("ci_blackout", repository),
                title=f"CI has no successful runs in {repository}",
                description=(
                    f"The report states {repository} had zero successful CI runs ({counts}). "
                    "Verification evidence (fail-before, pass-after) cannot be produced in this "
                    "repository until CI is restored."
                    + (f" Reported cause: {_clean(cause.group(1))}." if cause else "")
                ),
                category="CI_FAILURE",
                source_id=source.source_id,
                source_report_type=source.report_type.value,
                source_line=number,
                quote=_clean(line),
                repository=repository,
                candidate_repositories=(repository,),
                environment_signal=True,
                detail={
                    "counts": counts,
                    "reported_cause": _clean(cause.group(1)) if cause else None,
                },
            )
        )
    return findings


def _repetitive_rows(
    source: SourceFile,
    section: markdown.Section,
    member: str,
    product: str | None,
    candidates: tuple[str, ...],
    repository: str | None,
) -> list[RawFinding]:
    findings: list[RawFinding] = []
    for table in section.tables():
        for row in table.rows:
            activity = row.get("Activity")
            if not activity:
                continue
            frequency = row.get("Frequency / Pattern", "Frequency")
            approach = row.get("Better Approach")
            combined = " ".join(filter(None, (activity, frequency or "", approach or "")))
            findings.append(
                RawFinding(
                    finding_key=_key("repetitive", activity),
                    title=_clean(activity),
                    description=(
                        f"Repetitive work reported for {member}: {_clean(activity)}. "
                        f"Reported pattern: {_clean(frequency or 'not stated')}. "
                        f"Report's recommended approach: {_clean(approach or 'not stated')}."
                    ),
                    category=_category_for_opportunity(combined),
                    source_id=source.source_id,
                    source_report_type=source.report_type.value,
                    source_line=row.line,
                    quote=_clean(activity),
                    subject=member,
                    product=product,
                    repository=repository,
                    candidate_repositories=candidates,
                    paths=_paths_in(combined),
                    pr_references=_prs_in(combined),
                    frequency=_clean(frequency) if frequency else None,
                    recommended_action=_clean(approach) if approach else None,
                )
            )
    return findings


def _opportunity_items(
    source: SourceFile,
    section: markdown.Section,
    member: str,
    product: str | None,
    candidates: tuple[str, ...],
    repository: str | None,
) -> list[RawFinding]:
    findings: list[RawFinding] = []
    for line_number, item in section.ordered_items():
        text = _clean(item)
        findings.append(
            RawFinding(
                finding_key=_key("opportunity", text[:120]),
                title=text[:160],
                description=f"Delegation opportunity recorded for {member}: {text}",
                category=_category_for_opportunity(text),
                source_id=source.source_id,
                source_report_type=source.report_type.value,
                source_line=line_number,
                quote=text,
                subject=member,
                product=product,
                repository=repository,
                candidate_repositories=candidates,
                paths=_paths_in(item),
                pr_references=_prs_in(item),
                detail={"largest_file_count": _largest_file_count(item)},
            )
        )
    return findings


def _repeat_pattern_rows(
    source: SourceFile,
    section: markdown.Section,
    member: str,
    product: str | None,
    candidates: tuple[str, ...],
    repository: str | None,
) -> list[RawFinding]:
    findings: list[RawFinding] = []
    for table in section.tables():
        for row in table.rows:
            pattern = row.get("Pattern")
            if not pattern:
                continue
            current = row.get("Current Evidence")
            previous = row.get("Previous Evidence")
            action = row.get("Recommended Action")
            combined = " ".join(filter(None, (pattern, current or "", action or "")))
            findings.append(
                RawFinding(
                    finding_key=_key("repeat_pattern", pattern),
                    title=_clean(pattern),
                    description=(
                        f"Recurring pattern flagged for {member}: {_clean(pattern)}. "
                        f"Current evidence: {_clean(current or 'not stated')}. "
                        f"Recommended action: {_clean(action or 'not stated')}."
                    ),
                    category=_category_for_opportunity(combined),
                    source_id=source.source_id,
                    source_report_type=source.report_type.value,
                    source_line=row.line,
                    quote=_clean(f"{pattern} — {current or ''}"),
                    subject=member,
                    product=product,
                    repository=repository,
                    candidate_repositories=candidates,
                    paths=_paths_in(combined),
                    pr_references=_prs_in(combined),
                    prior_evidence=_clean(previous) if previous else None,
                    recommended_action=_clean(action) if action else None,
                    detail={"largest_file_count": _largest_file_count(combined)},
                )
            )
    return findings


def _largest_file_count(text: str) -> int | None:
    counts = [int(value) for value in FILE_COUNT.findall(text)]
    return max(counts) if counts else None


def extract_rating_cards(source: SourceFile, text: str) -> list[RawFinding]:
    """Extract corroborating signal only — ratings never prove a software defect."""
    sections = markdown.sections(text)
    findings: list[RawFinding] = []
    for section in sections:
        for table in section.tables():
            if "Automation" not in table.headers or "Member" not in table.headers:
                continue
            for row in table.rows:
                member = row.get("Member")
                score = row.get("Automation")
                if not member or not score:
                    continue
                numeric = _NUMBER.search(_clean(score))
                # Only a below-midpoint score corroborates an automation finding;
                # a healthy score carries no signal worth carrying downstream.
                if not numeric or int(numeric.group()) > 5:
                    continue
                findings.append(
                    RawFinding(
                        finding_key=_key("card_automation", member),
                        title=f"Low automation-adoption signal for {member}",
                        description=(
                            f"The employee rating card records a below-midpoint automation score "
                            f"for {member}. Corroborating signal only: it supports prioritization "
                            "of automation findings but is not evidence of any software defect."
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
                )
    return findings


def extract(source: SourceFile) -> list[RawFinding]:
    text = source.path.read_text(encoding="utf-8", errors="replace")
    if source.report_type is ReportType.DAILY_ENGINEERING_DETAIL:
        return extract_detail_report(source, text)
    if source.report_type is ReportType.EMPLOYEE_RATING_CARDS:
        return extract_rating_cards(source, text)
    return []
