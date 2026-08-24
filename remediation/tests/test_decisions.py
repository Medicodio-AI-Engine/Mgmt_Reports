"""Scoring, playbook matching, autonomy, guardrails, planning, and execution."""

from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from remediation import autonomy, devfix, guardrails, planner, playbooks, scoring
from remediation.config import Config
from remediation.playbooks import Match, Precedence
from remediation.states import State


def issue(**overrides: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "issue_id": "ISSUE_000001",
        "run_id": "RUN_0001",
        "attempt_id": "ISSUE_000001_ATTEMPT_01",
        "title": "Missing regression tests around the email send path",
        "description": "The report records no regression test for the email header defect class.",
        "category": "MISSING_TEST",
        "security_scope": "NONE",
        "repository": "globalcodio-monorepo",
        "files": ["services/email/send.ts"],
        "merged_sources": ["SOURCE_001:20"],
        "remediable": "CODE_CHANGE",
        "candidate_repositories": ["globalcodio-monorepo"],
        "corroborating_only": False,
        "environment_signal": False,
        "confidence": 0.7,
        "frequency": None,
        "recommended_action": "Generate a regression suite",
        "reproduction": {"available": False},
        "source_reference": "2026_08_23:SOURCE_001:20",
        "dedupe_signature": "MISSING_TEST|globalcodio-monorepo|email regression send test",
        "state": State.DISCOVERED.value,
    }
    return {**base, **overrides}


def scored(**overrides: Any) -> dict[str, Any]:
    document = issue(**overrides)
    return {**document, **scoring.score(document)}


def test_priority_and_complexity_are_independent_and_explained() -> None:
    document = issue()
    priority = scoring.priority(document)
    complexity = scoring.complexity(document)
    assert 1 <= priority.value <= 10
    assert 1 <= complexity.value <= 10
    assert priority.factors and priority.rationale
    assert complexity.factors and complexity.rationale
    assert priority.factors != complexity.factors


def test_a_security_surface_raises_priority_and_complexity_together() -> None:
    plain = scoring.priority(issue()).value
    tenancy = scoring.priority(
        issue(category="SECURITY_TENANCY", security_scope="TENANT_ISOLATION")
    ).value
    assert tenancy > plain
    assert (
        scoring.complexity(
            issue(category="SECURITY_TENANCY", security_scope="TENANT_ISOLATION")
        ).value
        > scoring.complexity(issue()).value
    )


def test_rating_corroboration_cannot_inflate_priority() -> None:
    assert (
        scoring.priority(issue(corroborating_only=True, remediable="NON_CODE_PROCESS")).value
        < scoring.priority(issue()).value
    )


def test_candidate_selection_is_ordering_only() -> None:
    high = scored()
    low = scored(
        issue_id="ISSUE_000002", category="PROCESS_PRACTICE", remediable="NON_CODE_PROCESS"
    )
    order = planner.select_candidates([low, high])
    assert order[0] == "ISSUE_000001"


def test_an_org_playbook_wins_over_a_general_one(config: Config) -> None:
    registry = playbooks.load_registry(config)
    result = playbooks.match(scored(), registry, config)
    assert result.playbook is not None
    assert result.playbook.scope == "ORG"
    assert result.precedence is Precedence.ORG_PLAYBOOK
    assert result.confidence >= config.min_playbook_confidence


def test_an_unclassified_category_falls_back_to_the_general_proposal(config: Config) -> None:
    registry = playbooks.load_registry(config)
    result = playbooks.match(scored(category="UNKNOWN", title="", description=""), registry, config)
    assert result.playbook is not None
    assert result.playbook.scope == "GENERAL"
    assert result.playbook.default_autonomy_tier == "C"


def test_an_issue_no_playbook_governs_escalates(config: Config) -> None:
    registry = playbooks.load_registry(config)
    result = playbooks.match(
        scored(category="CODE_DEFECT", title="Wrong header value", description="Header is wrong."),
        registry,
        config,
    )
    assert result.playbook is None
    assert result.precedence is Precedence.NO_MATCH


def test_a_playbook_refuses_a_disallowed_security_scope(config: Config) -> None:
    registry = playbooks.load_registry(config)
    result = playbooks.match(
        scored(category="MECHANICAL_MIGRATION", security_scope="PHI"), registry, config
    )
    assert result.playbook is None or result.playbook.playbook_id != "ORG_PB_MECHANICAL_MIGRATION"
    assert any("security scope PHI" in reason for reason in result.rejected)


def test_dry_run_suppresses_the_capabilities_that_write(config: Config) -> None:
    registry = playbooks.load_registry(config)
    unavailable = {skill_id for skill_id, skill in registry.skills.items() if not skill.available}
    assert {
        "test.write_regression_test",
        "repo.multi_file_edit",
        "git.stacked_branches",
        "ci.run_targeted_tests",
        "qa.execute_cases",
    } <= unavailable


def test_no_playbook_means_investigation_only(config: Config) -> None:
    registry = playbooks.load_registry(config)
    empty = Match(playbook=None, precedence=Precedence.NO_MATCH, confidence=0)
    decision = autonomy.classify(scored(), empty, registry, config)
    assert decision.tier == "C"
    assert not decision.execution_allowed
    assert decision.approval_required


def test_a_tenancy_issue_is_human_owned(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(category="SECURITY_TENANCY", security_scope="TENANT_ISOLATION")
    decision = autonomy.classify(
        document, playbooks.match(document, registry, config), registry, config
    )
    assert decision.tier == "D"
    assert any("HUMAN_OWNED_SURFACE" in stop for stop in decision.stop_conditions)


def test_an_unverified_security_scope_never_stays_autonomous(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(security_scope="UNKNOWN")
    decision = autonomy.classify(
        document, playbooks.match(document, registry, config), registry, config
    )
    assert decision.tier in {"B", "C", "D"}
    assert any("SECURITY_SCOPE_UNVERIFIED" in stop for stop in decision.stop_conditions)


def test_an_environment_signal_is_never_implemented(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(category="CI_FAILURE", environment_signal=True, remediable="UNKNOWN")
    decision = autonomy.classify(
        document, playbooks.match(document, registry, config), registry, config
    )
    assert decision.tier in {"C", "D"}
    assert not decision.execution_allowed


def test_a_missing_capability_lowers_the_tier(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored()
    match = playbooks.match(document, registry, config)
    assert match.missing_skills, "dry-run must leave writing capabilities unavailable"
    decision = autonomy.classify(document, match, registry, config)
    assert decision.tier == "C"
    assert any("MISSING_CAPABILITY" in stop for stop in decision.stop_conditions)


def test_execution_is_never_allowed_while_dry_run_is_on(config: Config) -> None:
    registry = playbooks.load_registry(config)
    for category in ("MISSING_TEST", "MECHANICAL_MIGRATION", "PROCESS_PRACTICE", "CI_FAILURE"):
        document = scored(category=category)
        match = playbooks.match(document, registry, config)
        decision = autonomy.classify(document, match, registry, config)
        assert not decision.execution_allowed


def test_an_environment_failure_called_a_code_defect_is_blocked(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(environment_signal=True, remediable="CODE_CHANGE")
    match = playbooks.match(document, registry, config)
    decision = autonomy.classify(document, match, registry, config)
    rules = {v.rule for v in guardrails.evaluate(document, match, decision, config)}
    assert "ENVIRONMENT_AS_CODE_DEFECT" in rules


def test_rating_data_proposed_as_a_code_change_is_blocked(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(corroborating_only=True, remediable="CODE_CHANGE")
    match = playbooks.match(document, registry, config)
    decision = autonomy.classify(document, match, registry, config)
    violations = guardrails.evaluate(document, match, decision, config)
    assert "RATING_AS_DEFECT_EVIDENCE" in {v.rule for v in violations}
    assert all(v.forced_state == State.BLOCKED.value for v in violations)


def test_an_implementable_issue_touching_a_forbidden_domain_is_blocked(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(title="Rotate the secret used by the billing invoice job")
    match = playbooks.match(document, registry, config)
    decision = replace(
        autonomy.classify(document, match, registry, config), tier="B", stop_conditions=[]
    )
    rules = {v.rule for v in guardrails.evaluate(document, match, decision, config)}
    assert {"SECRET_MODIFICATION", "MONEY_SEMANTICS"} <= rules


def test_every_violation_records_a_reason_evidence_and_a_human_action(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(environment_signal=True, remediable="CODE_CHANGE")
    match = playbooks.match(document, registry, config)
    decision = autonomy.classify(document, match, registry, config)
    for violation in guardrails.evaluate(document, match, decision, config):
        assert violation.stop_reason
        assert violation.evidence
        assert violation.required_human_action
        assert violation.forced_state in {State.BLOCKED.value, State.REJECTED.value}


def test_a_blocked_issue_plans_no_work(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored(environment_signal=True, remediable="CODE_CHANGE")
    match = playbooks.match(document, registry, config)
    decision = autonomy.classify(document, match, registry, config)
    violations = guardrails.evaluate(document, match, decision, config)
    result = planner.plan(document, match, decision, violations, config)
    assert result["proposed_action"].startswith("STOP")
    assert not result["execution_allowed"]
    assert result["stop_conditions"]


def test_a_plan_always_carries_tests_commands_and_a_rollback(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored()
    match = playbooks.match(document, registry, config)
    decision = autonomy.classify(document, match, registry, config)
    result = planner.plan(document, match, decision, [], config)
    assert result["test_plan"]
    assert result["verification_commands"]
    assert result["rollback_plan"]
    assert result["dry_run"] is True


def test_dev_fix_changes_nothing_and_says_so(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored()
    match = playbooks.match(document, registry, config)
    decision = autonomy.classify(document, match, registry, config)
    result = devfix.execute(document, planner.plan(document, match, decision, [], config), config)
    assert result["executed"] is False
    assert result["dry_run"] is True
    assert result["changed_files"] == []
    assert result["commit_sha"] is None
    assert result["pr_number"] is None
    assert result["external_systems_changed"] == []
    assert result["suppression_reasons"]
    assert result["would_have_done"]
    assert result["next_state"] == State.DEV_REVIEW.value


def test_dev_fix_refuses_to_execute_when_writes_are_not_permitted(config: Config) -> None:
    registry = playbooks.load_registry(config)
    document = scored()
    match = playbooks.match(document, registry, config)
    decision = autonomy.classify(document, match, registry, config)
    plan = {**planner.plan(document, match, decision, [], config), "execution_allowed": True}
    with pytest.raises(devfix.ExecutionSuppressed):
        devfix.execute(document, plan, config)
