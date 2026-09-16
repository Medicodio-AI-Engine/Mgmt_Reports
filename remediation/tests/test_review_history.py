"""Review decisions, attempt history, stable ids, metrics, and future contracts."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from remediation import ids, metrics, review
from remediation.attempts import AttemptImmutabilityError, AttemptStore
from remediation.audit import AuditLog
from remediation.contracts import StageDisabledError, future_stages
from remediation.review import Outcome
from remediation.states import State


def _issue(attempt: str = "ISSUE_000001_ATTEMPT_01", **overrides: Any) -> dict[str, Any]:
    base = {
        "issue_id": "ISSUE_000001",
        "run_id": "RUN_0001",
        "attempt_id": attempt,
        "title": "Missing regression tests",
        "category": "MISSING_TEST",
        "state": State.DEV_REVIEW.value,
        "remediable": "CODE_CHANGE",
        "autonomy_tier": "C",
        "playbook_match": {"playbook_id": "ORG_PB_REGRESSION_TEST_GENERATION"},
        "missing_skills": ["ci.run_targeted_tests"],
    }
    return {**base, **overrides}


def test_the_generated_block_round_trips_through_the_parser() -> None:
    block = review.decision_block("ISSUE_000001_ATTEMPT_01", "Missing regression tests")
    parsed = review.parse_decisions(block)
    decision = parsed["ISSUE_000001_ATTEMPT_01"]
    assert decision.outcome is Outcome.PENDING
    assert decision.issue_id == "ISSUE_000001"
    assert decision.attempt_id == "ISSUE_000001_ATTEMPT_01"


def test_each_supported_outcome_parses() -> None:
    text = """
### DECISION: ISSUE_000001_ATTEMPT_01
DECISION: APPROVE
REVIEWER: raj

### DECISION: ISSUE_000002_ATTEMPT_01
DECISION: REVIEW
QUESTIONS: Which repository owns this? | Is the CI outage resolved?

### DECISION: ISSUE_000003_ATTEMPT_02
DECISION: REJECT
COMMENTS: The evidence does not support a code change.
"""
    parsed = review.parse_decisions(text)
    assert parsed["ISSUE_000001_ATTEMPT_01"].outcome is Outcome.APPROVE
    assert parsed["ISSUE_000001_ATTEMPT_01"].reviewer == "raj"
    assert parsed["ISSUE_000002_ATTEMPT_01"].outcome is Outcome.REVIEW
    assert len(parsed["ISSUE_000002_ATTEMPT_01"].questions) == 2
    assert parsed["ISSUE_000003_ATTEMPT_02"].outcome is Outcome.REJECT
    assert parsed["ISSUE_000003_ATTEMPT_02"].comments


def test_a_review_without_a_question_is_not_accepted() -> None:
    parsed = review.parse_decisions(
        "### DECISION: ISSUE_000001_ATTEMPT_01\nDECISION: REVIEW\nQUESTIONS:\n"
    )
    decision = parsed["ISSUE_000001_ATTEMPT_01"]
    assert decision.outcome is Outcome.PENDING
    assert decision.malformed


def test_a_block_without_a_decision_line_is_reported_as_malformed() -> None:
    parsed = review.parse_decisions(
        "### DECISION: ISSUE_000001_ATTEMPT_01\nREVIEWER: raj\nCOMMENTS: looks fine\n"
    )
    decision = parsed["ISSUE_000001_ATTEMPT_01"]
    assert decision.outcome is Outcome.PENDING
    assert "no DECISION: line" in (decision.malformed or "")


def test_an_untouched_generated_block_is_not_malformed() -> None:
    block = review.decision_block("ISSUE_000001_ATTEMPT_01", "Missing regression tests")
    assert review.parse_decisions(block)["ISSUE_000001_ATTEMPT_01"].malformed is None


def test_an_unrecognized_outcome_is_reported_not_guessed() -> None:
    parsed = review.parse_decisions(
        "### DECISION: ISSUE_000001_ATTEMPT_01\nDECISION: looks fine to me\n"
    )
    decision = parsed["ISSUE_000001_ATTEMPT_01"]
    assert decision.outcome is Outcome.PENDING
    assert "unrecognized decision value" in (decision.malformed or "")


def test_decisions_are_collected_from_committed_artifacts(tmp_path: Path) -> None:
    stage = tmp_path / "05_DEV_REVIEW"
    stage.mkdir()
    (stage / "review.md").write_text(
        "### DECISION: ISSUE_000001_ATTEMPT_01\nDECISION: APPROVE\n", encoding="utf-8"
    )
    collected = review.load_decisions(tmp_path)
    assert collected["ISSUE_000001_ATTEMPT_01"].outcome is Outcome.APPROVE
    assert collected["ISSUE_000001_ATTEMPT_01"].source_file is not None


def test_approval_does_not_promote_past_dev_review() -> None:
    applied = review.apply_decision(
        _issue(), review.Decision(issue_id="ISSUE_000001", outcome=Outcome.APPROVE)
    )
    assert applied["state"] == State.DEV_REVIEW.value
    assert applied["next_state"] == State.DEV_REVIEW.value
    assert applied["attempt_id"] == "ISSUE_000001_ATTEMPT_01"
    assert any("stops at DEV_REVIEW" in note for note in applied["notes"])


def test_questions_keep_the_issue_in_review() -> None:
    applied = review.apply_decision(
        _issue(),
        review.Decision(
            issue_id="ISSUE_000001", outcome=Outcome.REVIEW, questions=["Which repository?"]
        ),
    )
    assert applied["state"] == State.DEV_REVIEW.value
    assert applied["questions"] == ["Which repository?"]


def test_rejection_opens_exactly_one_successor_attempt() -> None:
    applied = review.apply_decision(
        _issue(), review.Decision(issue_id="ISSUE_000001", outcome=Outcome.REJECT)
    )
    assert applied["state"] == State.DEV_FIXING.value
    assert applied["attempt_id"] == "ISSUE_000001_ATTEMPT_02"
    assert applied["superseded_attempt_id"] == "ISSUE_000001_ATTEMPT_01"


def test_an_issue_id_is_stable_across_runs(tmp_path: Path) -> None:
    path = tmp_path / "issue_registry.json"
    first = ids.IssueRegistry.load(path)
    allocated = [first.resolve("SIG_A"), first.resolve("SIG_B")]
    first.save()

    second = ids.IssueRegistry.load(path)
    assert second.resolve("SIG_B") == allocated[1]
    assert second.resolve("SIG_A") == allocated[0]
    # A genuinely new finding gets a new id rather than reusing one.
    assert second.resolve("SIG_C") not in allocated


def test_an_attempt_record_is_immutable(tmp_path: Path) -> None:
    store = AttemptStore(tmp_path / "attempts.jsonl")
    record = {
        "issue_id": "ISSUE_000001",
        "run_id": "RUN_0001",
        "attempt_id": "ISSUE_000001_ATTEMPT_01",
        "state": State.DEV_REVIEW.value,
    }
    store.open_attempt(record)
    with pytest.raises(AttemptImmutabilityError):
        store.open_attempt(record)
    assert store.open_attempt_if_absent(record) is None
    assert len(store.attempts()) == 1


def test_history_records_a_rejection_and_its_successor(tmp_path: Path) -> None:
    store = AttemptStore(tmp_path / "attempts.jsonl")
    base = {"issue_id": "ISSUE_000001", "run_id": "RUN_0001", "state": State.DEV_REVIEW.value}
    store.open_attempt({**base, "attempt_id": "ISSUE_000001_ATTEMPT_01"})
    assert store.current_number("ISSUE_000001") == 1

    store.record_decision(
        attempt_id="ISSUE_000001_ATTEMPT_01",
        issue_id="ISSUE_000001",
        run_id="RUN_0001",
        result="REJECT",
        comments=["evidence insufficient"],
    )
    assert store.current_number("ISSUE_000001") == 2

    store.open_attempt(
        {
            **base,
            "attempt_id": "ISSUE_000001_ATTEMPT_02",
            "state": State.DEV_FIXING.value,
            "supersedes_attempt_id": "ISSUE_000001_ATTEMPT_01",
        }
    )
    history = store.rejection_history("ISSUE_000001")
    assert [entry["attempt_id"] for entry in history] == ["ISSUE_000001_ATTEMPT_01"]
    assert store.current_number("ISSUE_000001") == 2
    # The rejected attempt is still on file untouched.
    assert store.attempts()[0]["attempt_id"] == "ISSUE_000001_ATTEMPT_01"


def test_a_decision_is_recorded_once(tmp_path: Path) -> None:
    store = AttemptStore(tmp_path / "attempts.jsonl")
    store.open_attempt(
        {
            "issue_id": "ISSUE_000001",
            "run_id": "RUN_0001",
            "attempt_id": "ISSUE_000001_ATTEMPT_01",
            "state": State.DEV_REVIEW.value,
        }
    )
    for _ in range(3):
        store.record_decision(
            attempt_id="ISSUE_000001_ATTEMPT_01",
            issue_id="ISSUE_000001",
            run_id="RUN_0001",
            result="APPROVE",
        )
    assert len(store.decisions()) == 1


def test_the_audit_log_only_appends(tmp_path: Path) -> None:
    path = tmp_path / "audit.jsonl"
    log = AuditLog(path, "RUN_0001")
    log.record("SOURCE_DISCOVERY", stage="PRE_STAGE")
    log.record("ISSUE_NORMALIZED", issue_id="ISSUE_000001")
    AuditLog(path, "RUN_0002").record("SOURCE_DISCOVERY", stage="PRE_STAGE")
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 3
    assert '"RUN_0001"' in lines[0]
    assert '"RUN_0002"' in lines[2]


def test_metrics_never_claim_work_that_did_not_happen() -> None:
    collected = metrics.collect([_issue(), _issue(attempt="ISSUE_000002_ATTEMPT_01")], [], True)
    assert collected["issues_total"] == 2
    assert collected["executions_performed"] == 0
    assert collected["commits_created"] == 0
    assert collected["pull_requests_created"] == 0
    assert collected["repositories_modified"] == []
    assert collected["missing_capabilities"] == {"ci.run_targeted_tests": 2}
    assert collected["playbook_match_rate"] == 1.0
    assert collected["human_decisions_recorded"] == 0


def test_metrics_count_guardrail_stops() -> None:
    blocked = _issue(guardrail_violations=[{"rule": "ENVIRONMENT_AS_CODE_DEFECT"}])
    collected = metrics.collect([blocked], [], True)
    assert collected["guardrail_blocked_count"] == 1
    assert collected["guardrail_rules_fired"] == {"ENVIRONMENT_AS_CODE_DEFECT": 1}


@pytest.mark.parametrize(
    "call",
    [
        lambda issue: future_stages.qa_result(issue, [], [], "PASS"),
        lambda issue: future_stages.uat_result(issue, "PASS"),
        lambda issue: future_stages.release_readiness(
            issue,
            approvals_complete=True,
            tests_passed=True,
            qa_passed=True,
            uat_passed=True,
            unresolved_blockers=[],
            rollback_plan="revert",
            deployment_procedure="pipeline",
            change_references=[],
        ),
        lambda issue: future_stages.learning_record(issue, 1),
    ],
)
def test_future_stages_are_refused_while_disabled(call: Any) -> None:
    with pytest.raises(StageDisabledError):
        call(_issue())


def test_a_future_stage_contract_is_already_schema_valid() -> None:
    document = future_stages.qa_result(
        _issue(),
        [
            {
                "case_id": "QA_001",
                "derived_from": ["ISSUE", "ACCEPTANCE_CRITERIA"],
                "steps": ["send an email without a case number"],
                "expected": "no default case_number header is present",
            }
        ],
        [],
        "PASS",
        enabled=True,
    )
    assert document["issue_id"] == "ISSUE_000001"
    assert document["verdict"] == "PASS"
