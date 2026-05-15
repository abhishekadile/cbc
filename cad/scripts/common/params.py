from __future__ import annotations

from pathlib import Path
from typing import Any


CAD_ROOT = Path(__file__).resolve().parents[2]
PARAMS_DIR = CAD_ROOT / "params"


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "null":
        return None
    if value in ("true", "false"):
        return value == "true"
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    try:
        if any(ch in value for ch in (".", "e", "E")):
            return float(value)
        return int(value)
    except ValueError:
        return value


def _minimal_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        key, sep, raw_value = raw_line.strip().partition(":")
        if not sep:
            continue

        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]
        if raw_value.strip() == "":
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = _parse_scalar(raw_value)
    return root


def load_yaml(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(text)
        return loaded or {}
    except Exception:
        return _minimal_yaml(text)


def load_all() -> dict[str, Any]:
    data: dict[str, Any] = {}
    for name in (
        "locked_dimensions.yaml",
        "unresolved_dimensions.yaml",
        "clearances.yaml",
        "prototype_v1.yaml",
    ):
        data.update(load_yaml(PARAMS_DIR / name))
    return data


def get_path(data: dict[str, Any], dotted: str, default: Any = None) -> Any:
    current: Any = data
    for part in dotted.split("."):
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return current


def require_path(data: dict[str, Any], dotted: str) -> Any:
    value = get_path(data, dotted)
    if value is None:
        raise ValueError(f"Required CAD parameter is unresolved: {dotted}")
    return value


def unresolved_paths(data: dict[str, Any], prefix: str = "unresolved_dimensions") -> list[str]:
    root = get_path(data, prefix, {})
    found: list[str] = []

    def walk(node: Any, path: str) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                walk(value, f"{path}.{key}")
        elif node is None:
            found.append(path)

    walk(root, prefix)
    return found
