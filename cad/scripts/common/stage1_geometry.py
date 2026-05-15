from __future__ import annotations

from typing import Any

from .fusion_context import FusionDesignContext, PartModel, add_user_parameter, create_part, new_component
from .holes import (
    add_hole,
    add_hole_pattern,
    add_slot,
    fusion_cut_hole,
    fusion_cut_hole_pattern,
    fusion_cut_rect,
    fusion_cut_rect_from_top,
    fusion_cut_slot,
)
from .sketches import add_centered_plate, add_cylinder, add_ring, fusion_box, fusion_cylinder


def _join(ctx: FusionDesignContext):
    return ctx.adsk_fusion.FeatureOperations.JoinFeatureOperation


def _stage1(data: dict[str, Any]) -> dict[str, Any]:
    return data["prototype_v1"]["stage1"]


def _locked(data: dict[str, Any]) -> dict[str, Any]:
    return data["locked_dimensions"]


def baseplate_spec(data: dict[str, Any]) -> PartModel:
    locked = _locked(data)
    sys = locked["system"]
    stage = _stage1(data)
    c = data["clearances"]
    model = create_part("cbc_baseplate_r001", "petg_printable_stage1", (sys["stage1_baseplate_x_mm"], sys["stage1_baseplate_y_mm"], sys["stage1_baseplate_z_mm"]))
    add_centered_plate(model, *model.bbox_mm)
    foot_x = sys["stage1_baseplate_x_mm"] - 2 * sys["rubber_foot_offset_from_corner_mm"]
    foot_y = sys["stage1_baseplate_y_mm"] - 2 * sys["rubber_foot_offset_from_corner_mm"]
    add_hole_pattern(model, foot_x, foot_y, c["m3_clearance_hole_mm"]["easy"], "rubber_foot_holes")
    add_hole_pattern(model, stage["slide_holder_mount_span_x_mm"], stage["slide_holder_mount_span_y_mm"], c["m3_insert_pilot_mm"], "slide_holder_insert_pilots")
    add_hole_pattern(model, stage["tower_mount_span_x_mm"], stage["tower_mount_span_y_mm"], c["m3_insert_pilot_mm"], "future_tower_insert_pilots")
    model.add_feature("wire_channel", "pi_to_tower_cable_channel", width_mm=8.0, depth_mm=1.6)
    model.add_feature("wire_channel", "pi_to_led_cable_channel", width_mm=6.0, depth_mm=1.4)
    model.add_feature("engraved_label", "CBC SCANNER V1", depth_mm=0.4)
    model.add_feature("engraved_label", "OPTICAL AXIS", depth_mm=0.4)
    model.add_feature("engraved_label", "SLIDE", depth_mm=0.4)
    model.add_feature("engraved_label", "PI4", depth_mm=0.4)
    return model


def build_baseplate_fusion(ctx: FusionDesignContext, data: dict[str, Any]):
    locked = _locked(data)
    sys = locked["system"]
    stage = _stage1(data)
    c = data["clearances"]
    component = new_component(ctx, "cbc_baseplate_r001")
    add_user_parameter(ctx, "stage1_baseplate_x_mm", sys["stage1_baseplate_x_mm"], "Stage 1 baseplate X")
    add_user_parameter(ctx, "stage1_baseplate_y_mm", sys["stage1_baseplate_y_mm"], "Stage 1 baseplate Y")
    add_user_parameter(ctx, "stage1_baseplate_z_mm", sys["stage1_baseplate_z_mm"], "Stage 1 baseplate thickness")
    fusion_box(ctx, component, "rounded_baseplate_blank", sys["stage1_baseplate_x_mm"], sys["stage1_baseplate_y_mm"], sys["stage1_baseplate_z_mm"])
    foot_x = sys["stage1_baseplate_x_mm"] - 2 * sys["rubber_foot_offset_from_corner_mm"]
    foot_y = sys["stage1_baseplate_y_mm"] - 2 * sys["rubber_foot_offset_from_corner_mm"]
    fusion_cut_hole_pattern(ctx, component, foot_x, foot_y, c["m3_clearance_hole_mm"]["easy"], sys["stage1_baseplate_z_mm"] + 1, "rubber_foot")
    fusion_cut_hole_pattern(ctx, component, stage["slide_holder_mount_span_x_mm"], stage["slide_holder_mount_span_y_mm"], c["m3_insert_pilot_mm"], sys["stage1_baseplate_z_mm"] + 1, "slide_holder_insert")
    fusion_cut_hole_pattern(ctx, component, stage["tower_mount_span_x_mm"], stage["tower_mount_span_y_mm"], c["m3_insert_pilot_mm"], sys["stage1_baseplate_z_mm"] + 1, "future_tower_insert")
    fusion_cut_slot(ctx, component, 42.0, -18.0, 82.0, 8.0, 1.8, "y", "pi_to_camera_cable_channel")
    fusion_cut_slot(ctx, component, 20.0, -28.0, 68.0, 6.0, 1.6, "x", "pi_to_led_cable_channel")
    return component


def slide_holder_spec(data: dict[str, Any]) -> PartModel:
    slide = _locked(data)["slide"]
    c = data["clearances"]
    pocket_x = slide["slide_x_mm"] + 2 * c["slide_end_clearance_mm"]
    pocket_y = slide["slide_y_mm"] + 2 * c["slide_side_clearance_mm"]
    holder_x = pocket_x + 12.0
    holder_y = pocket_y + 12.0
    holder_z = slide["holder_z_mm"]
    model = create_part("cbc_slide_holder_r001", "petg_printable_stage1", (holder_x, holder_y, holder_z))
    add_centered_plate(model, *model.bbox_mm)
    model.add_feature("slide_pocket", "removable_slide_pocket", size_mm=[pocket_x, pocket_y], depth_mm=1.2)
    model.add_feature("viewing_window", "centered_window", size_mm=[slide["viewing_window_x_mm"], slide["viewing_window_y_mm"]], through=True)
    add_hole_pattern(model, holder_x - 10.0, holder_y - 8.0, c["m3_clearance_hole_mm"]["snug"], "m3_mounting_holes")
    add_slot(model, -pocket_x / 4, pocket_y / 2 + 3.0, 14.0, c["m3_clearance_hole_mm"]["snug"], "x", "left_clamp_retainer_slot")
    add_slot(model, pocket_x / 4, pocket_y / 2 + 3.0, 14.0, c["m3_clearance_hole_mm"]["snug"], "x", "right_clamp_retainer_slot")
    model.add_feature("retaining_tabs", "two_open_edge_tabs", removable_slide=True)
    model.metadata["calculated_slide_pocket_mm"] = {"x": pocket_x, "y": pocket_y}
    return model


def build_slide_holder_fusion(ctx: FusionDesignContext, data: dict[str, Any]):
    slide = _locked(data)["slide"]
    c = data["clearances"]
    pocket_x = slide["slide_x_mm"] + 2 * c["slide_end_clearance_mm"]
    pocket_y = slide["slide_y_mm"] + 2 * c["slide_side_clearance_mm"]
    holder_x = pocket_x + 12.0
    holder_y = pocket_y + 12.0
    holder_z = slide["holder_z_mm"]
    component = new_component(ctx, "cbc_slide_holder_r001")
    body = fusion_box(ctx, component, "slide_holder_body", holder_x, holder_y, holder_z)
    body.name = "cbc_slide_holder_r001"
    fusion_cut_rect_from_top(ctx, component, 0, 0, pocket_x, pocket_y, holder_z, 1.2, "slide_pocket_recess")
    fusion_cut_rect(ctx, component, 0, 0, slide["viewing_window_x_mm"], slide["viewing_window_y_mm"], holder_z + 1, "viewing_window")
    fusion_cut_hole_pattern(ctx, component, holder_x - 10.0, holder_y - 8.0, c["m3_clearance_hole_mm"]["snug"], holder_z + 1, "m3_mount")
    fusion_cut_slot(ctx, component, -pocket_x / 4, pocket_y / 2 + 3.0, 14.0, c["m3_clearance_hole_mm"]["snug"], holder_z + 1, "x", "left_clamp_retainer_slot")
    fusion_cut_slot(ctx, component, pocket_x / 4, pocket_y / 2 + 3.0, 14.0, c["m3_clearance_hole_mm"]["snug"], holder_z + 1, "x", "right_clamp_retainer_slot")
    # Side and rear tabs leave the slide removable from the front.
    fusion_box(ctx, component, "left_retaining_tab", pocket_x, 2.4, 1.4, 0, pocket_y / 2 + 2.0, operation=_join(ctx))
    fusion_box(ctx, component, "right_retaining_tab", pocket_x, 2.4, 1.4, 0, -pocket_y / 2 - 2.0, operation=_join(ctx))
    fusion_box(ctx, component, "rear_end_stop_tab", 2.4, pocket_y, 1.4, -pocket_x / 2 - 2.0, 0, operation=_join(ctx))
    try:
        fillets = component.features.filletFeatures
        edge_collection = ctx.adsk_core.ObjectCollection.create()
        for edge in body.edges:
            edge_collection.add(edge)
        fillet_input = fillets.createInput()
        fillet_input.addConstantRadiusEdgeSet(edge_collection, ctx.adsk_core.ValueInput.createByString("1 mm"), True)
        fillets.add(fillet_input)
    except Exception:
        pass
    return component


def pi4_mount_spec(data: dict[str, Any]) -> PartModel:
    pi = _locked(data)["pi4"]
    c = data["clearances"]
    model = create_part("cbc_pi4_mount_r001", "petg_printable_stage1", (pi["board_nest_x_mm"] + 10.0, pi["board_nest_y_mm"] + 10.0, pi["standoff_boss_height_mm"] + 2.0))
    add_centered_plate(model, *model.bbox_mm)
    add_hole_pattern(model, pi["mount_hole_span_x_mm"], pi["mount_hole_span_y_mm"], pi["standoff_hole_d_mm"], "pi4_standoff_holes")
    model.add_feature("bosses", "four_pi4_standoff_bosses", outer_d_mm=pi["standoff_boss_outer_d_mm"], height_mm=pi["standoff_boss_height_mm"])
    model.add_feature("connector_keepout", "usb_ethernet_hdmi_gpio_keepouts", note="Do not cover board connectors")
    model.add_feature("cable_openings", "camera_power_gpio_routes", count=3)
    return model


def build_pi4_mount_fusion(ctx: FusionDesignContext, data: dict[str, Any]):
    pi = _locked(data)["pi4"]
    c = data["clearances"]
    component = new_component(ctx, "cbc_pi4_mount_r001")
    fusion_box(ctx, component, "pi4_mount_tray_floor", pi["board_nest_x_mm"] + 10.0, pi["board_nest_y_mm"] + 10.0, 2.0)
    for x in (-pi["mount_hole_span_x_mm"] / 2, pi["mount_hole_span_x_mm"] / 2):
        for y in (-pi["mount_hole_span_y_mm"] / 2, pi["mount_hole_span_y_mm"] / 2):
            fusion_cylinder(ctx, component, f"standoff_boss_{x:g}_{y:g}", pi["standoff_boss_outer_d_mm"], pi["standoff_boss_height_mm"], x, y, _join(ctx))
            fusion_cut_hole(ctx, component, x, y, pi["standoff_hole_d_mm"], pi["standoff_boss_height_mm"] + 2.5, f"standoff_hole_{x:g}_{y:g}")
    # Connector keepouts and cable openings are edge reliefs in the tray.
    fusion_cut_rect(ctx, component, 0, -(pi["board_nest_y_mm"] + 10.0) / 2 + 2.0, 48.0, 8.0, 3.0, "usb_ethernet_edge_keepout")
    fusion_cut_rect(ctx, component, -25.0, (pi["board_nest_y_mm"] + 10.0) / 2 - 2.0, 18.0, 8.0, 3.0, "usb_c_power_keepout")
    fusion_cut_rect(ctx, component, 30.0, (pi["board_nest_y_mm"] + 10.0) / 2 - 2.0, 22.0, 8.0, 3.0, "gpio_ribbon_keepout")
    return component


def camera_mount_rpi_gs_spec(data: dict[str, Any]) -> PartModel:
    cam = _locked(data)["camera_rpi_gs"]
    c = data["clearances"]
    model = create_part("cbc_camera_mount_rpi_gs_r001", "matte_black_petg_printable_stage1", (cam["board_nest_x_mm"] + 10.0, cam["board_nest_y_mm"] + 10.0, _stage1(data)["camera_plate_z_mm"]))
    add_centered_plate(model, *model.bbox_mm)
    add_hole_pattern(model, cam["mount_hole_span_x_mm"], cam["mount_hole_span_y_mm"], c["m2p5_printed_clearance_hole_mm"], "camera_board_mount")
    model.add_feature("sensor_axis", "centered_on_optical_axis")
    model.add_feature("cable_relief_slot", "rpi_gs_ribbon_exit")
    model.add_feature("slotted_attachment", "optical_tower_interface_slots")
    return model


def build_camera_mount_rpi_gs_fusion(ctx: FusionDesignContext, data: dict[str, Any]):
    cam = _locked(data)["camera_rpi_gs"]
    c = data["clearances"]
    z = _stage1(data)["camera_plate_z_mm"]
    component = new_component(ctx, "cbc_camera_mount_rpi_gs_r001")
    fusion_box(ctx, component, "camera_board_mount_plate", cam["board_nest_x_mm"] + 10.0, cam["board_nest_y_mm"] + 10.0, z)
    fusion_cut_hole_pattern(ctx, component, cam["mount_hole_span_x_mm"], cam["mount_hole_span_y_mm"], c["m2p5_printed_clearance_hole_mm"], z + 1, "camera_board")
    fusion_cut_rect(ctx, component, 0, -22.0, 18.0, 8.0, z + 1, "ribbon_cable_relief")
    fusion_cut_slot(ctx, component, -20.0, 0, 12.0, c["m3_clearance_hole_mm"]["easy"], z + 1, "y", "tower_slot_left")
    fusion_cut_slot(ctx, component, 20.0, 0, 12.0, c["m3_clearance_hole_mm"]["easy"], z + 1, "y", "tower_slot_right")
    return component


def objective_holder_placeholder_spec(data: dict[str, Any]) -> PartModel:
    optics = _locked(data)["optics"]
    height = _stage1(data)["objective_holder_height_mm"]
    outer_d = optics["stage1_placeholder_holder_bore_mm"] + 2 * optics["stage1_placeholder_holder_wall_mm"]
    model = create_part("cbc_objective_holder_placeholder_r001", "matte_black_petg_printable_stage1", (outer_d, outer_d, height))
    add_ring(model, outer_d, optics["stage1_placeholder_holder_bore_mm"], height, "split_clamp_placeholder")
    add_slot(model, outer_d / 2 - 4.0, 0.0, 18.0, 3.2, "y", "split_clamp_screw_slot")
    model.add_warning("Placeholder only; final AmScope 40X objective shoulder/body geometry must be measured.")
    model.metadata["not_final_rms_thread"] = True
    return model


def build_objective_holder_placeholder_fusion(ctx: FusionDesignContext, data: dict[str, Any]):
    optics = _locked(data)["optics"]
    height = _stage1(data)["objective_holder_height_mm"]
    outer_d = optics["stage1_placeholder_holder_bore_mm"] + 2 * optics["stage1_placeholder_holder_wall_mm"]
    component = new_component(ctx, "cbc_objective_holder_placeholder_r001")
    fusion_cylinder(ctx, component, "holder_outer_body", outer_d, height)
    fusion_cut_hole(ctx, component, 0, 0, optics["stage1_placeholder_holder_bore_mm"], height + 1, "objective_placeholder_bore")
    fusion_cut_slot(ctx, component, outer_d / 2 - 4.0, 0.0, 18.0, 3.2, height + 1, "y", "split_clamp_slot")
    return component


def optical_axis_datum_spec(data: dict[str, Any]) -> PartModel:
    model = create_part("cbc_optical_axis_datum_r001", "non_print_reference", (2.0, 2.0, _locked(data)["optics"]["objective_shoulder_to_sensor_plane_mm"]))
    model.add_feature("datum_axis", "objective_shoulder_to_sensor_plane", length_mm=160.0)
    model.metadata["reference_only"] = True
    return model


def build_optical_axis_datum_fusion(ctx: FusionDesignContext, data: dict[str, Any]):
    component = new_component(ctx, "cbc_optical_axis_datum_r001_reference_only")
    fusion_cylinder(ctx, component, "visible_optical_axis_160mm", 1.0, _locked(data)["optics"]["objective_shoulder_to_sensor_plane_mm"])
    return component
