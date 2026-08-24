"""Controlled engineering remediation platform (Version 1).

Version 1 ingests the daily management reports, normalizes and prioritizes the
findings, matches approved playbooks, assigns an autonomy tier, plans eligible
work, and routes everything to human review. It stops at ``DEV_REVIEW``: QA, UAT,
and release contracts exist but are disabled, and the pilot runs in dry-run mode,
so no repository, commit, pull request, deployment, or external system is touched.
"""

from __future__ import annotations

__version__ = "1.0.0"

__all__ = ["__version__"]
