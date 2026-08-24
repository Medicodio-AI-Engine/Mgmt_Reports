from __future__ import annotations

import pytest

from remediation import naming
from remediation.naming import Audience, Stage
from remediation.states import (
    FutureStageDisabled,
    InvalidTransition,
    State,
    transition,
    validate_transition,
)


def test_identifier_formats_are_stable() -> None:
    assert naming.issue_id(1) == "ISSUE_000001"
    assert naming.attempt_id("ISSUE_000001", 2) == "ISSUE_000001_ATTEMPT_02"
    assert naming.run_id(12) == "RUN_0012"
    assert naming.next_attempt("ISSUE_000001_ATTEMPT_09") == "ISSUE_000001_ATTEMPT_10"


def test_identifier_regexes_reject_near_misses() -> None:
    assert naming.ISSUE_ID.match("ISSUE_00001") is None
    assert naming.ATTEMPT_ID.match("ISSUE_000001_ATTEMPT_1") is None
    assert naming.RUN_ID.match("RUN_00001") is None


def test_artifact_names_follow_the_required_convention() -> None:
    assert (
        naming.artifact_name("2026_08_23", "RUN_0001", Stage.DEV_FIX, "OUTPUT", Audience.DEVIN_AI)
        == "2026_08_23_RUN_0001_04_DEV_FIX_OUTPUT_DEVIN_AI.json"
    )
    assert (
        naming.artifact_name(
            "2026_08_23", "RUN_0001", Stage.DEV_REVIEW, "OUTPUT", Audience.PEOPLE_ENGINEER, "md"
        )
        == "2026_08_23_RUN_0001_05_DEV_REVIEW_OUTPUT_PEOPLE_ENGINEER.md"
    )
    assert (
        naming.artifact_name("2026_08_23", "RUN_0001", Stage.TRIAGE, "INPUT")
        == "2026_08_23_RUN_0001_01_TRIAGE_INPUT.json"
    )


@pytest.mark.parametrize(
    ("source", "target"),
    [
        (State.DISCOVERED, State.TRIAGED),
        (State.TRIAGED, State.PLAYBOOK_MATCHED),
        (State.PLAYBOOK_MATCHED, State.PLANNED),
        (State.PLANNED, State.DEV_FIXING),
        (State.DEV_FIXING, State.DEV_REVIEW),
        (State.DEV_REVIEW, State.DEV_FIXING),
    ],
)
def test_the_v1_transitions_are_enabled(source: State, target: State) -> None:
    assert transition(source, target, "test").to_state is target


def test_promotion_past_dev_review_is_refused() -> None:
    with pytest.raises(FutureStageDisabled):
        validate_transition(State.DEV_REVIEW, State.QA_TESTING)


def test_promotion_past_dev_review_is_possible_only_when_future_stages_are_enabled() -> None:
    validate_transition(State.DEV_REVIEW, State.QA_TESTING, allow_future_stages=True)


def test_an_undefined_transition_is_always_refused() -> None:
    with pytest.raises(InvalidTransition):
        validate_transition(State.DISCOVERED, State.RELEASE_READY, allow_future_stages=True)


def test_exceptional_states_stay_reachable() -> None:
    assert transition(State.PLANNED, State.BLOCKED, "guardrail").to_state is State.BLOCKED
    assert transition(State.DEV_REVIEW, State.REJECTED, "rejected").to_state is State.REJECTED
