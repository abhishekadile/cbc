from __future__ import annotations

from pathlib import Path

from .fusion_context import FusionDesignContext, PartModel


def export_placeholder(model: PartModel, output_path: Path, kind: str) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        f"NON-PRINTABLE CBC CAD {kind} placeholder generated from deterministic script spec.\n"
        "This file was not generated through Autodesk Fusion ExportManager and must not be used for manufacturing.\n"
        f"name={model.name}\n"
        f"bbox_mm={model.bbox_mm}\n"
        f"material_tag={model.material_tag}\n",
        encoding="utf-8",
    )
    return output_path


def export_model(
    model: PartModel,
    output_path: Path,
    ctx: FusionDesignContext | None = None,
    component=None,
) -> Path:
    if ctx is not None and component is not None and ctx.is_live_fusion:
        suffix = output_path.suffix.lower()
        if suffix == ".stl":
            return export_component(ctx, component, stl_path=output_path)[0]
        if suffix in (".step", ".stp"):
            return export_component(ctx, component, step_path=output_path)[0]
        if suffix == ".f3d":
            return save_design_f3d(ctx, output_path)
        raise ValueError(f"Unsupported export suffix: {output_path.suffix}")

    suffix = output_path.suffix.lower()
    if suffix == ".stl":
        return export_placeholder(model, output_path, "STL")
    if suffix in (".step", ".stp"):
        return export_placeholder(model, output_path, "STEP")
    if suffix == ".f3d":
        return export_placeholder(model, output_path, "F3D")
    raise ValueError(f"Unsupported export suffix: {output_path.suffix}")


def export_component(ctx: FusionDesignContext, component, stl_path: Path | None = None, step_path: Path | None = None) -> list[Path]:
    if not ctx.is_live_fusion:
        raise RuntimeError("Fusion API is required for real STL/STEP exports")
    exported: list[Path] = []
    manager = ctx.design.exportManager
    if stl_path is not None:
        stl_path.parent.mkdir(parents=True, exist_ok=True)
        options = manager.createSTLExportOptions(component, str(stl_path))
        manager.execute(options)
        exported.append(stl_path)
    if step_path is not None:
        step_path.parent.mkdir(parents=True, exist_ok=True)
        options = manager.createSTEPExportOptions(str(step_path), component)
        manager.execute(options)
        exported.append(step_path)
    return exported


def export_design_step(ctx: FusionDesignContext, output_path: Path) -> Path:
    if not ctx.is_live_fusion:
        raise RuntimeError("Fusion API is required for real STEP exports")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    options = ctx.design.exportManager.createSTEPExportOptions(str(output_path))
    ctx.design.exportManager.execute(options)
    return output_path


def save_design_f3d(ctx: FusionDesignContext, output_path: Path) -> Path:
    if not ctx.is_live_fusion:
        raise RuntimeError("Fusion API is required for real F3D exports")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    options = ctx.design.exportManager.createFusionArchiveExportOptions(str(output_path))
    ctx.design.exportManager.execute(options)
    return output_path
