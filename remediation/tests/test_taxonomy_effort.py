"""Bug versus enhancement, and the time estimates a supervisor reads."""

from __future__ import annotations

import pytest

from remediation import effort, taxonomy


def test_missing_test_reported_as_a_bug_is_revised_to_enhancement() -> None:
    result = taxonomy.evaluate("MISSING_TEST", "Regression keeps failing because tests are missing")
    assert result.reported == taxonomy.BUG
    assert result.revised == taxonomy.ENHANCEMENT
    assert result.matched is False
    assert "does not exist yet" in result.rationale


def test_code_defect_stays_a_bug() -> None:
    result = taxonomy.evaluate("CODE_DEFECT", "Claim submission crashes on retry")
    assert (result.reported, result.revised, result.matched) == (
        taxonomy.BUG,
        taxonomy.BUG,
        True,
    )


def test_automation_opportunity_is_an_enhancement() -> None:
    result = taxonomy.evaluate("AUTOMATION_OPPORTUNITY", "Introduce a script for the manual step")
    assert result.revised == taxonomy.ENHANCEMENT


def test_ci_outage_is_carried_as_a_bug_label_but_stays_an_environment_signal() -> None:
    result = taxonomy.evaluate("CI_FAILURE", "CI has no successful runs in globalcodio-monorepo")
    assert result.revised == taxonomy.BUG
    assert "CI_FAILURE" in result.rationale


def test_as_dict_exposes_the_supervisor_fields() -> None:
    fields = taxonomy.evaluate("CODE_DEFECT", "broken export").as_dict()
    assert set(fields) == {
        "reported_category",
        "revised_category",
        "category_match",
        "category_rationale",
    }


@pytest.mark.parametrize(
    ("minutes", "expected"),
    [(0, "00:00"), (5, "00:05"), (60, "01:00"), (615, "10:15")],
)
def test_hhmm_formatting(minutes: int, expected: str) -> None:
    assert effort.as_hhmm(minutes) == expected


def test_negative_minutes_are_rejected() -> None:
    with pytest.raises(ValueError):
        effort.as_hhmm(-1)


def test_all_estimates_use_hhmm() -> None:
    estimate = effort.estimate(4, "CODE_CHANGE", "B")
    for value in (estimate.human, estimate.ai, estimate.joint):
        hours, _, minutes = value.partition(":")
        assert len(hours) >= 2 and len(minutes) == 2
        assert int(minutes) < 60


def test_ai_is_faster_than_a_human_when_it_may_implement() -> None:
    estimate = effort.estimate(5, "CODE_CHANGE", "A")
    assert estimate.ai < estimate.human


def test_proposal_only_tier_needs_human_time_on_top() -> None:
    estimate = effort.estimate(5, "CODE_CHANGE", "D")
    assert estimate.joint > estimate.human
    assert any("proposal only" in reason for reason in estimate.basis)


def test_higher_complexity_costs_more() -> None:
    low = effort.estimate(2, "CODE_CHANGE", "A")
    high = effort.estimate(8, "CODE_CHANGE", "A")
    assert high.human > low.human


def test_for_issue_reads_the_analysed_fields() -> None:
    issue = {"complexity": {"score": 3}, "remediable": "NON_CODE_PROCESS", "autonomy_tier": "C"}
    estimate = effort.for_issue(issue)
    assert "remediability NON_CODE_PROCESS" in estimate.basis
    assert estimate.as_dict()["time_human_ai"] == estimate.joint
