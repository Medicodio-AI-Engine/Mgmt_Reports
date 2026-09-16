"""Minimal markdown reader for the management reports.

Only what the pipeline needs: heading-scoped sections, pipe tables with their
source line numbers, and ordered-list items. Every parsed element keeps the line
number it came from so extracted findings can cite exact evidence.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*$")
TABLE_DIVIDER = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?$")
ORDERED_ITEM = re.compile(r"^\s*(\d+)[.)]\s+(.*)$")
BULLET_ITEM = re.compile(r"^\s*[-*]\s+(.*)$")


@dataclass(frozen=True)
class Row:
    """One table row, keyed by header cell."""

    line: int
    cells: dict[str, str]

    def get(self, *names: str) -> str | None:
        for name in names:
            for key, value in self.cells.items():
                if key.strip().lower() == name.strip().lower():
                    return value
        return None


@dataclass(frozen=True)
class Table:
    line: int
    headers: list[str]
    rows: list[Row]


@dataclass
class Section:
    level: int
    title: str
    line: int
    path: tuple[str, ...]
    lines: list[tuple[int, str]] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n".join(line for _, line in self.lines)

    def tables(self) -> list[Table]:
        return parse_tables(self.lines)

    def ordered_items(self) -> list[tuple[int, str]]:
        return [
            (number, match.group(2).strip())
            for number, line in self.lines
            if (match := ORDERED_ITEM.match(line))
        ]

    def bullets(self) -> list[tuple[int, str]]:
        return [
            (number, match.group(1).strip())
            for number, line in self.lines
            if (match := BULLET_ITEM.match(line))
        ]


def _split_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def _starts_table(lines: list[tuple[int, str]], index: int) -> bool:
    """A header row followed by a divider row opens a table."""
    _, line = lines[index]
    _, following = lines[index + 1]
    return "|" in line and bool(TABLE_DIVIDER.match(following.strip()))


def _row(number: int, line: str, headers: list[str]) -> Row | None:
    """One body row, padded to the header width, or ``None`` if it is not a row."""
    cells = _split_row(line)
    if len(cells) < 2:
        return None
    padded = cells + [""] * (len(headers) - len(cells))
    return Row(line=number, cells=dict(zip(headers, padded, strict=False)))


def _read_rows(
    lines: list[tuple[int, str]], start: int, headers: list[str]
) -> tuple[list[Row], int]:
    """Body rows from ``start``, and the index of the first line after the table."""
    rows: list[Row] = []
    cursor = start
    while cursor < len(lines) and "|" in lines[cursor][1]:
        row = _row(lines[cursor][0], lines[cursor][1], headers)
        if row is None:
            break
        rows.append(row)
        cursor += 1
    return rows, cursor


def _read_table(lines: list[tuple[int, str]], index: int) -> tuple[Table, int]:
    number, line = lines[index]
    headers = _split_row(line)
    rows, cursor = _read_rows(lines, index + 2, headers)
    return Table(line=number, headers=headers, rows=rows), cursor


def parse_tables(lines: list[tuple[int, str]]) -> list[Table]:
    """Every pipe table in the given numbered lines."""
    tables: list[Table] = []
    index = 0
    while index < len(lines) - 1:
        if not _starts_table(lines, index):
            index += 1
            continue
        table, index = _read_table(lines, index)
        tables.append(table)
    return tables


def _heading_path(stack: list[str], level: int, title: str) -> list[str]:
    """The heading stack after entering ``title``, padded for skipped levels."""
    trimmed = stack[: level - 1]
    trimmed += [""] * (level - 1 - len(trimmed))
    return [*trimmed, title]


def _heading(line: str) -> tuple[int, str] | None:
    match = HEADING.match(line)
    return (len(match.group(1)), match.group(2).strip()) if match else None


def _open_section(
    result: list[Section], stack: list[str], number: int, heading: tuple[int, str]
) -> list[str]:
    """Start a new section for one heading and return the updated heading stack."""
    level, title = heading
    updated = _heading_path(stack, level, title)
    result.append(Section(level=level, title=title, line=number, path=tuple(updated)))
    return updated


def sections(text: str) -> list[Section]:
    """Split a document into heading-scoped sections, preserving heading paths."""
    result = [Section(level=0, title="", line=0, path=())]
    stack: list[str] = []
    for number, line in enumerate(text.splitlines(), start=1):
        heading = _heading(line)
        if heading is None:
            result[-1].lines.append((number, line))
        else:
            stack = _open_section(result, stack, number, heading)
    return result


def find(all_sections: list[Section], title: str, *, level: int | None = None) -> list[Section]:
    lowered = title.lower()
    return [
        section
        for section in all_sections
        if section.title.lower() == lowered and (level is None or section.level == level)
    ]


def member_sections(all_sections: list[Section], member: str) -> list[Section]:
    """All sections nested under a member's top-level heading."""
    lowered = member.lower()
    return [
        section
        for section in all_sections
        if any(part.lower().startswith(lowered) for part in section.path[1:2])
    ]
