"""Issue state machine.

All states of the full lifecycle are represented, including the stages that
Version 1 does not execute. Only the Version 1 transitions are enabled for
automatic use; everything else is declared so later stages can be switched on
without redesigning the model.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class State(str, Enum):
    DISCOVERED = "DISCOVERED"
    TRIAGED = "TRIAGED"
    PLAYBOOK_MATCHED = "PLAYBOOK_MATCHED"
    PLANNED = "PLANNED"
    DEV_FIXING = "DEV_FIXING"
    DEV_REVIEW = "DEV_REVIEW"
    QA_TESTING = "QA_TESTING"
    UAT_TESTING = "UAT_TESTING"
    RELEASE_READY = "RELEASE_READY"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"
    REJECTED = "REJECTED"
    ROLLED_BACK = "ROLLED_BACK"


#: Transitions Version 1 may perform automatically.
V1_TRANSITIONS: frozenset[tuple[State, State]] = frozenset(
    {
        (State.DISCOVERED, State.TRIAGED),
        (State.TRIAGED, State.PLAYBOOK_MATCHED),
        (State.PLAYBOOK_MATCHED, State.PLANNED),
        (State.PLANNED, State.DEV_FIXING),
        (State.DEV_FIXING, State.DEV_REVIEW),
        # A rejected review starts a new attempt back in DEV_FIXING.
        (State.DEV_REVIEW, State.DEV_FIXING),
    }
)

#: Transitions that are part of the model but must not be taken by Version 1.
FUTURE_TRANSITIONS: frozenset[tuple[State, State]] = frozenset(
    {
        (State.DEV_REVIEW, State.QA_TESTING),
        (State.QA_TESTING, State.UAT_TESTING),
        # A UAT failure never goes straight back to Dev: QA must reproduce and
        # classify it first.
        (State.UAT_TESTING, State.QA_TESTING),
        (State.QA_TESTING, State.DEV_FIXING),
        (State.UAT_TESTING, State.RELEASE_READY),
        (State.RELEASE_READY, State.CLOSED),
        (State.RELEASE_READY, State.ROLLED_BACK),
        (State.CLOSED, State.ROLLED_BACK),
    }
)

#: Any active state may stop into an exceptional state.
_STOPPABLE = (
    State.DISCOVERED,
    State.TRIAGED,
    State.PLAYBOOK_MATCHED,
    State.PLANNED,
    State.DEV_FIXING,
    State.DEV_REVIEW,
    State.QA_TESTING,
    State.UAT_TESTING,
)

EXCEPTIONAL_TRANSITIONS: frozenset[tuple[State, State]] = frozenset(
    {(s, State.BLOCKED) for s in _STOPPABLE}
    | {(s, State.REJECTED) for s in _STOPPABLE}
    | {(State.BLOCKED, State.TRIAGED), (State.BLOCKED, State.DEV_FIXING)}
)

ALL_TRANSITIONS = V1_TRANSITIONS | FUTURE_TRANSITIONS | EXCEPTIONAL_TRANSITIONS

#: States a Version 1 run is allowed to leave an issue in.
V1_TERMINAL_STATES = frozenset(
    {State.DEV_REVIEW, State.BLOCKED, State.REJECTED, State.DISCOVERED, State.TRIAGED}
)


class InvalidTransition(Exception):
    """Raised when a transition is not part of the state model."""


class FutureStageDisabled(Exception):
    """Raised when a Version 1 run tries to promote into QA/UAT/release."""


@dataclass(frozen=True)
class Transition:
    from_state: State
    to_state: State
    reason: str


def validate_transition(
    from_state: State, to_state: State, *, allow_future_stages: bool = False
) -> None:
    """Validate a transition, rejecting invalid and (by default) future ones."""
    pair = (from_state, to_state)
    if pair not in ALL_TRANSITIONS:
        raise InvalidTransition(f"{from_state.value} -> {to_state.value} is not a valid transition")
    if pair in FUTURE_TRANSITIONS and not allow_future_stages:
        raise FutureStageDisabled(
            f"{from_state.value} -> {to_state.value} belongs to a stage that is "
            "defined but not enabled in Version 1"
        )


def transition(
    from_state: State,
    to_state: State,
    reason: str,
    *,
    allow_future_stages: bool = False,
) -> Transition:
    validate_transition(from_state, to_state, allow_future_stages=allow_future_stages)
    return Transition(from_state=from_state, to_state=to_state, reason=reason)
