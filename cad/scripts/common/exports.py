from __future__ import annotations

from pathlib import Path

from .fusion_context import PartModel


def export_placeholder(model: PartModel, output_path: Path, kind: str) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        f"CBC CAD {kind} placeholder generated from deterministic script spec.\n"
        f"name={model.name}\n"
        f"bbox_mm={model.bbox_mm}\n"
        f"material_tag={model.material_tag}\n",
        encoding="utf-8",
    )
    return output_path


def export_model(model: PartModel, output_path: Path) -> Path:
    suffix = output_path.suffix.lower()
    if suffix == ".stl":
        return export_placeholder(model, output_path, "STL")
    if suffix in (".step", ".stp"):
        return export_placeholder(model, output_path, "STEP")
    if suffix == ".f3d":
        return export_placeholder(model, output_path, "F3D")
    raise ValueError(f"Unsupported export suffix: {output_path.suffix}")
