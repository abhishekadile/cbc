from __future__ import annotations

from .fusion_context import PartModel
from .fusion_context import FusionDesignContext, mm_to_cm, value_cm


def add_centered_plate(model: PartModel, x_mm: float, y_mm: float, z_mm: float, name: str = "main_plate") -> None:
    model.add_feature("extrude_box", name, center=[0, 0, z_mm / 2], size=[x_mm, y_mm, z_mm])


def add_upright(model: PartModel, x_mm: float, y_mm: float, z_mm: float, center_x_mm: float, center_y_mm: float, name: str) -> None:
    model.add_feature("extrude_box", name, center=[center_x_mm, center_y_mm, z_mm / 2], size=[x_mm, y_mm, z_mm])


def add_cylinder(model: PartModel, diameter_mm: float, height_mm: float, center: tuple[float, float, float], name: str) -> None:
    model.add_feature("cylinder", name, center=list(center), diameter_mm=diameter_mm, height_mm=height_mm)


def add_ring(model: PartModel, outer_d_mm: float, inner_d_mm: float, height_mm: float, name: str) -> None:
    model.add_feature("ring", name, center=[0, 0, height_mm / 2], outer_d_mm=outer_d_mm, inner_d_mm=inner_d_mm, height_mm=height_mm)


def fusion_box(ctx: FusionDesignContext, component, name: str, x_mm: float, y_mm: float, z_mm: float, center_x_mm: float = 0.0, center_y_mm: float = 0.0, operation=None):
    sketch = component.sketches.add(component.xYConstructionPlane)
    sketch.name = f"{name}_profile"
    lines = sketch.sketchCurves.sketchLines
    lines.addCenterPointRectangle(
        ctx.adsk_core.Point3D.create(mm_to_cm(center_x_mm), mm_to_cm(center_y_mm), 0),
        ctx.adsk_core.Point3D.create(mm_to_cm(center_x_mm + x_mm / 2), mm_to_cm(center_y_mm + y_mm / 2), 0),
    )
    extrude = component.features.extrudeFeatures.addSimple(
        sketch.profiles.item(0),
        value_cm(ctx, z_mm),
        operation or ctx.adsk_fusion.FeatureOperations.NewBodyFeatureOperation,
    )
    body = extrude.bodies.item(0)
    body.name = name
    return body


def fusion_cylinder(ctx: FusionDesignContext, component, name: str, diameter_mm: float, z_mm: float, center_x_mm: float = 0.0, center_y_mm: float = 0.0, operation=None):
    sketch = component.sketches.add(component.xYConstructionPlane)
    sketch.name = f"{name}_profile"
    sketch.sketchCurves.sketchCircles.addByCenterRadius(
        ctx.adsk_core.Point3D.create(mm_to_cm(center_x_mm), mm_to_cm(center_y_mm), 0),
        mm_to_cm(diameter_mm) / 2,
    )
    extrude = component.features.extrudeFeatures.addSimple(
        sketch.profiles.item(0),
        value_cm(ctx, z_mm),
        operation or ctx.adsk_fusion.FeatureOperations.NewBodyFeatureOperation,
    )
    body = extrude.bodies.item(0)
    body.name = name
    return body
