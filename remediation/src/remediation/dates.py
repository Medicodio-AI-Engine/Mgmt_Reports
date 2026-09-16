"""Report-date normalization.

The canonical report-date key is ``YYYY_MM_DD``. Filenames in this repository
use ``YYYY-MM-DD`` and report bodies may write the date in either form, so every
date that enters the pipeline is normalized before it is used as a grouping key.
"""

from __future__ import annotations

import datetime as dt
import re

CANONICAL = "%Y_%m_%d"

_DATE_PATTERNS = (
    re.compile(r"(?P<y>\d{4})[-_/.](?P<m>\d{2})[-_/.](?P<d>\d{2})"),
    re.compile(r"(?P<y>\d{4})(?P<m>\d{2})(?P<d>\d{2})"),
)

#: Lines such as "**Review date:** 2026-08-23 (Sunday, UTC)" or "Review day: 2026-08-19".
_CONTENT_DATE_LABEL = re.compile(
    r"review\s*(?:date|day)\W{0,4}\s*(?P<date>\d{4}[-_/.]?\d{2}[-_/.]?\d{2})",
    re.IGNORECASE,
)


class DateNormalizationError(ValueError):
    """Raised when a string does not contain a usable date."""


def normalize(value: str) -> str:
    """Normalize any supported date representation to ``YYYY_MM_DD``."""
    found = find_date(value)
    if found is None:
        raise DateNormalizationError(f"no date found in {value!r}")
    return found


def find_date(value: str) -> str | None:
    """Return the first date in ``value`` as ``YYYY_MM_DD``, or ``None``."""
    for pattern in _DATE_PATTERNS:
        match = pattern.search(value)
        if match is None:
            continue
        try:
            parsed = dt.date(int(match.group("y")), int(match.group("m")), int(match.group("d")))
        except ValueError:
            continue
        return parsed.strftime(CANONICAL)
    return None


def find_content_review_date(text: str) -> str | None:
    """Extract the review date a report states in its own body."""
    match = _CONTENT_DATE_LABEL.search(text)
    if match is None:
        return None
    return find_date(match.group("date"))


def to_date(report_date: str) -> dt.date:
    return dt.datetime.strptime(report_date, CANONICAL).date()


def today(clock: dt.datetime | None = None) -> str:
    now = clock or dt.datetime.now(dt.UTC)
    return now.strftime(CANONICAL)
