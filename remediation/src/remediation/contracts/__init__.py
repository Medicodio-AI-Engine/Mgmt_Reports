"""Future-stage contracts.

Stages 06_QA through 09_LEARNING have stable, validated interfaces so later
versions can implement them without changing upstream stages. They are disabled
in Version 1: calling one without explicitly enabling it raises
``StageDisabledError``. Nothing is promoted into QA, UAT, or production here.
"""

from __future__ import annotations


class StageDisabledError(RuntimeError):
    """Raised when a disabled future stage is invoked."""


def require_enabled(stage: str, enabled: bool) -> None:
    if not enabled:
        raise StageDisabledError(
            f"{stage} is defined but disabled in Version 1; enabling it requires an explicit "
            "configuration change and human approval"
        )


__all__ = ["StageDisabledError", "require_enabled"]
