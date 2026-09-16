"""Account names that a human has confirmed belong to one person.

A person can appear under more than one account across review days, which would
otherwise read as one person leaving the rated set and another joining it. The
mapping is committed, not inferred: the rating report flags a resemblance, and
only a confirmed entry here merges two names. Nothing else about a card changes —
the scores stay exactly as the card stated them.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .config import PROJECT_ROOT

DEFAULT_IDENTITY_FILE = PROJECT_ROOT / "config" / "rating_identities.yaml"


def _pairs(raw: object) -> dict[str, str]:
    if not isinstance(raw, dict):
        return {}
    stated = raw.get("identities") if "identities" in raw else raw
    if not isinstance(stated, dict):
        return {}
    return {str(alias).lower(): str(name) for alias, name in stated.items() if name}


def load(path: Path | None = None) -> dict[str, str]:
    """The confirmed alias-to-person mapping; empty when the file is absent."""
    source = path or DEFAULT_IDENTITY_FILE
    if not source.exists():
        return {}
    return _pairs(yaml.safe_load(source.read_text(encoding="utf-8")))


def canonical(member: str, mapping: dict[str, str]) -> str:
    """The person's name for an account name, or the account name itself."""
    return mapping.get(member.strip().lower(), member)
