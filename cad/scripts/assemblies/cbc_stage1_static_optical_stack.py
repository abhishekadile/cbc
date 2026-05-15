from __future__ import annotations

from cad.scripts.common.fusion_context import PartModel, create_part, move_component
from cad.scripts.common.params import load_all, unresolved_paths
from cad.scripts.parts import (
    cbc_baseplate,
    cbc_camera_mount_rpi_gs,
    cbc_objective_holder_placeholder,
    cbc_optical_axis_datum,
    cbc_pi4_mount,
    cbc_slide_holder,
)


STAGE1_PRINTED_PARTS = [
    cbc_baseplate,
    cbc_slide_holder,
    cbc_pi4_mount,
    cbc_camera_mount_rpi_gs,
    cbc_objective_holder_placeholder,
]


def build(data=None) -> PartModel:
    data = data or load_all()
    model = create_part("cbc_stage1_static_optical_stack_r001", "assembly_stage1_reference", (180.0, 160.0, 180.0))
    model.metadata["printed_parts"] = [module.build(data).name for module in STAGE1_PRINTED_PARTS]
    model.metadata["reference_components"] = [cbc_optical_axis_datum.build(data).name]
    model.metadata["optical_axis"] = {
        "x_mm": data["prototype_v1"]["stage1"]["optical_axis_x_mm"],
        "y_mm": data["prototype_v1"]["stage1"]["optical_axis_y_mm"],
        "objective_shoulder_to_sensor_plane_mm": data["locked_dimensions"]["optics"]["objective_shoulder_to_sensor_plane_mm"],
    }
    unresolved = [
        path for path in unresolved_paths(data)
        if "stage1_optical_stack" in path or "objective_amscope_40x" in path
    ]
    if unresolved:
        model.add_warning("Unresolved Stage 1 optical dimensions: " + ", ".join(unresolved))
    return model


def build_fusion(ctx, data=None):
    data = data or load_all()
    base = cbc_baseplate.build_fusion(ctx, data)
    slide = cbc_slide_holder.build_fusion(ctx, data)
    pi4 = cbc_pi4_mount.build_fusion(ctx, data)
    camera = cbc_camera_mount_rpi_gs.build_fusion(ctx, data)
    objective = cbc_objective_holder_placeholder.build_fusion(ctx, data)
    datum = cbc_optical_axis_datum.build_fusion(ctx, data)

    stage = data["prototype_v1"]["stage1"]
    move_component(ctx, base.name, 0, 0, 0)
    move_component(ctx, slide.name, stage["optical_axis_x_mm"], stage["optical_axis_y_mm"], 6.0)
    move_component(ctx, pi4.name, stage["pi_mount_center_x_mm"], stage["pi_mount_center_y_mm"], 6.0)
    move_component(ctx, camera.name, stage["optical_axis_x_mm"], 62.0, 136.0)
    move_component(ctx, objective.name, stage["optical_axis_x_mm"], stage["optical_axis_y_mm"], 28.0)
    move_component(ctx, datum.name, stage["optical_axis_x_mm"], stage["optical_axis_y_mm"], 18.0)
    return {
        "baseplate": base,
        "slide_holder": slide,
        "pi4_mount": pi4,
        "camera_mount": camera,
        "objective_holder_placeholder": objective,
        "optical_axis_datum": datum,
    }
