"""Stable identifiers and the mandatory artifact naming contract."""

from __future__ import annotations

import re
from enum import Enum

ISSUE_ID = re.compile(r"^ISSUE_\d{6}$")
ATTEMPT_ID = re.compile(r"^ISSUE_\d{6}_ATTEMPT_\d{2}$")
RUN_ID = re.compile(r"^RUN_\d{4}$")


class Audience(str, Enum):
    DEVIN_AI = "DEVIN_AI"
    PEOPLE_ENGINEER = "PEOPLE_ENGINEER"


class Stage(str, Enum):
    PRE_STAGE = "PRE_STAGE"
    INTAKE = "00_INTAKE"
    TRIAGE = "01_TRIAGE"
    PLAYBOOK_MATCH = "02_PLAYBOOK_MATCH"
    PLAN = "03_PLAN"
    DEV_FIX = "04_DEV_FIX"
    DEV_REVIEW = "05_DEV_REVIEW"
    QA = "06_QA"
    UAT = "07_UAT"
    RELEASE = "08_RELEASE"
    LEARNING = "09_LEARNING"


#: Stages Version 1 executes. The remaining stages exist as contracts only.
V1_STAGES: tuple[Stage, ...] = (
    Stage.INTAKE,
    Stage.TRIAGE,
    Stage.PLAYBOOK_MATCH,
    Stage.PLAN,
    Stage.DEV_FIX,
    Stage.DEV_REVIEW,
)

FUTURE_STAGES: tuple[Stage, ...] = (Stage.QA, Stage.UAT, Stage.RELEASE, Stage.LEARNING)


def issue_id(sequence: int) -> str:
    if sequence < 1:
        raise ValueError("issue sequence starts at 1")
    return f"ISSUE_{sequence:06d}"


def attempt_id(issue: str, attempt: int) -> str:
    if not ISSUE_ID.match(issue):
        raise ValueError(f"{issue!r} is not a valid issue id")
    if attempt < 1:
        raise ValueError("attempt numbering starts at 1")
    return f"{issue}_ATTEMPT_{attempt:02d}"


def run_id(sequence: int) -> str:
    return f"RUN_{sequence:04d}"


def next_attempt(current_attempt_id: str) -> str:
    if not ATTEMPT_ID.match(current_attempt_id):
        raise ValueError(f"{current_attempt_id!r} is not a valid attempt id")
    issue, _, number = current_attempt_id.rpartition("_")
    return f"{issue}_{int(number) + 1:02d}"


def artifact_name(
    report_date: str,
    run: str,
    stage: Stage,
    artifact: str,
    audience: Audience | None = None,
    extension: str = "json",
) -> str:
    """Build a runtime artifact filename.

    ``YYYY_MM_DD_<RUN_ID>_<STAGE>_<ARTIFACT>[_<AUDIENCE>].<ext>``

    The date prefix is mandatory. ``INPUT`` artifacts carry no audience because
    they are consumed by the stage itself.
    """
    if not RUN_ID.match(run):
        raise ValueError(f"{run!r} is not a valid run id")
    parts = [report_date, run, stage.value, artifact]
    if audience is not None:
        parts.append(audience.value)
    return "_".join(parts) + f".{extension}"
