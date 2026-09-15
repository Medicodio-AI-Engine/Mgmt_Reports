"""Reading the employee rating cards as data.

The cards are written for people, not for machines: the summary grid's column
order changed between 2026-08-19 and 2026-08-23, dimensions can be ``NR``, and
the overall score is bolded. This module reads whichever grid a card carries and
returns the scores it actually states — nothing is inferred and nothing missing
is filled in.

This is the one place in the platform that keeps individual rating values. The
remediation pipeline never uses it: there, cards remain corroborating signal
with every value redacted. It exists for the supervisor rating-trend report,
which the report owner asked to show per-engineer scores.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from . import dates, markdown

DIMENSIONS = ("Delivery", "Rigor", "Review", "Devin", "Automation", "Consistency")
NUMBER = re.compile(r"\d+(?:\.\d+)?")
GRID_KEYS = ("Member", "Overall")
NOTE_MARKERS = ("scope:", "caveat", "limitation")
MAX_NOTES = 4
MAX_NOTE_CHARS = 400


@dataclass(frozen=True)
class Card:
    """One member's scores on one review date."""

    member: str
    product: str | None
    overall: float | None
    band: str | None
    scores: dict[str, float | None]


@dataclass(frozen=True)
class CardSet:
    """Every card stated by one rating-card file."""

    date: str
    path: Path
    cards: tuple[Card, ...]
    notes: tuple[str, ...] = ()

    def by_member(self) -> dict[str, Card]:
        return {card.member.lower(): card for card in self.cards}


def _number(cell: str | None) -> float | None:
    """The score a grid cell states; ``None`` for ``NR``, blank or prose."""
    if not cell:
        return None
    match = NUMBER.search(cell.replace("*", ""))
    return float(match.group()) if match else None


def _is_grid(table: markdown.Table) -> bool:
    """A summary grid names its members and gives each an overall score."""
    headers = [header.strip().lower() for header in table.headers]
    return all(any(key.lower() in header for header in headers) for key in GRID_KEYS)


def _dimension(row: markdown.Row, name: str) -> float | None:
    """One dimension's score, found by the header names the cards use."""
    return _number(row.get(name, f"{name} Score", f"{name} & Follow-Through"))


def _scores(row: markdown.Row) -> dict[str, float | None]:
    return {name: _dimension(row, name) for name in DIMENSIONS}


def _band(row: markdown.Row) -> str | None:
    band = row.get("Band")
    return band.strip() or None if band else None


def _card(row: markdown.Row) -> Card | None:
    """One grid row as a card, or ``None`` when the row names no member."""
    member = (row.get("Member") or "").strip()
    if not member or member.startswith("-") or member.startswith(":"):
        return None
    product = (row.get("Product") or "").strip() or None
    overall = _number(row.get("Overall", "Overall (1-10)"))
    return Card(
        member=member, product=product, overall=overall, band=_band(row), scores=_scores(row)
    )


def _grid_rows(text: str) -> list[markdown.Row]:
    """Rows of the first summary grid the document states."""
    for section in markdown.sections(text):
        for table in section.tables():
            if _is_grid(table):
                return table.rows
    return []


def _is_note(line: str) -> bool:
    """Whether a line is the card's own statement about its scope or limits."""
    lowered = line.lower()
    return line.startswith((">", "**Scope")) and any(mark in lowered for mark in NOTE_MARKERS)


def _notes(text: str) -> tuple[str, ...]:
    """The scope and caveat lines a card states about its own comparability."""
    found = [line.lstrip("> ").strip() for line in text.splitlines() if _is_note(line)]
    return tuple(note[:MAX_NOTE_CHARS] for note in found[:MAX_NOTES])


def read(path: Path) -> CardSet:
    """The cards one rating-card file states, keyed by its review date."""
    text = path.read_text(encoding="utf-8", errors="replace")
    date = dates.find_content_review_date(text) or dates.find_date(path.name) or ""
    found = [_card(row) for row in _grid_rows(text)]
    cards = tuple(card for card in found if card is not None)
    return CardSet(date=date, path=path, cards=cards, notes=_notes(text))


def _is_card_file(path: Path) -> bool:
    return path.suffix.lower() == ".md" and "rating-card" in path.name.lower().replace("_", "-")


def read_all(directory: Path) -> list[CardSet]:
    """Every rating-card file in ``directory``, oldest review date first."""
    found = [read(path) for path in sorted(directory.glob("*.md")) if _is_card_file(path)]
    return sorted((card_set for card_set in found if card_set.date), key=lambda item: item.date)
