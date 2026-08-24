"""Report functions whose body exceeds the project limit of ten statements.

The project rule is one job per function: a function body may contain at most ten
statements, so a failure is diagnosable by reading a single screen of code.
"""

from __future__ import annotations

import ast
import sys
from collections.abc import Iterator
from pathlib import Path

LIMIT = 10


def _is_docstring(node: ast.stmt) -> bool:
    return isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)


def _body(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.stmt]:
    statements = list(node.body)
    if statements and _is_docstring(statements[0]):
        statements = statements[1:]
    return statements


def _statements(node: ast.stmt) -> int:
    """Count ``node`` plus every statement nested inside it."""
    return 1 + sum(_statements(child) for child in ast.iter_child_nodes(node) if _is_stmt(child))


def _is_stmt(node: ast.AST) -> bool:
    return isinstance(node, ast.stmt)


def _size(node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    return sum(_statements(statement) for statement in _body(node))


def _functions(tree: ast.AST) -> Iterator[ast.FunctionDef | ast.AsyncFunctionDef]:
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            yield node


def offenders(path: Path, limit: int = LIMIT) -> list[tuple[str, int, int]]:
    """Return ``(qualified_name, line, size)`` for every function over ``limit``."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = [(node.name, node.lineno, _size(node)) for node in _functions(tree)]
    return [item for item in found if item[2] > limit]


def scan(directory: Path, limit: int = LIMIT) -> dict[Path, list[tuple[str, int, int]]]:
    """Map each file under ``directory`` to its over-limit functions."""
    results: dict[Path, list[tuple[str, int, int]]] = {}
    for path in sorted(directory.rglob("*.py")):
        found = offenders(path, limit)
        if found:
            results[path] = found
    return results


def _report(results: dict[Path, list[tuple[str, int, int]]]) -> None:
    for path, found in results.items():
        for name, line, size in found:
            print(f"{path}:{line}: {name} has {size} statements (limit {LIMIT})")


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    root = Path(args[0]) if args else Path(__file__).resolve().parents[1] / "src"
    results = scan(root)
    _report(results)
    return 1 if results else 0


if __name__ == "__main__":
    raise SystemExit(main())
