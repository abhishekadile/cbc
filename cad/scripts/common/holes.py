from __future__ import annotations

from .fusion_context import PartModel
from .fusion_context import FusionDesignContext, mm_to_cm, value_cm


def add_hole(model: PartModel, x_mm: float, y_mm: float, diameter_mm: float, through: bool = True, name: str = "hole") -> None:
    model.add_feature("hole", name, center=[x_mm, y_mm], diameter_mm=diameter_mm, through=through)


def add_hole_pattern(model: PartModel, span_x_mm: float, span_y_mm: float, diameter_mm: float, name: str) -> None:
    for x in (-span_x_mm / 2, span_x_mm / 2):
        for y in (-span_y_mm / 2, span_y_mm / 2):
            add_hole(model, x, y, diameter_mm, True, f"{name}_{x:g}_{y:g}")


def add_slot(model: PartModel, x_mm: float, y_mm: float, length_mm: float, diameter_mm: float, axis: str, name: str) -> None:
    model.add_feature(
        "slot",
        name,
        center=[x_mm, y_mm],
        length_mm=length_mm,
        diameter_mm=diameter_mm,
        axis=axis,
    )


def add_slot_pattern(model: PartModel, span_x_mm: float, span_y_mm: float, length_mm: float, diameter_mm: float, axis: str, name: str) -> None:
    for x in (-span_x_mm / 2, span_x_mm / 2):
        for y in (-span_y_mm / 2, span_y_mm / 2):
            add_slot(model, x, y, length_mm, diameter_mm, axis, f"{name}_{x:g}_{y:g}")


def _cut_profile(ctx: FusionDesignContext, component, profile, depth_mm: float):
    return component.features.extrudeFeatures.addSimple(
        profile,
        value_cm(ctx, abs(depth_mm)),
        ctx.adsk_fusion.FeatureOperations.CutFeatureOperation,
    )


def fusion_cut_hole(ctx: FusionDesignContext, component, x_mm: float, y_mm: float, diameter_mm: float, depth_mm: float, name: str):
    sketch = component.sketches.add(component.xYConstructionPlane)
    sketch.name = f"{name}_cut"
    sketch.sketchCurves.sketchCircles.addByCenterRadius(
        ctx.adsk_core.Point3D.create(mm_to_cm(x_mm), mm_to_cm(y_mm), 0),
        mm_to_cm(diameter_mm) / 2,
    )
    return _cut_profile(ctx, component, sketch.profiles.item(0), depth_mm)


def fusion_cut_hole_pattern(ctx: FusionDesignContext, component, span_x_mm: float, span_y_mm: float, diameter_mm: float, depth_mm: float, name: str):
    for x_mm in (-span_x_mm / 2, span_x_mm / 2):
        for y_mm in (-span_y_mm / 2, span_y_mm / 2):
            fusion_cut_hole(ctx, component, x_mm, y_mm, diameter_mm, depth_mm, f"{name}_{x_mm:g}_{y_mm:g}")


def fusion_cut_rect(ctx: FusionDesignContext, component, x_mm: float, y_mm: float, size_x_mm: float, size_y_mm: float, depth_mm: float, name: str):
    sketch = component.sketches.add(component.xYConstructionPlane)
    sketch.name = f"{name}_cut"
    sketch.sketchCurves.sketchLines.addCenterPointRectangle(
        ctx.adsk_core.Point3D.create(mm_to_cm(x_mm), mm_to_cm(y_mm), 0),
        ctx.adsk_core.Point3D.create(mm_to_cm(x_mm + size_x_mm / 2), mm_to_cm(y_mm + size_y_mm / 2), 0),
    )
    return _cut_profile(ctx, component, sketch.profiles.item(0), depth_mm)


def fusion_cut_rect_from_top(
    ctx: FusionDesignContext,
    component,
    x_mm: float,
    y_mm: float,
    size_x_mm: float,
    size_y_mm: float,
    top_z_mm: float,
    depth_mm: float,
    name: str,
):
    planes = component.constructionPlanes
    plane_input = planes.createInput()
    plane_input.setByOffset(component.xYConstructionPlane, value_cm(ctx, top_z_mm))
    top_plane = planes.add(plane_input)
    sketch = component.sketches.add(top_plane)
    sketch.name = f"{name}_top_cut"
    sketch.sketchCurves.sketchLines.addCenterPointRectangle(
        ctx.adsk_core.Point3D.create(mm_to_cm(x_mm), mm_to_cm(y_mm), 0),
        ctx.adsk_core.Point3D.create(mm_to_cm(x_mm + size_x_mm / 2), mm_to_cm(y_mm + size_y_mm / 2), 0),
    )
    return component.features.extrudeFeatures.addSimple(
        sketch.profiles.item(0),
        value_cm(ctx, -abs(depth_mm)),
        ctx.adsk_fusion.FeatureOperations.CutFeatureOperation,
    )


def fusion_cut_slot(ctx: FusionDesignContext, component, x_mm: float, y_mm: float, length_mm: float, diameter_mm: float, depth_mm: float, axis: str, name: str):
    slot_x = length_mm if axis == "x" else diameter_mm
    slot_y = diameter_mm if axis == "x" else length_mm
    fusion_cut_rect(ctx, component, x_mm, y_mm, slot_x, slot_y, depth_mm, name)
    if axis == "x":
        fusion_cut_hole(ctx, component, x_mm - length_mm / 2, y_mm, diameter_mm, depth_mm, f"{name}_end_a")
        fusion_cut_hole(ctx, component, x_mm + length_mm / 2, y_mm, diameter_mm, depth_mm, f"{name}_end_b")
    else:
        fusion_cut_hole(ctx, component, x_mm, y_mm - length_mm / 2, diameter_mm, depth_mm, f"{name}_end_a")
        fusion_cut_hole(ctx, component, x_mm, y_mm + length_mm / 2, diameter_mm, depth_mm, f"{name}_end_b")
