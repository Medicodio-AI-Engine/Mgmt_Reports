"""Pre-stage source discovery and run assembly.

Finds the management-report artifacts that belong to one report date, classifies
them by evidence, verifies filename date against the date stated inside the
document, and emits the source manifest that ``00_INTAKE`` consumes.

Filenames are never hard-coded: this repository's committed convention is
``mgmt-activity-report-YYYY-MM-DD.md`` / ``employee-rating-cards-YYYY-MM-DD.md``,
but classification relies on filename semantics plus report headers so a renamed
or reformatted report is still recognized.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

from . import dates
from .config import Config
from .naming import Stage

READABLE_SUFFIXES = {".md", ".markdown", ".txt", ".json"}


class ReportType(str, Enum):
    DAILY_ENGINEERING_DETAIL = "DAILY_ENGINEERING_DETAIL"
    EMPLOYEE_RATING_CARDS = "EMPLOYEE_RATING_CARDS"
    UNKNOWN_REPORT = "UNKNOWN_REPORT"


class Completeness(str, Enum):
    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"
    AMBIGUOUS = "AMBIGUOUS"
    DATE_MISMATCH = "DATE_MISMATCH"
    DUPLICATE_SOURCE_TYPE = "DUPLICATE_SOURCE_TYPE"
    NO_REPORTS_FOUND = "NO_REPORTS_FOUND"


class DateResolution(str, Enum):
    EXPLICIT_ARGUMENT = "EXPLICIT_ARGUMENT"
    TRIGGERING_EVENT = "TRIGGERING_EVENT"
    SELECTED_REPORT_CONTENT = "SELECTED_REPORT_CONTENT"
    LATEST_COMPLETE_GROUP = "LATEST_COMPLETE_GROUP"


_DETAIL_INDICATORS = (
    "daily team summary",
    "individual reviews",
    "activities completed",
    "devin usage",
    "repetitive work identified",
    "opportunities for devin",
    "recommended next improvement",
)

_CARDS_INDICATORS = (
    "employee rating cards",
    "summary grid",
    "delivery & follow-through",
    "engineering rigor",
    "observable devin leverage",
    "automation of repetitive work",
)

_FILENAME_HINTS = {
    ReportType.DAILY_ENGINEERING_DETAIL: (
        "mgmt_activity_report",
        "mgmt-activity-report",
        "activity_report",
        "engineering_detail",
    ),
    ReportType.EMPLOYEE_RATING_CARDS: (
        "employee_rating_cards",
        "employee-rating-cards",
        "rating_cards",
    ),
}


class DiscoveryError(RuntimeError):
    """Raised when discovery cannot produce a usable run context."""


@dataclass
class SourceFile:
    source_id: str
    path: Path
    repository_path: str
    report_type: ReportType
    filename_date: str | None
    content_review_date: str | None
    normalized_date: str | None
    date_verified: bool
    classification_evidence: list[str] = field(default_factory=list)
    excluded: bool = False
    exclusion_reason: str | None = None

    def as_manifest_entry(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "report_type": self.report_type.value,
            "filename": self.path.name,
            "repository_path": self.repository_path,
            "file_format": self.path.suffix.lstrip(".").upper() or "UNKNOWN",
            "filename_date": self.filename_date,
            "content_review_date": self.content_review_date,
            "normalized_date": self.normalized_date,
            "date_verified": self.date_verified,
            "classification_evidence": self.classification_evidence,
            "excluded": self.excluded,
            "exclusion_reason": self.exclusion_reason,
        }


@dataclass
class RunContext:
    """The assembled run: one report date and its verified sources."""

    run_id: str
    report_date: str
    resolution_method: DateResolution
    requested_report_date: str | None
    completeness: Completeness
    sources: list[SourceFile]
    all_discovered: list[SourceFile]
    warnings: list[str]
    run_flags: list[str]
    human_action_required: str | None
    source_directory: str

    @property
    def required_sources_present(self) -> bool:
        return self.completeness is Completeness.COMPLETE

    @property
    def processable(self) -> bool:
        """Whether intake may proceed (possibly with reduced confidence)."""
        return self.completeness in {Completeness.COMPLETE, Completeness.PARTIAL}

    def source(self, report_type: ReportType) -> SourceFile | None:
        for candidate in self.sources:
            if candidate.report_type is report_type and not candidate.excluded:
                return candidate
        return None

    def missing_sources(self) -> list[str]:
        return [
            report_type.value
            for report_type in (
                ReportType.DAILY_ENGINEERING_DETAIL,
                ReportType.EMPLOYEE_RATING_CARDS,
            )
            if self.source(report_type) is None
        ]

    def manifest(self, config: Config) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "report_date": self.report_date,
            "repository": config.mgmt_reports_repository,
            "directory": config.mgmt_reports_directory,
            "branch": config.mgmt_reports_branch,
            "requested_report_date": self.requested_report_date,
            "resolved_report_date": self.report_date,
            "date_resolution_method": self.resolution_method.value,
            "source_directory": self.source_directory,
            "files_discovered": [s.path.name for s in self.all_discovered],
            "source_files": [s.as_manifest_entry() for s in self.sources],
            "completeness": self.completeness.value,
            "required_sources_present": self.required_sources_present,
            "missing_sources": self.missing_sources(),
            "run_flags": self.run_flags,
            "warnings": self.warnings,
            "human_action_required": self.human_action_required,
            "next_state": Stage.INTAKE.value if self.processable else "BLOCKED",
            "next_expected_input_file": None,
        }


def _filename_guess(path: Path) -> ReportType | None:
    """The report type the filename claims, if any."""
    stem = path.stem.lower().replace("-", "_")
    for report_type, hints in _FILENAME_HINTS.items():
        if any(hint.replace("-", "_") in stem for hint in hints):
            return report_type
    return None


def _content_guess(text: str) -> tuple[ReportType | None, list[str]]:
    """The report type the content evidence supports, and that evidence."""
    lowered = text.lower()
    detail = [i for i in _DETAIL_INDICATORS if i in lowered]
    cards = [i for i in _CARDS_INDICATORS if i in lowered]
    if len(cards) >= 2 and len(cards) > len(detail):
        return ReportType.EMPLOYEE_RATING_CARDS, sorted(cards)[:4]
    if len(detail) >= 2:
        return ReportType.DAILY_ENGINEERING_DETAIL, sorted(detail)[:4]
    return None, []


def _classification_evidence(
    named: ReportType | None, guessed: ReportType | None, indicators: list[str]
) -> list[str]:
    evidence = [f"filename matches {named.value} naming"] if named else []
    if indicators:
        evidence.append("content indicators: " + ", ".join(indicators))
    if named and guessed and named is not guessed:
        evidence.append(f"filename suggested {named.value}, content evidence chose {guessed.value}")
    return evidence


def classify(path: Path, text: str) -> tuple[ReportType, list[str]]:
    """Classify a report by filename semantics and header evidence.

    Content evidence wins over the filename, because a report can be renamed but its
    body is what the pipeline actually reads.
    """
    named = _filename_guess(path)
    guessed, indicators = _content_guess(text)
    resolved = guessed or named or ReportType.UNKNOWN_REPORT
    return resolved, _classification_evidence(named, guessed, indicators)


def _unreadable_source(path: Path, source_id: str) -> SourceFile:
    """A file the pipeline cannot read is preserved, excluded, and explained."""
    return SourceFile(
        source_id=source_id,
        path=path,
        repository_path=path.name,
        report_type=ReportType.UNKNOWN_REPORT,
        filename_date=dates.find_date(path.name),
        content_review_date=None,
        normalized_date=dates.find_date(path.name),
        date_verified=False,
        classification_evidence=[f"unreadable format {path.suffix or 'none'}"],
        excluded=True,
        exclusion_reason="UNSUPPORTED_FORMAT",
    )


def _readable_source(path: Path, source_id: str) -> SourceFile:
    """Classify one readable report and verify its date against its content."""
    text = path.read_text(encoding="utf-8", errors="replace")
    report_type, evidence = classify(path, text)
    filename_date = dates.find_date(path.name)
    content_date = dates.find_content_review_date(text)
    mismatch = bool(filename_date and content_date and filename_date != content_date)
    return SourceFile(
        source_id=source_id,
        path=path,
        repository_path=path.name,
        report_type=report_type,
        filename_date=filename_date,
        content_review_date=content_date,
        normalized_date=filename_date or content_date,
        date_verified=bool(filename_date and content_date and not mismatch),
        classification_evidence=evidence,
        excluded=mismatch,
        exclusion_reason="DATE_MISMATCH" if mismatch else None,
    )


def _read_source(path: Path, source_id: str) -> SourceFile:
    if path.suffix.lower() not in READABLE_SUFFIXES:
        return _unreadable_source(path, source_id)
    return _readable_source(path, source_id)


def scan(directory: Path) -> list[SourceFile]:
    """Read every candidate artifact in ``directory`` and classify it."""
    if not directory.is_dir():
        raise DiscoveryError(f"report directory not found: {directory}")
    files = sorted(p for p in directory.iterdir() if p.is_file())
    return [_read_source(path, f"SOURCE_{index:03d}") for index, path in enumerate(files, start=1)]


def group_by_date(sources: list[SourceFile]) -> dict[str, list[SourceFile]]:
    grouped: dict[str, list[SourceFile]] = {}
    for source in sources:
        if source.normalized_date is None:
            continue
        grouped.setdefault(source.normalized_date, []).append(source)
    return grouped


REQUIRED_TYPES = frozenset({ReportType.DAILY_ENGINEERING_DETAIL, ReportType.EMPLOYEE_RATING_CARDS})
DATE_MISMATCH_WARNING = (
    "DATE_MISMATCH: filename date and stated review date disagree; artifact excluded from "
    "automatic processing"
)


def _has_date_mismatch(group: list[SourceFile]) -> bool:
    return any(s.exclusion_reason == "DATE_MISMATCH" for s in group)


def _by_type(group: list[SourceFile]) -> dict[ReportType, list[SourceFile]]:
    """Usable sources indexed by report type."""
    indexed: dict[ReportType, list[SourceFile]] = {}
    for source in group:
        if not source.excluded:
            indexed.setdefault(source.report_type, []).append(source)
    return indexed


def _duplicates(indexed: dict[ReportType, list[SourceFile]]) -> str | None:
    """Two candidates for one report type: a human must pick the authoritative one."""
    found = {
        report_type: files
        for report_type, files in indexed.items()
        if len(files) > 1 and report_type is not ReportType.UNKNOWN_REPORT
    }
    if not found:
        return None
    return ", ".join(
        f"{report_type.value}: {', '.join(sorted(f.path.name for f in files))}"
        for report_type, files in found.items()
    )


def _nothing_recognized(
    group: list[SourceFile], warnings: list[str]
) -> tuple[Completeness, list[str], str | None]:
    if _has_date_mismatch(group):
        action = "Confirm the correct review date for the excluded artifacts"
        return Completeness.DATE_MISMATCH, warnings, action
    return (
        Completeness.NO_REPORTS_FOUND,
        warnings,
        "No recognizable management report for this date",
    )


def _duplicate_outcome(
    duplicated: str, warnings: list[str]
) -> tuple[Completeness, list[str], str | None]:
    warnings.append(f"DUPLICATE_SOURCE_TYPE: {duplicated}; all alternatives preserved in manifest")
    action = "Select the authoritative revision for the duplicated report type"
    return Completeness.DUPLICATE_SOURCE_TYPE, warnings, action


def _partial(
    present: set[ReportType], warnings: list[str]
) -> tuple[Completeness, list[str], str | None]:
    missing = ", ".join(sorted(t.value for t in REQUIRED_TYPES - present))
    warnings.append(
        f"PARTIAL: missing {missing}; run continues in analysis-only mode with reduced confidence"
    )
    return Completeness.PARTIAL, warnings, None


def _recognized(
    group: list[SourceFile], present: set[ReportType], warnings: list[str]
) -> tuple[Completeness, list[str], str | None]:
    if not present:
        return _nothing_recognized(group, warnings)
    if present == REQUIRED_TYPES:
        return Completeness.COMPLETE, warnings, None
    return _partial(present, warnings)


def _completeness(group: list[SourceFile]) -> tuple[Completeness, list[str], str | None]:
    """How usable this date's source set is, and what a human must do about it."""
    warnings = [DATE_MISMATCH_WARNING] if _has_date_mismatch(group) else []
    indexed = _by_type(group)
    duplicated = _duplicates(indexed)
    if duplicated:
        return _duplicate_outcome(duplicated, warnings)
    return _recognized(group, REQUIRED_TYPES & set(indexed), warnings)


def assemble(
    config: Config,
    directory: Path,
    run_id: str,
    *,
    requested_report_date: str | None = None,
    event_report_date: str | None = None,
) -> RunContext:
    """Resolve the target report date and assemble its verified source set."""
    discovered = scan(directory)
    grouped = group_by_date(discovered)
    if not grouped:
        raise DiscoveryError(f"no dated report artifacts found in {directory}")
    report_date, method = _resolve_date(grouped, requested_report_date, event_report_date)
    group = _group_for(grouped, report_date)
    completeness, warnings, human_action = _completeness(group)
    warnings += _fallback_warning(completeness, method)
    run_flags = [] if completeness is Completeness.COMPLETE else ["PARTIAL_SOURCE_DATA"]
    return RunContext(
        run_id=run_id,
        report_date=report_date,
        resolution_method=method,
        requested_report_date=(
            dates.normalize(requested_report_date) if requested_report_date else None
        ),
        completeness=completeness,
        sources=group,
        all_discovered=discovered,
        warnings=warnings,
        run_flags=run_flags,
        human_action_required=human_action,
        source_directory=config.mgmt_reports_directory,
    )


def _resolve_date(
    grouped: dict[str, list[SourceFile]],
    requested_report_date: str | None,
    event_report_date: str | None,
) -> tuple[str, DateResolution]:
    """Which report date this run is about, and how that was decided."""
    if requested_report_date:
        return dates.normalize(requested_report_date), DateResolution.EXPLICIT_ARGUMENT
    if event_report_date:
        return dates.normalize(event_report_date), DateResolution.TRIGGERING_EVENT
    return _latest_complete(grouped)


def _group_for(grouped: dict[str, list[SourceFile]], report_date: str) -> list[SourceFile]:
    group = grouped.get(report_date, [])
    if group:
        return group
    raise DiscoveryError(
        f"no report artifacts for {report_date}; available dates: {', '.join(sorted(grouped))}"
    )


def _fallback_warning(completeness: Completeness, method: DateResolution) -> list[str]:
    """Say so when no date was complete and the newest group was used instead."""
    if completeness is not Completeness.PARTIAL:
        return []
    if method is not DateResolution.LATEST_COMPLETE_GROUP:
        return []
    return [
        "No date in the directory has the full required source set; processed the newest "
        "available group instead"
    ]


def _latest_complete(grouped: dict[str, list[SourceFile]]) -> tuple[str, DateResolution]:
    """Newest date whose required set is complete, else the newest date at all."""
    for report_date in sorted(grouped, reverse=True):
        completeness, _, _ = _completeness(grouped[report_date])
        if completeness is Completeness.COMPLETE:
            return report_date, DateResolution.LATEST_COMPLETE_GROUP
    return max(grouped), DateResolution.LATEST_COMPLETE_GROUP
