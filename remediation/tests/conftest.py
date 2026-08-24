from __future__ import annotations

from pathlib import Path

import pytest

from remediation import config as config_module

REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"


@pytest.fixture
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture
def config(tmp_path: Path) -> config_module.Config:
    """Pilot configuration with artifacts redirected to a temporary directory."""
    return config_module.load(
        PROJECT_ROOT / "config" / "config.yaml",
        overrides={"artifact_root_directory": str(tmp_path / "artifacts")},
    )


@pytest.fixture
def report_directory(tmp_path: Path) -> Path:
    directory = tmp_path / "reports"
    directory.mkdir()
    return directory
