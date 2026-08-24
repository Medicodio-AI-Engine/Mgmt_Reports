from __future__ import annotations

from pathlib import Path

import pytest

from helpers import write_cards_report, write_detail_report
from remediation import discovery, schema
from remediation.config import Config


def test_classify_uses_filename_and_heading(report_directory: Path) -> None:
    detail = write_detail_report(report_directory)
    report_type, notes = discovery.classify(detail, detail.read_text(encoding="utf-8"))
    assert report_type is discovery.ReportType.DAILY_ENGINEERING_DETAIL
    assert notes == [] or all(isinstance(note, str) for note in notes)


def test_classify_recognizes_rating_cards(report_directory: Path) -> None:
    cards = write_cards_report(report_directory)
    report_type, _ = discovery.classify(cards, cards.read_text(encoding="utf-8"))
    assert report_type is discovery.ReportType.EMPLOYEE_RATING_CARDS


def test_classify_marks_an_unrelated_file_unknown(report_directory: Path) -> None:
    other = report_directory / "notes-2026-08-23.md"
    other.write_text("# Some other document\n", encoding="utf-8")
    report_type, _ = discovery.classify(other, other.read_text(encoding="utf-8"))
    assert report_type is discovery.ReportType.UNKNOWN_REPORT


def test_scan_extracts_dates_and_groups_them(report_directory: Path) -> None:
    write_detail_report(report_directory)
    write_cards_report(report_directory)
    write_cards_report(report_directory, date="2026-08-19")
    grouped = discovery.group_by_date(discovery.scan(report_directory))
    assert sorted(grouped) == ["2026_08_19", "2026_08_23"]
    assert len(grouped["2026_08_23"]) == 2


def test_a_detail_report_plus_cards_is_complete(config: Config, report_directory: Path) -> None:
    write_detail_report(report_directory)
    write_cards_report(report_directory)
    context = discovery.assemble(config, report_directory, "RUN_0001")
    assert context.completeness is discovery.Completeness.COMPLETE
    assert context.processable
    assert context.missing_sources() == []


def test_cards_only_is_partial_and_analysis_only(config: Config, report_directory: Path) -> None:
    write_cards_report(report_directory, date="2026-08-19")
    context = discovery.assemble(config, report_directory, "RUN_0001")
    assert context.completeness is discovery.Completeness.PARTIAL
    assert not context.required_sources_present
    assert "PARTIAL_SOURCE_DATA" in context.run_flags
    assert "DAILY_ENGINEERING_DETAIL" in context.missing_sources()


def test_the_latest_complete_date_wins_over_a_newer_partial_one(
    config: Config, report_directory: Path
) -> None:
    write_detail_report(report_directory, date="2026-08-22")
    write_cards_report(report_directory, date="2026-08-22")
    write_cards_report(report_directory, date="2026-08-23")
    context = discovery.assemble(config, report_directory, "RUN_0001")
    assert context.report_date == "2026_08_22"
    assert context.completeness is discovery.Completeness.COMPLETE


def test_a_requested_date_is_honored_even_when_partial(
    config: Config, report_directory: Path
) -> None:
    write_detail_report(report_directory)
    write_cards_report(report_directory)
    write_cards_report(report_directory, date="2026-08-19")
    context = discovery.assemble(
        config, report_directory, "RUN_0001", requested_report_date="2026-08-19"
    )
    assert context.report_date == "2026_08_19"
    assert context.resolution_method is discovery.DateResolution.EXPLICIT_ARGUMENT
    assert context.completeness is discovery.Completeness.PARTIAL


def test_two_detail_reports_for_one_date_are_ambiguous(
    config: Config, report_directory: Path
) -> None:
    write_detail_report(report_directory)
    write_cards_report(report_directory)
    duplicate = report_directory / "mgmt-activity-report-2026-08-23-v2.md"
    duplicate.write_text(
        (report_directory / "mgmt-activity-report-2026-08-23.md").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    context = discovery.assemble(config, report_directory, "RUN_0001")
    assert context.completeness is discovery.Completeness.DUPLICATE_SOURCE_TYPE
    assert not context.processable
    # Nothing is silently discarded: both candidates stay on the manifest.
    detail_paths = [
        source.path.name
        for source in context.sources
        if source.report_type is discovery.ReportType.DAILY_ENGINEERING_DETAIL
    ]
    assert len(detail_paths) == 2


def test_a_content_date_disagreeing_with_the_filename_is_flagged(
    config: Config, report_directory: Path
) -> None:
    detail = write_detail_report(report_directory)
    detail.write_text(
        detail.read_text(encoding="utf-8").replace(
            "**Review date:** 2026-08-23", "**Review date:** 2026-08-21"
        ),
        encoding="utf-8",
    )
    context = discovery.assemble(config, report_directory, "RUN_0001")
    assert context.completeness is discovery.Completeness.DATE_MISMATCH
    assert not context.processable
    assert any("date" in warning.lower() for warning in context.warnings)


def test_only_unrecognized_artifacts_reports_no_reports_found(
    config: Config, report_directory: Path
) -> None:
    (report_directory / "notes-2026-08-23.md").write_text("# Meeting notes\n", encoding="utf-8")
    context = discovery.assemble(config, report_directory, "RUN_0001")
    assert context.completeness is discovery.Completeness.NO_REPORTS_FOUND
    assert not context.processable


def test_an_empty_directory_is_an_error(config: Config, report_directory: Path) -> None:
    with pytest.raises(discovery.DiscoveryError):
        discovery.assemble(config, report_directory, "RUN_0001")


def test_a_missing_directory_is_an_error(config: Config, tmp_path: Path) -> None:
    with pytest.raises(discovery.DiscoveryError):
        discovery.assemble(config, tmp_path / "absent", "RUN_0001")


def test_the_manifest_validates_against_its_schema(config: Config, report_directory: Path) -> None:
    write_detail_report(report_directory)
    write_cards_report(report_directory)
    context = discovery.assemble(config, report_directory, "RUN_0001")
    schema.validate(context.manifest(config), schema.PRE_STAGE_MANIFEST)
