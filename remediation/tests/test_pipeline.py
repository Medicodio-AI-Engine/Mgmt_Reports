"""End-to-end Version 1 flow: PRE_STAGE through 05_DEV_REVIEW."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from helpers import write_cards_report, write_detail_report
from remediation import cli, discovery, pipeline, review, schema
from remediation.config import Config
from remediation.naming import Stage
from remediation.states import State

STAGES = (
    Stage.INTAKE,
    Stage.TRIAGE,
    Stage.PLAYBOOK_MATCH,
    Stage.PLAN,
    Stage.DEV_FIX,
    Stage.DEV_REVIEW,
)


@pytest.fixture
def checkout(tmp_path: Path, config: Config) -> Path:
    """A minimal Mgmt_Reports checkout containing one complete report date."""
    directory = tmp_path / "checkout" / config.mgmt_reports_directory
    directory.mkdir(parents=True)
    write_detail_report(directory)
    write_cards_report(directory)
    return tmp_path / "checkout"


def test_the_full_flow_produces_every_stage_artifact(config: Config, checkout: Path) -> None:
    result = pipeline.run(config, repository_root=checkout)

    assert result.run_context.report_date == "2026_08_23"
    assert result.run_context.completeness.value == "COMPLETE"
    assert result.issues

    for stage in (Stage.PRE_STAGE, *STAGES):
        assert result.paths.stage_dir(stage).is_dir()
    for stage in STAGES:
        directory = result.paths.stage_dir(stage)
        names = {path.name for path in directory.iterdir()}
        assert any(name.endswith("_INPUT.json") for name in names)
        assert any(name.endswith("_OUTPUT_DEVIN_AI.json") for name in names)
        assert any(name.endswith("_OUTPUT_PEOPLE_ENGINEER.md") for name in names)
        assert all(name.startswith(f"2026_08_23_{result.run_context.run_id}_") for name in names)

    assert (result.paths.root / "audit.jsonl").exists()
    assert (result.paths.root / f"2026_08_23_{result.run_context.run_id}_METRICS.json").exists()
    assert (result.paths.root / f"2026_08_23_{result.run_context.run_id}_SUMMARY.md").exists()


def test_every_machine_output_validates_and_chains_to_the_next_stage(
    config: Config, checkout: Path
) -> None:
    result = pipeline.run(config, repository_root=checkout)
    for stage in STAGES:
        directory = result.paths.stage_dir(stage)
        path = next(p for p in directory.iterdir() if p.name.endswith("_OUTPUT_DEVIN_AI.json"))
        document = json.loads(path.read_text(encoding="utf-8"))
        schema.validate(document, schema.STAGE_OUTPUT)
        assert document["stage"] == stage.value
        assert document["dry_run"] is True
        if stage is not Stage.DEV_REVIEW:
            expected = document["next_expected_input_file"]
            assert expected is not None
            assert expected.endswith("_INPUT.json")
        else:
            assert document["next_expected_input_file"] is None


def test_a_stage_input_references_the_previous_output_by_digest(
    config: Config, checkout: Path
) -> None:
    result = pipeline.run(config, repository_root=checkout)
    previous = Stage.INTAKE
    for stage in STAGES[1:]:
        directory = result.paths.stage_dir(stage)
        path = next(p for p in directory.iterdir() if p.name.endswith("_INPUT.json"))
        reference = json.loads(path.read_text(encoding="utf-8"))
        assert reference["source_stage"] == previous.value
        source = result.paths.root / reference["source_artifact"]
        assert hashlib.sha256(source.read_bytes()).hexdigest() == reference["sha256"], (
            f"{stage.value} input does not match the {previous.value} output it names"
        )
        previous = stage


def test_the_run_stops_at_dev_review_and_changes_nothing(config: Config, checkout: Path) -> None:
    result = pipeline.run(config, repository_root=checkout)

    terminal = {issue["state"] for issue in result.issues}
    assert terminal <= {State.DEV_REVIEW.value, State.BLOCKED.value, State.DEV_FIXING.value}
    assert not any(
        state in terminal
        for state in (
            State.QA_TESTING.value,
            State.UAT_TESTING.value,
            State.RELEASE_READY.value,
            State.CLOSED.value,
        )
    )
    assert result.metrics["commits_created"] == 0
    assert result.metrics["pull_requests_created"] == 0
    assert result.metrics["repositories_modified"] == []
    assert result.metrics["executions_performed"] == 0
    for issue in result.issues:
        assert issue.get("commit_sha") is None
        assert issue.get("pr_number") is None
        assert not issue.get("changed_files")
        assert issue.get("execution_allowed") is False


def test_the_review_artifact_asks_for_a_decision_per_attempt(
    config: Config, checkout: Path
) -> None:
    result = pipeline.run(config, repository_root=checkout)
    path = next(
        p
        for p in result.paths.stage_dir(Stage.DEV_REVIEW).iterdir()
        if p.name.endswith("_OUTPUT_PEOPLE_ENGINEER.md")
    )
    parsed = review.parse_decisions(path.read_text(encoding="utf-8"))
    reviewable = [issue for issue in result.issues if not issue["guardrail_violations"]]
    assert {issue["attempt_id"] for issue in reviewable} <= set(parsed)
    assert all(decision.outcome is review.Outcome.PENDING for decision in parsed.values())


def test_issue_ids_are_stable_across_two_runs(config: Config, checkout: Path) -> None:
    first = pipeline.run(config, repository_root=checkout)
    second = pipeline.run(config, repository_root=checkout)

    assert second.run_context.run_id != first.run_context.run_id
    by_signature = {issue["dedupe_signature"]: issue["issue_id"] for issue in first.issues}
    assert {issue["dedupe_signature"]: issue["issue_id"] for issue in second.issues} == by_signature
    assert all(issue["attempt_id"].endswith("_ATTEMPT_01") for issue in second.issues)


def _decide(path: Path, attempt_id: str, outcome: str, extra: str = "") -> None:
    path.write_text(
        f"### DECISION: {attempt_id}\nDECISION: {outcome}\nREVIEWER: raj\n{extra}\n",
        encoding="utf-8",
    )


def test_an_approval_is_recorded_without_promoting(config: Config, checkout: Path) -> None:
    first = pipeline.run(config, repository_root=checkout)
    target = next(issue for issue in first.issues if not issue["guardrail_violations"])
    _decide(config.artifact_root_directory / "decisions.md", target["attempt_id"], "APPROVE")

    second = pipeline.run(config, repository_root=checkout)
    reviewed = next(i for i in second.issues if i["issue_id"] == target["issue_id"])
    assert reviewed["human_review_result"] == "APPROVE"
    assert reviewed["state"] == State.DEV_REVIEW.value
    assert reviewed["attempt_id"] == target["attempt_id"]


def test_a_rejection_opens_one_successor_attempt_and_keeps_the_history(
    config: Config, checkout: Path
) -> None:
    first = pipeline.run(config, repository_root=checkout)
    target = next(issue for issue in first.issues if not issue["guardrail_violations"])
    decisions = config.artifact_root_directory / "decisions.md"
    _decide(decisions, target["attempt_id"], "REJECT", "COMMENTS: evidence is insufficient")

    second = pipeline.run(config, repository_root=checkout)
    rejected = next(i for i in second.issues if i["issue_id"] == target["issue_id"])
    assert rejected["state"] == State.DEV_FIXING.value
    assert rejected["attempt_id"] == f"{target['issue_id']}_ATTEMPT_02"
    assert [entry["attempt_id"] for entry in rejected["rejection_history"]] == [
        target["attempt_id"]
    ]

    # A third run must not reapply the old decision to the new attempt.
    third = pipeline.run(config, repository_root=checkout)
    again = next(i for i in third.issues if i["issue_id"] == target["issue_id"])
    assert again["attempt_id"] == f"{target['issue_id']}_ATTEMPT_02"
    assert again["human_review_result"] == "PENDING"
    assert len(again["rejection_history"]) == 1


def test_a_question_keeps_the_attempt_in_review(config: Config, checkout: Path) -> None:
    first = pipeline.run(config, repository_root=checkout)
    target = next(issue for issue in first.issues if not issue["guardrail_violations"])
    _decide(
        config.artifact_root_directory / "decisions.md",
        target["attempt_id"],
        "REVIEW",
        "QUESTIONS: Which repository owns this?",
    )
    second = pipeline.run(config, repository_root=checkout)
    asked = next(i for i in second.issues if i["issue_id"] == target["issue_id"])
    assert asked["human_review_result"] == "REVIEW"
    assert asked["questions"] == ["Which repository owns this?"]
    assert asked["attempt_id"] == target["attempt_id"]
    assert asked["state"] == State.DEV_REVIEW.value


def test_partial_sources_are_flagged_but_still_analysed(config: Config, tmp_path: Path) -> None:
    directory = tmp_path / "cards_only" / config.mgmt_reports_directory
    directory.mkdir(parents=True)
    write_cards_report(directory)
    result = pipeline.run(config, repository_root=tmp_path / "cards_only")
    assert result.run_context.completeness.value == "PARTIAL"
    assert "PARTIAL_SOURCE_DATA" in result.run_context.run_flags
    assert all(issue["corroborating_only"] for issue in result.issues)
    assert all(issue["remediable"] != "CODE_CHANGE" for issue in result.issues)


def test_a_missing_report_directory_fails_loudly(config: Config, tmp_path: Path) -> None:
    with pytest.raises(discovery.DiscoveryError):
        pipeline.run(config, repository_root=tmp_path / "empty")


def test_the_cli_runs_the_flow_and_reports_dry_run(
    config: Config, checkout: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    code = cli.main(
        [
            "--artifact-root",
            str(config.artifact_root_directory),
            "run",
            "--report-date",
            "2026-08-23",
            "--repository-root",
            str(checkout),
        ]
    )
    captured = capsys.readouterr().out
    assert code == 0
    assert "dry_run True" in captured
    assert "completeness COMPLETE" in captured


def test_the_cli_reports_a_refusal_in_one_line(
    config: Config, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    code = cli.main(
        [
            "--artifact-root",
            str(config.artifact_root_directory),
            "run",
            "--repository-root",
            str(tmp_path / "empty"),
        ]
    )
    captured = capsys.readouterr()
    assert code == 1
    assert captured.err.strip().startswith("DiscoveryError: ")
    assert "Traceback" not in captured.err


def test_the_cli_validate_command_loads_everything(
    config: Config, capsys: pytest.CaptureFixture[str]
) -> None:
    assert cli.main(["validate"]) == 0
    captured = capsys.readouterr().out
    assert "dry_run_mode True" in captured
    assert "approval_mechanism FILE_DECISION_BLOCK" in captured
    for name in schema.SCHEMAS:
        assert f"schema loaded: {name}" in captured
