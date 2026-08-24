"""Runtime configuration.

Values resolve from, in order: explicit CLI argument, environment variable,
``config/config.yaml``, built-in default. Missing optional values stay explicitly
unset rather than being invented.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .scope import RepositoryScope

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent.parent
DEFAULT_CONFIG_FILE = PROJECT_ROOT / "config" / "config.yaml"


class ConfigError(ValueError):
    """Raised when configuration is present but unusable."""


@dataclass(frozen=True)
class RepoCommands:
    """Verification commands for one repository, as configured."""

    test: list[str] = field(default_factory=list)
    build: list[str] = field(default_factory=list)
    typecheck: list[str] = field(default_factory=list)
    static_analysis: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Config:
    mgmt_reports_repository: str
    mgmt_reports_directory: str
    mgmt_reports_branch: str | None
    artifact_root_directory: Path
    playbook_directory: Path
    general_playbook_registry: Path
    org_skill_registry: Path
    approval_mechanism: str
    dry_run_mode: bool
    remediation_repository_allowlist: tuple[str, ...]
    default_branches: dict[str, str]
    commands: dict[str, RepoCommands]
    max_complexity_for_autonomy: int
    min_playbook_confidence: int
    redact_employee_ratings: bool
    future_stages_enabled: dict[str, bool]
    repository_scope: RepositoryScope = field(default_factory=RepositoryScope)

    def stage_enabled(self, stage: str) -> bool:
        """Future stages are disabled unless explicitly turned on in config."""
        return bool(self.future_stages_enabled.get(stage, False))

    def commands_for(self, repository: str | None) -> RepoCommands:
        if repository is None:
            return RepoCommands()
        return self.commands.get(repository, RepoCommands())

    def default_branch_for(self, repository: str | None) -> str | None:
        if repository is None:
            return None
        return self.default_branches.get(repository)

    def remediation_allowed(self, repository: str | None) -> bool:
        """Whether the guardrail engine may permit writes to ``repository``."""
        if self.dry_run_mode or repository is None:
            return False
        return repository in self.remediation_repository_allowlist


def _as_bool(value: Any, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    lowered = str(value).strip().lower()
    if lowered in {"1", "true", "yes", "on"}:
        return True
    if lowered in {"0", "false", "no", "off"}:
        return False
    raise ConfigError(f"{value!r} is not a boolean")


def _resolve(root: Path, value: str | None, fallback: Path) -> Path:
    if not value:
        return fallback
    candidate = Path(value)
    return candidate if candidate.is_absolute() else root / candidate


def _repository_scope(raw: Any) -> RepositoryScope:
    """Build the pilot scope, falling back to the medicodio defaults."""
    if not raw:
        return RepositoryScope()
    if not isinstance(raw, dict):
        raise ConfigError("repository_scope must be a mapping")
    default = RepositoryScope()
    return RepositoryScope(
        repositories=tuple(raw.get("repositories") or default.repositories),
        prefixes=tuple(raw.get("prefixes") or default.prefixes),
        excluded=tuple(raw.get("excluded") or default.excluded),
    )


def _read_file(path: Path) -> dict[str, Any]:
    """The configuration file's contents, or nothing when it is absent."""
    if not path.exists():
        return {}
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(loaded, dict):
        raise ConfigError(f"{path} must contain a mapping")
    return loaded


def _merged(path: Path, overrides: dict[str, Any] | None) -> dict[str, Any]:
    """File settings with explicit overrides applied; ``None`` never overrides."""
    merged = dict(_read_file(path))
    stated = {key: value for key, value in (overrides or {}).items() if value is not None}
    merged.update(stated)
    return merged


def _repo_commands(spec: dict[str, Any]) -> RepoCommands:
    return RepoCommands(
        test=list(spec.get("test") or []),
        build=list(spec.get("build") or []),
        typecheck=list(spec.get("typecheck") or []),
        static_analysis=list(spec.get("static_analysis") or []),
    )


def _commands(merged: dict[str, Any]) -> dict[str, RepoCommands]:
    raw = merged.get("commands") or {}
    return {repo: _repo_commands(spec) for repo, spec in raw.items()}


def _future_stages(merged: dict[str, Any]) -> dict[str, bool]:
    raw = merged.get("future_stages_enabled") or {}
    return {str(stage): _as_bool(value, False) for stage, value in raw.items()}


def load(config_file: Path | None = None, overrides: dict[str, Any] | None = None) -> Config:
    """The effective configuration: file, then overrides, then environment defaults."""
    merged = _merged(config_file or DEFAULT_CONFIG_FILE, overrides)
    return _config(merged)


def _config(merged: dict[str, Any]) -> Config:
    def pick(key: str, env: str, default: Any = None) -> Any:
        if merged.get(key) is not None:
            return merged[key]
        return os.environ.get(env, default)

    return Config(
        mgmt_reports_repository=pick(
            "mgmt_reports_repository",
            "MGMT_REPORTS_REPOSITORY",
            "Medicodio-AI-Engine/Mgmt_Reports",
        ),
        mgmt_reports_directory=pick(
            "mgmt_reports_directory",
            "MGMT_REPORTS_DIRECTORY",
            "Ai_Engr_Rpt/Daily/medicodio/Detail",
        ),
        mgmt_reports_branch=pick("mgmt_reports_branch", "MGMT_REPORTS_BRANCH", None),
        artifact_root_directory=_resolve(
            PROJECT_ROOT.parent,
            pick("artifact_root_directory", "ARTIFACT_ROOT_DIRECTORY"),
            PROJECT_ROOT.parent / "Ai_Engr_Rpt" / "Daily" / "medicodio" / "Remediation",
        ),
        playbook_directory=_resolve(
            PROJECT_ROOT,
            pick("playbook_directory", "PLAYBOOK_DIRECTORY"),
            PROJECT_ROOT / "playbooks" / "org",
        ),
        general_playbook_registry=_resolve(
            PROJECT_ROOT,
            pick("general_playbook_registry", "GENERAL_PLAYBOOK_REGISTRY"),
            PROJECT_ROOT / "playbooks" / "general",
        ),
        org_skill_registry=_resolve(
            PROJECT_ROOT,
            pick("org_skill_registry", "ORG_SKILL_REGISTRY"),
            PROJECT_ROOT / "skills" / "registry.yaml",
        ),
        approval_mechanism=pick("approval_mechanism", "APPROVAL_MECHANISM", "FILE_DECISION_BLOCK"),
        dry_run_mode=_as_bool(pick("dry_run_mode", "DRY_RUN_MODE"), True),
        remediation_repository_allowlist=tuple(
            merged.get("remediation_repository_allowlist") or ()
        ),
        default_branches=dict(merged.get("default_branches") or {}),
        commands=_commands(merged),
        max_complexity_for_autonomy=int(merged.get("max_complexity_for_autonomy") or 4),
        min_playbook_confidence=int(merged.get("min_playbook_confidence") or 60),
        redact_employee_ratings=_as_bool(merged.get("redact_employee_ratings"), True),
        future_stages_enabled=_future_stages(merged),
        repository_scope=_repository_scope(merged.get("repository_scope")),
    )
