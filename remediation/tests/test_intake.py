"""Markdown parsing, extraction, deduplication, and normalization."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from helpers import write_cards_report, write_detail_report
from remediation import dedupe, discovery, extract, markdown, normalize, schema
from remediation.config import Config


def _sources(config: Config, directory: Path) -> discovery.RunContext:
    write_detail_report(directory)
    write_cards_report(directory)
    return discovery.assemble(config, directory, "RUN_0001")


def _findings(config: Config, directory: Path) -> tuple[discovery.RunContext, list[Any]]:
    context = _sources(config, directory)
    findings: list[Any] = []
    for source in context.sources:
        findings += extract.extract(source)
    return context, findings


def test_sections_keep_their_source_line_numbers(report_directory: Path) -> None:
    path = write_detail_report(report_directory)
    parsed = markdown.sections(path.read_text(encoding="utf-8"))
    members = markdown.member_sections(parsed, "example-engineer")
    assert members, "the per-engineer section must be found"
    assert all(line > 0 for line, _ in members[0].lines)


def test_tables_are_addressable_by_header_name(report_directory: Path) -> None:
    path = write_detail_report(report_directory)
    parsed = markdown.sections(path.read_text(encoding="utf-8"))
    repetitive = markdown.find(parsed, "Repetitive Work Identified")
    rows = repetitive[0].tables()[0].rows
    assert rows[0].get("Activity", "activity") is not None
    assert rows[0].get("Better Approach") is not None
    assert rows[0].line > 0


def test_extraction_finds_each_kind_of_report_evidence(
    config: Config, report_directory: Path
) -> None:
    _, findings = _findings(config, report_directory)
    categories = {finding.category for finding in findings}
    assert "CI_FAILURE" in categories
    assert "MISSING_TEST" in categories
    assert "SECURITY_TENANCY" in categories
    assert "PROCESS_PRACTICE" in categories
    assert all(finding.source_line > 0 for finding in findings)
    assert all(finding.quote for finding in findings)


def test_the_ci_blackout_is_an_environment_signal(config: Config, report_directory: Path) -> None:
    _, findings = _findings(config, report_directory)
    ci = [f for f in findings if f.category == "CI_FAILURE"]
    assert ci and all(f.environment_signal for f in ci)


def test_rating_cards_are_corroborating_only(config: Config, report_directory: Path) -> None:
    _, findings = _findings(config, report_directory)
    cards = [f for f in findings if f.source_report_type == "EMPLOYEE_RATING_CARDS"]
    assert cards
    assert all(f.corroborating_only for f in cards)
    # A healthy score is not a finding at all.
    assert all("8" not in f.title for f in cards)


def test_identical_findings_merge_and_keep_every_source(
    config: Config, report_directory: Path
) -> None:
    _, findings = _findings(config, report_directory)
    duplicated = [*findings, findings[0]]
    clusters = dedupe.cluster(duplicated)
    assert len(clusters) == len(dedupe.cluster(findings))
    merged = next(c for c in clusters if c.signature == dedupe.signature(findings[0]))
    assert len(merged.all_findings) >= 2


def test_findings_in_different_repositories_never_merge(
    config: Config, report_directory: Path
) -> None:
    _, findings = _findings(config, report_directory)
    left = next(f for f in findings if f.repository)
    right = type(left)(**{**left.__dict__, "repository": "some-other-repository"})
    clusters = dedupe.cluster([left, right])
    assert len(clusters) == 2


def test_corroborating_findings_never_merge_into_substantive_ones(
    config: Config, report_directory: Path
) -> None:
    _, findings = _findings(config, report_directory)
    for cluster in dedupe.cluster(findings):
        kinds = {f.corroborating_only for f in cluster.all_findings}
        assert len(kinds) == 1, "a rating-card row must not be folded into a report finding"


def test_normalized_issues_validate_and_keep_provenance(
    config: Config, report_directory: Path
) -> None:
    context, findings = _findings(config, report_directory)
    issues = normalize.normalize(dedupe.cluster(findings), context, config.mgmt_reports_repository)
    assert issues
    for issue in issues:
        schema.validate(issue, schema.ISSUE)
        assert issue["source_provenance"]
        assert all(
            entry["report_date"] == context.report_date for entry in issue["source_provenance"]
        )
        assert issue["evidence"], "every issue must carry evidence"
        assert issue["state"] == "DISCOVERED"


def test_rating_detail_is_redacted_but_stays_locatable(
    config: Config, report_directory: Path
) -> None:
    context, findings = _findings(config, report_directory)
    issues = normalize.normalize(
        dedupe.cluster(findings), context, config.mgmt_reports_repository, redact_ratings=True
    )
    rating_issues = [i for i in issues if i["corroborating_only"]]
    assert rating_issues
    for issue in rating_issues:
        excerpts = " ".join(item["excerpt"] for item in issue["evidence"])
        assert normalize.RATING_REDACTION in excerpts
        assert not any(character.isdigit() for character in excerpts)
        assert all(item["locator"] for item in issue["evidence"])


def test_a_missing_value_stays_explicit(config: Config, report_directory: Path) -> None:
    context, findings = _findings(config, report_directory)
    issues = normalize.normalize(dedupe.cluster(findings), context, config.mgmt_reports_repository)
    unresolved = [i for i in issues if i["repository"] is None]
    assert unresolved, "the fixture contains findings with no single resolvable repository"
    assert all(i["candidate_repositories"] is not None for i in unresolved)


def test_process_findings_are_not_labelled_code_changes(
    config: Config, report_directory: Path
) -> None:
    context, findings = _findings(config, report_directory)
    issues = normalize.normalize(dedupe.cluster(findings), context, config.mgmt_reports_repository)
    for issue in issues:
        if issue["category"] == "PROCESS_PRACTICE":
            assert issue["remediable"] != "CODE_CHANGE"
        if issue["environment_signal"]:
            assert issue["remediable"] == "UNKNOWN", (
                "an environment failure must never be asserted to be a code defect"
            )
