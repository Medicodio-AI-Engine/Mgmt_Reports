"""The pilot looks at medicodio libraries and the management repository only."""

from __future__ import annotations

from remediation import config as config_module
from remediation import scope


def test_medicodio_libraries_are_in_scope() -> None:
    default = scope.RepositoryScope()
    for repository in ("medicodio-nextgen-app-react", "nextgen-codio-engine", "Mgmt_Reports"):
        assert scope.classify(default, repository) == scope.IN_SCOPE


def test_prefix_match_covers_unlisted_medicodio_libraries() -> None:
    assert scope.classify(scope.RepositoryScope(), "medicodio-billing-lib") == scope.IN_SCOPE


def test_owner_prefixed_name_is_resolved() -> None:
    result = scope.classify(scope.RepositoryScope(), "Medicodio-AI-Engine/medicodio-paperclip")
    assert result == scope.IN_SCOPE


def test_excluded_repositories_are_out_of_scope() -> None:
    default = scope.RepositoryScope()
    for repository in ("globalcodio-monorepo", "paperclip-ai", "interview"):
        assert scope.classify(default, repository) == scope.OUT_OF_SCOPE


def test_unknown_repository_is_out_of_scope() -> None:
    assert scope.classify(scope.RepositoryScope(), "some-other-service") == scope.OUT_OF_SCOPE


def test_missing_repository_is_unresolved() -> None:
    assert scope.classify(scope.RepositoryScope(), None) == scope.UNRESOLVED


def test_configuration_carries_the_pilot_scope(config: config_module.Config) -> None:
    configured = config.repository_scope
    assert "medicodio-nextgen-app-nodejs" in configured.repositories
    assert "globalcodio-monorepo" in configured.excluded
    assert scope.classify(configured, "globalcodio-monorepo") == scope.OUT_OF_SCOPE
