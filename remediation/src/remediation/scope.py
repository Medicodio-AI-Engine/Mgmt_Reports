"""Which repositories this pilot is allowed to look at.

The pilot covers the medicodio libraries and the management-reports repository
only. Scope is registry-driven: the in-scope names, the name prefixes and the
explicitly excluded names all come from configuration, so widening the pilot is a
config change rather than a code change.

An out-of-scope finding is never deleted — deleting it would destroy report
evidence. It is labelled ``OUT_OF_SCOPE`` and excluded from candidate selection
and from the supervisor report.
"""

from __future__ import annotations

from dataclasses import dataclass

IN_SCOPE = "IN_SCOPE"
OUT_OF_SCOPE = "OUT_OF_SCOPE"
UNRESOLVED = "UNRESOLVED"

DEFAULT_REPOSITORIES: tuple[str, ...] = (
    "Mgmt_Reports",
    "medicodio-nextgen-app-nodejs",
    "medicodio-nextgen-app-react",
    "medicodio-nextgen-integration",
    "medicodio-paperclip",
    "nextgen-codio-engine",
)
DEFAULT_PREFIXES: tuple[str, ...] = ("medicodio-", "nextgen-codio")
DEFAULT_EXCLUDED: tuple[str, ...] = ("globalcodio-monorepo", "paperclip-ai", "interview")


@dataclass(frozen=True)
class RepositoryScope:
    """The configured pilot scope."""

    repositories: tuple[str, ...] = DEFAULT_REPOSITORIES
    prefixes: tuple[str, ...] = DEFAULT_PREFIXES
    excluded: tuple[str, ...] = DEFAULT_EXCLUDED

    def known(self) -> tuple[str, ...]:
        """Every repository name the pilot can recognise, in or out of scope."""
        return tuple(sorted({*self.repositories, *self.excluded}))


def _short_name(repository: str) -> str:
    return repository.rsplit("/", 1)[-1].strip()


def _listed(scope: RepositoryScope, name: str) -> bool:
    return name.lower() in {entry.lower() for entry in scope.repositories}


def _excluded(scope: RepositoryScope, name: str) -> bool:
    return name.lower() in {entry.lower() for entry in scope.excluded}


def _prefixed(scope: RepositoryScope, name: str) -> bool:
    return any(name.lower().startswith(prefix.lower()) for prefix in scope.prefixes)


def classify(scope: RepositoryScope, repository: str | None) -> str:
    """Label ``repository`` as in scope, out of scope, or not yet resolved."""
    if not repository:
        return UNRESOLVED
    name = _short_name(repository)
    if _excluded(scope, name):
        return OUT_OF_SCOPE
    if _listed(scope, name) or _prefixed(scope, name):
        return IN_SCOPE
    return OUT_OF_SCOPE


def reason(scope: RepositoryScope, repository: str | None) -> str:
    """Explain the label in one sentence a supervisor can act on."""
    label = classify(scope, repository)
    if label == UNRESOLVED:
        return "the report does not name a repository, so scope cannot be decided"
    if label == IN_SCOPE:
        return f"{_short_name(repository or '')} is a medicodio library in the pilot scope"
    return f"{_short_name(repository or '')} is outside the medicodio pilot scope"


def mentions(scope: RepositoryScope, text: str) -> tuple[str, ...]:
    """Known repository names named in ``text``, in configuration order."""
    lowered = text.lower()
    return tuple(name for name in scope.known() if name.lower() in lowered)
