"""Week-over-week arithmetic over the rating cards.

Cards are grouped into the ISO weeks their review dates fall in, and consecutive
weeks are compared member by member. A week with no card is kept in the series as
an explicitly empty week: a missing week is a finding about the inputs, not a
gap to be smoothed over. A member who appears in only one of two weeks is
reported as joining or leaving the rated set rather than as a score change.
"""

from __future__ import annotations

import datetime as dt
import itertools
from dataclasses import dataclass

from . import dates
from .ratings import CardSet


@dataclass(frozen=True)
class Week:
    """One ISO week and the card sets whose review dates fall in it."""

    key: str
    monday: dt.date
    sunday: dt.date
    card_sets: tuple[CardSet, ...] = ()

    @property
    def covered(self) -> bool:
        return bool(self.card_sets)

    @property
    def latest(self) -> CardSet | None:
        """The week's most recent card set: the week's rating of record."""
        return self.card_sets[-1] if self.card_sets else None

    @property
    def review_dates(self) -> tuple[str, ...]:
        return tuple(card_set.date for card_set in self.card_sets)


@dataclass(frozen=True)
class Change:
    """One member's movement between two compared weeks."""

    member: str
    product: str | None
    previous: float | None
    current: float | None
    dimensions: dict[str, tuple[float | None, float | None]]

    @property
    def delta(self) -> float | None:
        if self.previous is None or self.current is None:
            return None
        return round(self.current - self.previous, 1)

    @property
    def status(self) -> str:
        if self.previous is None:
            return "NEW"
        if self.current is None:
            return "NOT_RATED"
        return "CHANGED"


@dataclass(frozen=True)
class Comparison:
    """Two adjacent weeks in the series, and every member movement between them."""

    earlier: Week
    later: Week
    changes: tuple[Change, ...]

    @property
    def comparable(self) -> bool:
        return self.earlier.covered and self.later.covered


def iso_week(report_date: str) -> str:
    """The ISO week key (``2026-W34``) a canonical report date falls in."""
    calendar = dates.to_date(report_date).isocalendar()
    return f"{calendar.year}-W{calendar.week:02d}"


def _monday(report_date: str) -> dt.date:
    day = dates.to_date(report_date)
    return day - dt.timedelta(days=day.isoweekday() - 1)


def _week(monday: dt.date, card_sets: tuple[CardSet, ...]) -> Week:
    calendar = monday.isocalendar()
    return Week(
        key=f"{calendar.year}-W{calendar.week:02d}",
        monday=monday,
        sunday=monday + dt.timedelta(days=6),
        card_sets=card_sets,
    )


def _grouped(card_sets: list[CardSet]) -> dict[dt.date, list[CardSet]]:
    grouped: dict[dt.date, list[CardSet]] = {}
    for card_set in sorted(card_sets, key=lambda item: item.date):
        grouped.setdefault(_monday(card_set.date), []).append(card_set)
    return grouped


def series(card_sets: list[CardSet], count: int) -> list[Week]:
    """The last ``count`` ISO weeks up to the newest card, empty weeks included."""
    grouped = _grouped(card_sets)
    if not grouped:
        return []
    newest = max(grouped)
    mondays = [newest - dt.timedelta(weeks=offset) for offset in reversed(range(count))]
    return [_week(monday, tuple(grouped.get(monday, ()))) for monday in mondays]


def _dimension_pairs(
    earlier: dict[str, float | None], later: dict[str, float | None]
) -> dict[str, tuple[float | None, float | None]]:
    names = list(dict.fromkeys([*earlier, *later]))
    return {name: (earlier.get(name), later.get(name)) for name in names}


def _change(member: str, earlier: CardSet | None, later: CardSet | None) -> Change:
    before = earlier.by_member().get(member) if earlier else None
    after = later.by_member().get(member) if later else None
    named = after or before
    return Change(
        member=named.member if named else member,
        product=(after.product if after else None) or (before.product if before else None),
        previous=before.overall if before else None,
        current=after.overall if after else None,
        dimensions=_dimension_pairs(before.scores if before else {}, after.scores if after else {}),
    )


def _members(earlier: CardSet | None, later: CardSet | None) -> list[str]:
    keys = list(later.by_member() if later else {})
    keys += [key for key in (earlier.by_member() if earlier else {}) if key not in keys]
    return keys


def compare(earlier: Week, later: Week) -> Comparison:
    """Every member movement from ``earlier``'s rating of record to ``later``'s."""
    before, after = earlier.latest, later.latest
    changes = [_change(member, before, after) for member in _members(before, after)]
    ordered = sorted(changes, key=lambda item: (item.delta is None, -(item.delta or 0.0)))
    return Comparison(earlier=earlier, later=later, changes=tuple(ordered))


def comparisons(weeks: list[Week]) -> list[Comparison]:
    """Each adjacent week pair in the series, oldest pair first."""
    return [compare(earlier, later) for earlier, later in itertools.pairwise(weeks)]


def within_week(week: Week) -> Comparison | None:
    """Movement between a week's own first and last review days, when it has two."""
    if len(week.card_sets) < 2:
        return None
    first = Week(key=week.key, monday=week.monday, sunday=week.sunday, card_sets=week.card_sets[:1])
    return compare(first, week)
