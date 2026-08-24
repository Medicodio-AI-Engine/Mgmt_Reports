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


def load_registry(config: Config, learned: dict[str, str] | None = None) -> Registry:
    def load_dir(directory: Path) -> list[Playbook]:
        if not directory.is_dir():
            return []
        return [
            _load_playbook(path)
            for path in sorted(directory.iterdir())
            if path.suffix in {".yaml", ".yml"}
        ]

    skills: dict[str, Skill] = {}
    if config.org_skill_registry.exists():
        raw = yaml.safe_load(config.org_skill_registry.read_text(encoding="utf-8")) or {}
        for entry in raw.get("skills") or []:
            skills[str(entry["id"])] = Skill(
                skill_id=str(entry["id"]),
                description=str(entry.get("description") or ""),
                available=bool(entry.get("available")),
                unavailable_reason=entry.get("unavailable_reason"),
            )

    org = load_dir(config.playbook_directory)
    general = load_dir(config.general_playbook_registry)
    duplicates = {p.playbook_id for p in org} & {p.playbook_id for p in general}
    if duplicates:
        raise PlaybookError(f"playbook id declared in both scopes: {', '.join(sorted(duplicates))}")
    return Registry(org=org, general=general, skills=skills, learned=dict(learned or {}))


def _issue_text(issue: dict[str, Any]) -> str:
    parts = [
        issue.get("title") or "",
        issue.get("description") or "",
        issue.get("recommended_action") or "",
        " ".join(issue.get("files") or []),
    ]
    return " ".join(parts).lower()


def _score(playbook: Playbook, issue: dict[str, Any]) -> tuple[int, list[str], list[str]]:
    """Return (confidence 0-100, matched_on, blocking_reasons)."""
    matched: list[str] = []
    blocking: list[str] = []
    text = _issue_text(issue)

    category = issue.get("category")
    if category in playbook.applies_to_categories:
        matched.append(f"category {category}")
    hits = [keyword for keyword in playbook.match_keywords if keyword in text]
    if hits:
        matched.append("keywords: " + ", ".join(hits[:5]))
    excluded = [keyword for keyword in playbook.exclude_keywords if keyword in text]
    if excluded:
        blocking.append("excluded by keywords: " + ", ".join(excluded))

    scope = issue.get("security_scope") or "UNKNOWN"
    if scope not in playbook.allowed_security_scopes:
        blocking.append(f"security scope {scope} not allowed by playbook")

    complexity = (issue.get("complexity") or {}).get("score")
    if isinstance(complexity, int) and complexity > playbook.max_complexity:
        blocking.append(
            f"complexity {complexity} exceeds playbook maximum {playbook.max_complexity}"
        )

    confidence = 0
    if category in playbook.applies_to_categories:
        # A declared category is on its own enough to clear min_playbook_confidence;
        # keyword hits and org scope only strengthen an already-valid match.
        confidence += 60
    confidence += min(35, 12 * len(hits))
    if playbook.scope == "ORG":
        confidence += 5
    return min(confidence, 100), matched, blocking


def match(issue: dict[str, Any], registry: Registry, config: Config) -> Match:
    """Match one scored issue against the registry, honoring scope precedence."""
    rejected: list[str] = []
    best: tuple[int, Playbook, list[str]] | None = None

    for group, precedence in (
        (registry.org, Precedence.ORG_PLAYBOOK),
        (registry.general, Precedence.GENERAL_PLAYBOOK),
    ):
        for playbook in group:
            confidence, matched, blocking = _score(playbook, issue)
            if blocking:
                rejected.append(f"{playbook.playbook_id}: " + "; ".join(blocking))
                continue
            if confidence < config.min_playbook_confidence:
                if confidence > 0:
                    rejected.append(
                        f"{playbook.playbook_id}: confidence {confidence} below "
                        f"{config.min_playbook_confidence}"
                    )
                continue
            if best is None or confidence > best[0]:
                best = (confidence, playbook, matched)
        if best is not None:
            # Organization scope resolved; never fall through to general guidance.
            confidence, playbook, matched = best
            learned = registry.learned.get(issue.get("dedupe_signature", ""))
            resolved = (
                Precedence.LEARNED_PATTERN
                if learned and learned == playbook.playbook_id
                else precedence
            )
            return _with_skills(
                Match(
                    playbook=playbook,
                    precedence=resolved,
                    confidence=confidence,
                    matched_on=matched,
                    rejected=rejected,
                ),
                registry,
            )

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
