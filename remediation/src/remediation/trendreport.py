"""The supervisor's week-over-week rating report.

One document: which weeks the repository actually has cards for, how each rated
person moved from one week's rating of record to the next, and the dimension
scores behind each movement. Weeks with no card are printed as missing, and a
person rated in only one of two weeks is printed as joining or leaving the rated
set — neither is turned into a score.

Per-engineer values appear here by explicit instruction from the report owner.
The remediation artifacts remain redacted; this file does not change that.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from . import dates
from .ratings import DIMENSIONS, Card, CardSet
from .trend import Change, Comparison, Week, comparisons, within_week

NOT_RATED_NOTE = (
    "`NR` in a Current column means the later card carries no entry for that person — a card "
    "scopes itself to the contributors with observable activity on its review day — so it is an "
    "absence of evidence, not a fall in rating. Only `CHANGED` rows are movements."
)
MIN_ALIAS_PREFIX = 5

CONFIDENTIAL = (
    "**Confidential — individual performance data.** Per-engineer rating values are reproduced "
    "here at the report owner's explicit request. They are ratings of observable activity on "
    "single review days, not appraisals, and they are not evidence of any software defect."
)


@dataclass(frozen=True)
class Report:
    """The rendered report and the data it was rendered from."""

    markdown: str
    data: dict[str, object]


def _pretty(report_date: str) -> str:
    return report_date.replace("_", "-")


def _score(value: float | None) -> str:
    if value is None:
        return "NR"
    return f"{value:g}"


def _delta(change: Change) -> str:
    if change.delta is None:
        return "—"
    return f"{change.delta:+g}" if change.delta else "0"


def _row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def _table(headers: list[str], rows: list[list[str]]) -> list[str]:
    divider = ["---"] * len(headers)
    return [_row(headers), _row(divider), *[_row(row) for row in rows]]


def _coverage_row(week: Week) -> list[str]:
    dates_found = ", ".join(_pretty(date) for date in week.review_dates) or "—"
    status = "covered" if week.covered else "**no rating card in the repository**"
    cards = sum(len(card_set.cards) for card_set in week.card_sets)
    return [week.key, f"{week.monday} → {week.sunday}", dates_found, str(cards), status]


def _coverage(weeks: list[Week]) -> list[str]:
    headers = ["ISO week", "Week range (UTC)", "Review dates found", "Members rated", "Status"]
    rows = [_coverage_row(week) for week in weeks]
    missing = [week.key for week in weeks if not week.covered]
    lines = ["## Coverage", "", *_table(headers, rows), ""]
    if missing:
        lines += [f"Weeks without any rating card: {', '.join(missing)}.", ""]
    return lines


def _movement_row(change: Change) -> list[str]:
    return [
        change.member,
        change.product or "—",
        _score(change.previous),
        _score(change.current),
        _delta(change),
        change.status,
    ]


def _dimension_row(change: Change) -> list[str]:
    cells = [change.member]
    for name in DIMENSIONS:
        before, after = change.dimensions.get(name, (None, None))
        cells.append(f"{_score(before)} → {_score(after)}")
    return cells


def _shares_prefix(first: str, second: str) -> bool:
    prefix = min(len(first), len(second), MIN_ALIAS_PREFIX)
    return prefix >= MIN_ALIAS_PREFIX and first[:prefix].lower() == second[:prefix].lower()


def _alias_pairs(comparison: Comparison) -> list[str]:
    """Names that may belong to one person, so a supervisor can confirm or reject."""
    new = [change.member for change in comparison.changes if change.status == "NEW"]
    gone = [change.member for change in comparison.changes if change.status == "NOT_RATED"]
    return [f"`{a}` / `{b}`" for a in new for b in gone if _shares_prefix(a, b)]


def _alias_note(comparison: Comparison) -> list[str]:
    pairs = _alias_pairs(comparison)
    if not pairs:
        return []
    joined = "; ".join(pairs)
    return [
        f"Possibly the same person under two account names, unverified: {joined}. "
        "They are kept as separate rows until someone confirms the mapping.",
        "",
    ]


def _movement_tables(comparison: Comparison) -> list[str]:
    headers = ["Member", "Product", "Previous", "Current", "Δ", "Status"]
    rows = [_movement_row(change) for change in comparison.changes]
    dimensions = [_dimension_row(change) for change in comparison.changes]
    return [
        *_table(headers, rows),
        "",
        *_alias_note(comparison),
        "Dimension movement (previous → current):",
        "",
        *_table(["Member", *DIMENSIONS], dimensions),
        "",
    ]


def _pair_title(comparison: Comparison) -> str:
    return f"### {comparison.earlier.key} → {comparison.later.key}"


def _uncomparable(comparison: Comparison) -> list[str]:
    absent = [week.key for week in (comparison.earlier, comparison.later) if not week.covered]
    return [
        _pair_title(comparison),
        "",
        f"Not comparable: no rating card exists for {', '.join(absent)}.",
        "",
    ]


def _pair(comparison: Comparison) -> list[str]:
    if not comparison.comparable:
        return _uncomparable(comparison)
    earlier = _pretty(comparison.earlier.latest.date) if comparison.earlier.latest else "—"
    later = _pretty(comparison.later.latest.date) if comparison.later.latest else "—"
    lines = [_pair_title(comparison), "", f"Ratings of record: {earlier} versus {later}.", ""]
    return [*lines, *_movement_tables(comparison)]


def _week_over_week(weeks: list[Week]) -> list[str]:
    lines = ["## Week-over-week movement", ""]
    for comparison in comparisons(weeks):
        lines += _pair(comparison)
    return lines


def _within(weeks: list[Week]) -> list[str]:
    """Day-over-day movement inside a week that holds more than one card."""
    lines: list[str] = []
    for week in weeks:
        comparison = within_week(week)
        if comparison is None:
            continue
        first = _pretty(week.review_dates[0])
        last = _pretty(week.review_dates[-1])
        lines += [f"### {week.key}: {first} → {last} (same week)", ""]
        lines += _movement_tables(comparison)
    return ["## Within-week movement", "", *lines] if lines else []


def _card_notes(card_set: CardSet) -> list[str]:
    return [f"- {_pretty(card_set.date)}: {note}" for note in card_set.notes]


def _caveats(weeks: list[Week]) -> list[str]:
    """What the cards themselves say about being compared."""
    stated = [line for week in weeks for cs in week.card_sets for line in _card_notes(cs)]
    lines = ["## Comparability", "", NOT_RATED_NOTE, ""]
    if stated:
        lines += ["Each card's own scope and caveats:", "", *stated, ""]
    return lines


def _card_row(card: Card) -> list[str]:
    scores = [_score(card.scores.get(name)) for name in DIMENSIONS]
    return [card.member, card.product or "—", _score(card.overall), card.band or "—", *scores]


def _card_set(card_set: CardSet) -> list[str]:
    headers = ["Member", "Product", "Overall", "Band", *DIMENSIONS]
    rows = [_card_row(card) for card in card_set.cards]
    return [f"### {_pretty(card_set.date)} — {card_set.path.name}", "", *_table(headers, rows), ""]


def _ratings_of_record(weeks: list[Week]) -> list[str]:
    lines = ["## Scores as stated by each card", ""]
    for week in weeks:
        for card_set in week.card_sets:
            lines += _card_set(card_set)
    return lines


def _header(weeks: list[Week], generated: str) -> list[str]:
    covered = sum(1 for week in weeks if week.covered)
    span = f"{weeks[0].key} → {weeks[-1].key}" if weeks else "no weeks"
    return [
        f"# Employee Rating Trend — {len(weeks)} weeks ({span})",
        "",
        f"**Generated:** {_pretty(generated)} UTC · **Weeks requested:** {len(weeks)} · "
        f"**Weeks with data:** {covered}",
        "",
        CONFIDENTIAL,
        "",
    ]


def _change_data(change: Change) -> dict[str, object]:
    return {
        "member": change.member,
        "product": change.product,
        "previous_overall": change.previous,
        "current_overall": change.current,
        "delta": change.delta,
        "status": change.status,
        "dimensions": {name: list(pair) for name, pair in change.dimensions.items()},
    }


def _comparison_data(comparison: Comparison) -> dict[str, object]:
    return {
        "earlier_week": comparison.earlier.key,
        "later_week": comparison.later.key,
        "comparable": comparison.comparable,
        "changes": [_change_data(change) for change in comparison.changes],
    }


def _week_data(week: Week) -> dict[str, object]:
    return {
        "week": week.key,
        "monday": str(week.monday),
        "sunday": str(week.sunday),
        "covered": week.covered,
        "review_dates": [_pretty(date) for date in week.review_dates],
        "members_rated": sum(len(card_set.cards) for card_set in week.card_sets),
    }


def _data(weeks: list[Week], generated: str) -> dict[str, object]:
    return {
        "generated": _pretty(generated),
        "weeks_requested": len(weeks),
        "weeks": [_week_data(week) for week in weeks],
        "missing_weeks": [week.key for week in weeks if not week.covered],
        "comparisons": [_comparison_data(item) for item in comparisons(weeks)],
    }


def render(weeks: list[Week], generated: str | None = None) -> Report:
    """The rating-trend report for a week series, plus its machine-readable form."""
    stamp = generated or dates.today()
    lines = [
        *_header(weeks, stamp),
        *_coverage(weeks),
        *_caveats(weeks),
        *_week_over_week(weeks),
        *_within(weeks),
        *_ratings_of_record(weeks),
    ]
    return Report(markdown="\n".join(lines).rstrip() + "\n", data=_data(weeks, stamp))


def write(report: Report, directory: Path, stem: str) -> list[Path]:
    """Write the report and its data beside the other management reports."""
    directory.mkdir(parents=True, exist_ok=True)
    document = directory / f"{stem}.md"
    data = directory / f"{stem}.json"
    document.write_text(report.markdown, encoding="utf-8")
    data.write_text(json.dumps(report.data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return [document, data]
