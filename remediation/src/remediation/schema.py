"""JSON Schema loading and validation.

Every machine document the pipeline emits is validated before it is written, so
an invalid artifact fails the run instead of being handed to the next stage.
"""

from __future__ import annotations

import json
from functools import cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from .config import PROJECT_ROOT

SCHEMA_DIR = PROJECT_ROOT / "schemas"

PRE_STAGE_MANIFEST = "pre_stage_manifest"
ISSUE = "issue"
STAGE_OUTPUT = "stage_output"
FUTURE_STAGE_CONTRACTS = "future_stage_contracts"

SCHEMAS: tuple[str, ...] = (PRE_STAGE_MANIFEST, ISSUE, STAGE_OUTPUT, FUTURE_STAGE_CONTRACTS)


class SchemaValidationError(ValueError):
    """Raised when a document does not satisfy its schema."""


@cache
def _load(name: str) -> dict[str, Any]:
    path = SCHEMA_DIR / f"{name}.schema.json"
    if not path.exists():
        raise SchemaValidationError(f"unknown schema {name!r} (looked in {path})")
    return json.loads(path.read_text(encoding="utf-8"))


@cache
def _validator(name: str, pointer: str | None = None) -> Draft202012Validator:
    schema = _load(name)
    if pointer:
        schema = {**schema.get("$defs", {})[pointer], "$defs": schema.get("$defs", {})}
    return Draft202012Validator(schema)


def load_schema(name: str) -> dict[str, Any]:
    """Return a schema document, raising if it is missing or malformed."""
    return _load(name)


def validate(document: Any, schema_name: str, pointer: str | None = None) -> None:
    errors = sorted(_validator(schema_name, pointer).iter_errors(document), key=lambda e: e.path)
    if not errors:
        return
    detail = "; ".join(
        f"{'/'.join(str(p) for p in error.path) or '<root>'}: {error.message}" for error in errors
    )
    target = f"{schema_name}#{pointer}" if pointer else schema_name
    raise SchemaValidationError(f"{target} validation failed: {detail}")


def write_json(document: Any, path: Path, schema_name: str, pointer: str | None = None) -> Path:
    """Validate then write a machine artifact."""
    validate(document, schema_name, pointer)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path
