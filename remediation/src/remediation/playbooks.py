"""Playbook registry, matching, and capability resolution.

Lookup precedence, highest first:

1. organization playbook
2. organization skill/capability match
3. previously successful organizational remediation pattern (learning store)
4. approved general playbook
5. no match -> escalate

An organization playbook always wins over a general playbook that scores higher;
generic guidance never overrides organization guidance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Any

import yaml

from .config import Config


class Precedence(IntEnum):
    ORG_PLAYBOOK = 1
    ORG_SKILL = 2
    LEARNED_PATTERN = 3
    GENERAL_PLAYBOOK = 4
    NO_MATCH = 5


@dataclass(frozen=True)
class Playbook:
    playbook_id: str
    name: str
    scope: str
    version: int
    applies_to_categories: tuple[str, ...]
    match_keywords: tuple[str, ...]
    exclude_keywords: tuple[str, ...]
    required_skills: tuple[str, ...]
    default_autonomy_tier: str
    max_complexity: int
    allowed_security_scopes: tuple[str, ...]
    requires_reproduction: bool
    requires_failing_test_first: bool
    steps: tuple[str, ...]
    guardrails: tuple[str, ...]
    stop_conditions: tuple[str, ...]
    review_checklist: tuple[str, ...]
    source_path: str

    @property
    def precedence(self) -> Precedence:
        return Precedence.ORG_PLAYBOOK if self.scope == "ORG" else Precedence.GENERAL_PLAYBOOK


@dataclass(frozen=True)
class Skill:
    skill_id: str
    description: str
    available: bool
    unavailable_reason: str | None


@dataclass
class Match:
    playbook: Playbook | None
    precedence: Precedence
    confidence: int
    matched_on: list[str] = field(default_factory=list)
    rejected: list[str] = field(default_factory=list)
    skills_required: list[str] = field(default_factory=list)
    skills_available: list[str] = field(default_factory=list)
    missing_skills: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "playbook_id": self.playbook.playbook_id if self.playbook else None,
            "playbook_name": self.playbook.name if self.playbook else None,
            "playbook_scope": self.playbook.scope if self.playbook else None,
            "playbook_version": self.playbook.version if self.playbook else None,
            "source": self.precedence.name,
            "confidence": self.confidence,
            "matched_on": self.matched_on,
            "rejected_candidates": self.rejected,
        }


class PlaybookError(RuntimeError):
    """Raised when the playbook or skill registry cannot be loaded."""


_REQUIRED_KEYS = ("playbook_id", "name", "scope", "applies_to_categories")


def _load_playbook(path: Path) -> Playbook:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise PlaybookError(f"{path} must contain a mapping")
    missing = [key for key in _REQUIRED_KEYS if not raw.get(key)]
    if missing:
        raise PlaybookError(f"{path} is missing required keys: {', '.join(missing)}")
    scope = str(raw["scope"]).upper()
    if scope not in {"ORG", "GENERAL"}:
        raise PlaybookError(f"{path} has unsupported scope {scope!r}")
    return Playbook(
        playbook_id=str(raw["playbook_id"]),
        name=str(raw["name"]),
        scope=scope,
        version=int(raw.get("version") or 1),
        applies_to_categories=tuple(raw.get("applies_to_categories") or ()),
        match_keywords=tuple(str(k).lower() for k in raw.get("match_keywords") or ()),
        exclude_keywords=tuple(str(k).lower() for k in raw.get("exclude_keywords") or ()),
        required_skills=tuple(raw.get("required_skills") or ()),
        default_autonomy_tier=str(raw.get("default_autonomy_tier") or "C").upper(),
        max_complexity=int(raw.get("max_complexity") or 10),
        allowed_security_scopes=tuple(raw.get("allowed_security_scopes") or ("NONE",)),
        requires_reproduction=bool(raw.get("requires_reproduction")),
        requires_failing_test_first=bool(raw.get("requires_failing_test_first")),
        steps=tuple(raw.get("steps") or ()),
        guardrails=tuple(raw.get("guardrails") or ()),
        stop_conditions=tuple(raw.get("stop_conditions") or ()),
        review_checklist=tuple(raw.get("review_checklist") or ()),
        source_path=str(path),
    )


@dataclass
class Registry:
    org: list[Playbook]
    general: list[Playbook]
    skills: dict[str, Skill]
    learned: dict[str, str]

    @property
    def all(self) -> list[Playbook]:
        return [*self.org, *self.general]

    def get(self, playbook_id: str) -> Playbook | None:
        return next((p for p in self.all if p.playbook_id == playbook_id), None)


def _load_directory(directory: Path) -> list[Playbook]:
    """Every playbook declared in one scope directory."""
    if not directory.is_dir():
        return []
    paths = sorted(directory.iterdir())
    return [_load_playbook(path) for path in paths if path.suffix in {".yaml", ".yml"}]


def _skill(entry: dict[str, Any]) -> Skill:
    return Skill(
        skill_id=str(entry["id"]),
        description=str(entry.get("description") or ""),
        available=bool(entry.get("available")),
        unavailable_reason=entry.get("unavailable_reason"),
    )


def _load_skills(path: Path) -> dict[str, Skill]:
    """The declared capability registry; absent means no capabilities are claimed."""
    if not path.exists():
        return {}
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(entry["id"]): _skill(entry) for entry in raw.get("skills") or []}


def _reject_duplicate_ids(org: list[Playbook], general: list[Playbook]) -> None:
    """One id must name one playbook, or precedence would be ambiguous."""
    duplicates = {p.playbook_id for p in org} & {p.playbook_id for p in general}
    if duplicates:
        raise PlaybookError(f"playbook id declared in both scopes: {', '.join(sorted(duplicates))}")


def load_registry(config: Config, learned: dict[str, str] | None = None) -> Registry:
    """Load org and general playbooks plus the declared capability registry."""
    org = _load_directory(config.playbook_directory)
    general = _load_directory(config.general_playbook_registry)
    _reject_duplicate_ids(org, general)
    skills = _load_skills(config.org_skill_registry)
    return Registry(org=org, general=general, skills=skills, learned=dict(learned or {}))


def _issue_text(issue: dict[str, Any]) -> str:
    parts = [
        issue.get("title") or "",
        issue.get("description") or "",
        issue.get("recommended_action") or "",
        " ".join(issue.get("files") or []),
    ]
    return " ".join(parts).lower()


def _keyword_hits(playbook: Playbook, text: str) -> list[str]:
    return [keyword for keyword in playbook.match_keywords if keyword in text]


def _matched_on(playbook: Playbook, issue: dict[str, Any], hits: list[str]) -> list[str]:
    matched = []
    if issue.get("category") in playbook.applies_to_categories:
        matched.append(f"category {issue['category']}")
    if hits:
        matched.append("keywords: " + ", ".join(hits[:5]))
    return matched


def _excluded_reason(playbook: Playbook, text: str) -> str | None:
    excluded = [keyword for keyword in playbook.exclude_keywords if keyword in text]
    return "excluded by keywords: " + ", ".join(excluded) if excluded else None


def _scope_reason(playbook: Playbook, issue: dict[str, Any]) -> str | None:
    scope = issue.get("security_scope") or "UNKNOWN"
    if scope in playbook.allowed_security_scopes:
        return None
    return f"security scope {scope} not allowed by playbook"


def _complexity_reason(playbook: Playbook, issue: dict[str, Any]) -> str | None:
    complexity = (issue.get("complexity") or {}).get("score")
    if not isinstance(complexity, int) or complexity <= playbook.max_complexity:
        return None
    return f"complexity {complexity} exceeds playbook maximum {playbook.max_complexity}"


def _blocking(playbook: Playbook, issue: dict[str, Any], text: str) -> list[str]:
    """Every reason this playbook may not be used for this issue."""
    reasons = (
        _excluded_reason(playbook, text),
        _scope_reason(playbook, issue),
        _complexity_reason(playbook, issue),
    )
    return [reason for reason in reasons if reason]


def _confidence(playbook: Playbook, issue: dict[str, Any], hits: list[str]) -> int:
    """A declared category alone clears the minimum; keywords and org scope strengthen it."""
    score = 60 if issue.get("category") in playbook.applies_to_categories else 0
    score += min(35, 12 * len(hits))
    score += 5 if playbook.scope == "ORG" else 0
    return min(score, 100)


def _score(playbook: Playbook, issue: dict[str, Any]) -> tuple[int, list[str], list[str]]:
    """Return (confidence 0-100, matched_on, blocking_reasons)."""
    text = _issue_text(issue)
    hits = _keyword_hits(playbook, text)
    return (
        _confidence(playbook, issue, hits),
        _matched_on(playbook, issue, hits),
        _blocking(playbook, issue, text),
    )


Candidate = tuple[int, Playbook, list[str]]


def _rejection(playbook: Playbook, confidence: int, blocking: list[str], floor: int) -> str | None:
    """Why this playbook was not usable, when it is worth telling a reviewer."""
    if blocking:
        return f"{playbook.playbook_id}: " + "; ".join(blocking)
    if confidence < floor and confidence > 0:
        return f"{playbook.playbook_id}: confidence {confidence} below {floor}"
    return None


def _candidate(
    playbook: Playbook, issue: dict[str, Any], floor: int, rejected: list[str]
) -> Candidate | None:
    """One playbook's usable candidacy; its rejection reason is recorded either way."""
    confidence, matched, blocking = _score(playbook, issue)
    reason = _rejection(playbook, confidence, blocking, floor)
    if reason:
        rejected.append(reason)
    if blocking or confidence < floor:
        return None
    return (confidence, playbook, matched)


def _best_in_group(
    group: list[Playbook], issue: dict[str, Any], floor: int, rejected: list[str]
) -> Candidate | None:
    """Highest-confidence usable playbook in one scope; records why others failed."""
    scored = [_candidate(playbook, issue, floor, rejected) for playbook in group]
    usable = [candidate for candidate in scored if candidate is not None]
    return max(usable, key=lambda candidate: candidate[0]) if usable else None


def _precedence_for(
    playbook: Playbook, issue: dict[str, Any], registry: Registry, scope: Precedence
) -> Precedence:
    """A learned pattern is credited as such when it selected this playbook."""
    learned = registry.learned.get(issue.get("dedupe_signature", ""))
    return Precedence.LEARNED_PATTERN if learned == playbook.playbook_id else scope


def _no_match(rejected: list[str]) -> Match:
    return Match(
        playbook=None,
        precedence=Precedence.NO_MATCH,
        confidence=0,
        matched_on=[],
        rejected=rejected,
        skills_required=[],
        skills_available=[],
        missing_skills=[],
    )


def _matched(candidate: Candidate, precedence: Precedence, rejected: list[str]) -> Match:
    confidence, playbook, matched_on = candidate
    return Match(
        playbook=playbook,
        precedence=precedence,
        confidence=confidence,
        matched_on=matched_on,
        rejected=rejected,
    )


def match(issue: dict[str, Any], registry: Registry, config: Config) -> Match:
    """Match one scored issue against the registry, honoring scope precedence.

    Organization scope is resolved first and never falls through to general guidance.
    """
    rejected: list[str] = []
    groups = (
        (registry.org, Precedence.ORG_PLAYBOOK),
        (registry.general, Precedence.GENERAL_PLAYBOOK),
    )
    for group, scope in groups:
        best = _best_in_group(group, issue, config.min_playbook_confidence, rejected)
        if best is None:
            continue
        precedence = _precedence_for(best[1], issue, registry, scope)
        return _with_skills(_matched(best, precedence, rejected), registry)
    return _no_match(rejected)


def _with_skills(result: Match, registry: Registry) -> Match:
    required = list(result.playbook.required_skills) if result.playbook else []
    available = [
        skill_id
        for skill_id in required
        if skill_id in registry.skills and registry.skills[skill_id].available
    ]
    result.skills_required = required
    result.skills_available = available
    result.missing_skills = [skill_id for skill_id in required if skill_id not in available]
    return result


def missing_skill_reasons(missing: list[str], registry: Registry) -> list[str]:
    reasons: list[str] = []
    for skill_id in missing:
        skill = registry.skills.get(skill_id)
        if skill is None:
            reasons.append(f"{skill_id}: not present in the capability registry")
        else:
            reasons.append(f"{skill_id}: {skill.unavailable_reason or 'marked unavailable'}")
    return reasons
