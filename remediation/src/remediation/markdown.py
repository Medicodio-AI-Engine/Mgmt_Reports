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


def parse_tables(lines: list[tuple[int, str]]) -> list[Table]:
    tables: list[Table] = []
    index = 0
    while index < len(lines) - 1:
        number, line = lines[index]
        _, following = lines[index + 1]
        if "|" in line and TABLE_DIVIDER.match(following.strip()):
            headers = _split_row(line)
            rows: list[Row] = []
            cursor = index + 2
            while cursor < len(lines) and "|" in lines[cursor][1]:
                row_number, row_line = lines[cursor]
                cells = _split_row(row_line)
                if len(cells) < 2:
                    break
                padded = cells + [""] * (len(headers) - len(cells))
                rows.append(Row(line=row_number, cells=dict(zip(headers, padded, strict=False))))
                cursor += 1
            tables.append(Table(line=number, headers=headers, rows=rows))
            index = cursor
            continue
        index += 1
    return tables


def sections(text: str) -> list[Section]:
    """Split a document into heading-scoped sections, preserving heading paths."""
    result: list[Section] = []
    stack: list[str] = []
    current = Section(level=0, title="", line=0, path=())
    result.append(current)
    for number, line in enumerate(text.splitlines(), start=1):
        match = HEADING.match(line)
        if not match:
            current.lines.append((number, line))
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        stack = stack[: level - 1]
        while len(stack) < level - 1:
            stack.append("")
        stack.append(title)
        current = Section(level=level, title=title, line=number, path=tuple(stack))
        result.append(current)
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
