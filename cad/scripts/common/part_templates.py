from __future__ import annotations

from typing import Any

from .fusion_context import PartModel, create_part
from .holes import add_hole, add_hole_pattern, add_slot, add_slot_pattern
from .params import get_path
from .sketches import add_centered_plate, add_cylinder, add_ring, add_upright


def baseplate(data: dict[str, Any]) -> PartModel:
    layout = data["prototype_v1"]["layout"]
    c = data["clearances"]
    model = create_part(
        "cbc_baseplate_r001",
        "petg_structural_motion",
        (layout["baseplate_x_mm"], layout["baseplate_y_mm"], layout["baseplate_z_mm"]),
    )
    add_centered_plate(model, *model.bbox_mm)
    add_hole_pattern(model, 150.0, 140.0, c["m3_insert_pilot_mm"], "foot_insert")
    add_hole_pattern(model, 48.0, 32.0, c["m3_clearance_hole_mm"]["easy"], "optical_tower_datum")
    add_slot_pattern(model, 120.0, 60.0, 16.0, c["m3_clearance_hole_mm"]["easy"], "x", "rail_datum_slot")
    add_slot(model, 55.0, -55.0, 18.0, c["m3_clearance_hole_mm"]["easy"], "x", "electronics_deck_slot_a")
    add_slot(model, 85.0, -55.0, 18.0, c["m3_clearance_hole_mm"]["easy"], "x", "electronics_deck_slot_b")
    model.metadata["datums"] = ["optical_tower", "x_rails", "electronics_deck", "feet"]
    return model


def optical_tower(data: dict[str, Any]) -> PartModel:
    h = data["prototype_v1"]["layout"]["tower_height_mm"]
    model = create_part("cbc_optical_tower_r001", "matte_black_petg_optics_adjacent", (58.0, 42.0, h))
    add_upright(model, 18.0, 38.0, h, -20.0, 0.0, "left_column")
    add_upright(model, 18.0, 38.0, h, 20.0, 0.0, "right_column")
    add_upright(model, 58.0, 12.0, 18.0, 0.0, 0.0, "base_lug")
    add_upright(model, 58.0, 12.0, 18.0, 0.0, 0.0, "top_camera_lug")
    add_slot_pattern(model, 40.0, 0.0, 12.0, 3.4, "z", "camera_height_adjustment")
    model.add_feature("rib", "rear_web_stiffener", count=3, thickness_mm=5.0)
    return model


def camera_mount_rpi_gs(data: dict[str, Any]) -> PartModel:
    cam = data["locked_dimensions"]["camera_rpi_gs"]
    c = data["clearances"]
    model = create_part("cbc_camera_mount_rpi_gs_r001", "matte_black_petg_optics_adjacent", (54.0, 54.0, 8.0))
    add_centered_plate(model, *model.bbox_mm)
    add_hole_pattern(model, cam["mount_hole_span_x_mm"], cam["mount_hole_span_y_mm"], c["m2p5_printed_clearance_hole_mm"], "rpi_gs_mount")
    add_hole(model, 0, 0, 16.0, True, "sensor_clear_aperture")
    model.metadata["sensor_datum"] = "sensor plane, not camera exterior"
    return model


def camera_mount_imx296(data: dict[str, Any]) -> PartModel:
    c = data["clearances"]
    unresolved = data["unresolved_dimensions"]["camera_innomaker_imx296"]
    board_x = unresolved["board_x_mm"] or 42.0
    board_y = unresolved["board_y_mm"] or 42.0
    model = create_part("cbc_camera_mount_imx296_r001", "matte_black_petg_optics_adjacent", (board_x + 18.0, board_y + 18.0, 8.0))
    add_centered_plate(model, *model.bbox_mm)
    adjustment = c["vendor_uncertain_slot_adjustment_mm"]
    add_slot_pattern(model, 30.0, 30.0, 8.0 + adjustment * 2, c["m2p5_printed_clearance_hole_mm"], "x", "unresolved_imx296_mount_slot")
    add_hole(model, 0, 0, 16.0, True, "sensor_clear_aperture_todo_measure")
    model.add_warning("IMX296 board and sensor plane dimensions unresolved; slots are intentional placeholders.")
    model.metadata["todo"] = unresolved["note"]
    return model


def objective_holder(data: dict[str, Any]) -> PartModel:
    optics = data["locked_dimensions"]["optics"]
    p = data["prototype_v1"]["optics"]
    unresolved = data["unresolved_dimensions"]["objective_amscope_40x"]
    major_mm = optics["objective_rms_major_diameter_in"] * 25.4
    model = create_part("cbc_objective_holder_rms_r001", "matte_black_petg_optics_adjacent", (p["objective_holder_outer_d_mm"], p["objective_holder_outer_d_mm"], p["objective_holder_height_mm"]))
    add_ring(model, p["objective_holder_outer_d_mm"], major_mm + unresolved["thread_print_offset_mm"], p["objective_holder_height_mm"], "rms_threaded_or_split_clamp_body")
    add_slot(model, p["objective_holder_outer_d_mm"] / 2 - 5.0, 0.0, 16.0, 3.2, "y", "split_clamp_relief")
    model.metadata["rms_thread"] = {"major_diameter_in": optics["objective_rms_major_diameter_in"], "tpi": optics["objective_rms_tpi"]}
    model.metadata["thread_compensation_parameter"] = "unresolved_dimensions.objective_amscope_40x.thread_print_offset_mm"
    return model


def optical_tube(data: dict[str, Any]) -> PartModel:
    locked = data["locked_dimensions"]["optics"]
    p = data["prototype_v1"]["optics"]
    objective_holder_h = p["objective_holder_height_mm"]
    camera_offset = p["camera_mount_face_to_sensor_plane_mm"]
    tube_length = locked["objective_shoulder_to_sensor_plane_mm"] - objective_holder_h - camera_offset
    model = create_part("cbc_optical_tube_section_r001", "matte_black_petg_optics_adjacent", (p["optical_tube_outer_d_mm"], p["optical_tube_outer_d_mm"], tube_length))
    add_ring(model, p["optical_tube_outer_d_mm"], p["optical_tube_outer_d_mm"] - 2 * p["optical_tube_wall_mm"], tube_length, "160mm_stack_tube")
    model.metadata["objective_shoulder_to_sensor_plane_mm"] = locked["objective_shoulder_to_sensor_plane_mm"]
    model.metadata["tube_length_mm"] = tube_length
    model.metadata["stack_terms_mm"] = {"objective_holder": objective_holder_h, "tube": tube_length, "camera_mount_face_to_sensor": camera_offset}
    if abs((objective_holder_h + tube_length + camera_offset) - 160.0) > 0.01:
        model.add_warning("Optical stack does not hit 160.0 mm.")
    return model


def led_ring(data: dict[str, Any]) -> PartModel:
    p = data["prototype_v1"]["optics"]
    model = create_part("cbc_led_ring_holder_r001", "matte_black_petg_optics_adjacent", (p["led_ring_outer_d_mm"], p["led_ring_outer_d_mm"], 6.0))
    add_ring(model, p["led_ring_outer_d_mm"], p["led_ring_inner_d_mm"], 6.0, "led_ring_body")
    model.add_feature("led_holes", "parameterized_led_positions", count=p["led_count"], diameter_mm=5.2, concentric=True)
    return model


def diffuser_frame(data: dict[str, Any]) -> PartModel:
    p = data["prototype_v1"]["optics"]
    c = data["clearances"]
    model = create_part("cbc_diffuser_frame_r001", "matte_black_petg_optics_adjacent", (p["diffuser_frame_x_mm"], p["diffuser_frame_y_mm"], 5.0))
    add_centered_plate(model, *model.bbox_mm)
    add_hole(model, 0, 0, p["diffuser_window_d_mm"], True, "diffuser_window")
    add_hole_pattern(model, 54.0, 54.0, c["printed_peg_to_hole_diametral_mm"]["max"] + 2.0, "diffuser_sheet_capture_pegs")
    return model


def rail_support(data: dict[str, Any], stem: str, side: str) -> PartModel:
    m = data["prototype_v1"]["motion"]
    c = data["clearances"]
    model = create_part(f"{stem}_r001", "petg_structural_motion", (m["rail_support_x_mm"], m["rail_support_y_mm"], m["rail_support_z_mm"]))
    add_centered_plate(model, *model.bbox_mm)
    add_slot_pattern(model, 64.0, 0.0, 14.0, c["m3_clearance_hole_mm"]["easy"], "x", f"{side}_rail_adjustment")
    model.add_warning("Rail hole pitch is unresolved; slots preserve adjustment until rail family is locked.")
    return model


def carriage(data: dict[str, Any], stem: str, axis: str) -> PartModel:
    m = data["prototype_v1"]["motion"]
    c = data["clearances"]
    z = data["prototype_v1"]["layout"]["carriage_plate_z_mm"]
    size = (m["x_carriage_x_mm"], m["x_carriage_y_mm"], z) if axis == "x" else (m["y_carriage_x_mm"], m["y_carriage_y_mm"], z)
    model = create_part(f"{stem}_r001", "petg_structural_motion", size)
    add_centered_plate(model, *model.bbox_mm)
    add_slot_pattern(model, size[0] - 28.0, size[1] - 22.0, 10.0, c["m3_clearance_hole_mm"]["easy"], "x", f"{axis}_rail_carriage_slot")
    model.add_warning("MGN12 carriage hole pattern remains unresolved; slotted features avoid hidden fixed geometry.")
    return model


def slide_holder(data: dict[str, Any]) -> PartModel:
    slide = data["locked_dimensions"]["slide"]
    c = data["clearances"]
    x = slide["slide_x_mm"] + 2 * c["slide_end_clearance_mm"] + 12.0
    y = slide["slide_y_mm"] + 2 * c["slide_side_clearance_mm"] + 12.0
    model = create_part("cbc_slide_holder_r001", "petg_structural_motion", (x, y, 6.0))
    add_centered_plate(model, *model.bbox_mm)
    model.add_feature("recess", "slide_recess", size=[slide["slide_x_mm"] + 2 * c["slide_end_clearance_mm"], slide["slide_y_mm"] + 2 * c["slide_side_clearance_mm"], c["slide_thickness_allowance_max_mm"]])
    add_slot_pattern(model, x - 18.0, y - 14.0, 8.0, c["m3_clearance_hole_mm"]["snug"], "x", "clamp_mount_slots")
    return model


def slide_clamp(data: dict[str, Any], stem: str, side: str) -> PartModel:
    model = create_part(f"{stem}_r001", "petg_structural_motion", (42.0, 8.0, 6.0))
    add_centered_plate(model, *model.bbox_mm)
    model.add_feature("spring_lip", f"{side}_slide_retainer_lip", slide_contact="gentle")
    add_slot(model, 0, 0, 18.0, 3.2, "x", "adjustable_clamp_screw_slot")
    return model


def lead_nut_carrier(data: dict[str, Any], stem: str, axis: str) -> PartModel:
    m = data["prototype_v1"]["motion"]
    c = data["clearances"]
    u = data["unresolved_dimensions"]["lead_screw"]
    model = create_part(f"{stem}_r001", "petg_structural_motion", (m["lead_nut_carrier_x_mm"], m["lead_nut_carrier_y_mm"], m["lead_nut_carrier_z_mm"]))
    add_centered_plate(model, *model.bbox_mm)
    add_slot_pattern(model, 18.0, 12.0, 9.0, c["m3_clearance_hole_mm"]["snug"], axis, f"{axis}_lead_nut_unresolved_slots")
    model.add_warning("T8 nut body and mount hole geometry unresolved; carrier uses parameterized slots.")
    model.metadata["todo"] = u
    return model


def manual_knob(data: dict[str, Any]) -> PartModel:
    m = data["prototype_v1"]["motion"]
    model = create_part("cbc_manual_knob_t8_r001", "petg_structural_motion", (m["manual_knob_d_mm"], m["manual_knob_d_mm"], m["manual_knob_z_mm"]))
    add_cylinder(model, m["manual_knob_d_mm"], m["manual_knob_z_mm"], (0, 0, m["manual_knob_z_mm"] / 2), "knurled_knob_body")
    add_hole(model, 0, 0, 8.2, True, "t8_screw_clearance")
    model.add_feature("grip_texture", "radial_knurl_placeholder", count=24)
    return model


def nema17_mount(data: dict[str, Any], stem: str, axis: str) -> PartModel:
    n = data["locked_dimensions"]["nema17_pololu_2267"]
    c = data["clearances"]
    model = create_part(f"{stem}_r001", "petg_structural_motion", (58.0, 52.0, 8.0))
    add_centered_plate(model, *model.bbox_mm)
    add_hole_pattern(model, n["motor_mount_span_x_mm"], n["motor_mount_span_y_mm"], c["m3_clearance_hole_mm"]["easy"], f"{axis}_nema17_mount")
    add_hole(model, 0, 0, n["shaft_d_mm"] + 8.0, True, "shaft_coupler_clearance")
    return model


def pcb_mount(data: dict[str, Any], stem: str, locked_key: str, material: str = "petg_electronics_mount") -> PartModel:
    board = data["locked_dimensions"][locked_key]
    c = data["clearances"]
    x = board["board_x_mm"] + 2 * c["pcb_side_clearance_mm"] + 10.0
    y = board["board_y_mm"] + 2 * c["pcb_side_clearance_mm"] + 10.0
    model = create_part(f"{stem}_r001", material, (x, y, data["prototype_v1"]["electronics"]["standoff_height_mm"]))
    add_centered_plate(model, *model.bbox_mm)
    if "mount_hole_span_x_mm" in board and "mount_hole_span_y_mm" in board:
        add_hole_pattern(model, board["mount_hole_span_x_mm"], board["mount_hole_span_y_mm"], board.get("mount_hole_dia_mm", 3.2), f"{locked_key}_mount")
    elif "mount_hole_span_x_mm" in board:
        add_slot_pattern(model, board["mount_hole_span_x_mm"], y - 12.0, 10.0, c["m3_clearance_hole_mm"]["easy"], "x", f"{locked_key}_slot_mount")
    else:
        add_slot_pattern(model, board["board_x_mm"] - 8.0, board["board_y_mm"] - 8.0, 10.0, c["m3_clearance_hole_mm"]["easy"], "x", f"{locked_key}_unlocked_mount_slots")
        model.add_warning(f"{locked_key} hole pattern unresolved; board tray uses adjustable retention slots.")
    return model


def permaproto_tray(data: dict[str, Any]) -> PartModel:
    model = pcb_mount(data, "cbc_permaproto_tray", "permaproto_quarter")
    model.add_feature("tray_walls", "low_retaining_walls", wall_mm=data["prototype_v1"]["electronics"]["tray_wall_mm"])
    return model


def cable_clip(data: dict[str, Any]) -> PartModel:
    model = create_part("cbc_cable_clip_r001", "petg_electronics_mount", (18.0, 12.0, 10.0))
    add_centered_plate(model, *model.bbox_mm)
    model.add_feature("flex_clip", "ribbon_or_jumper_wire_retainer", cable_bundle_d_mm=5.0)
    add_hole(model, 0, -3.0, 3.4, True, "m3_mount")
    return model


def rms_thread_coupon(data: dict[str, Any]) -> PartModel:
    optics = data["locked_dimensions"]["optics"]
    offset = data["unresolved_dimensions"]["objective_amscope_40x"]["thread_print_offset_mm"]
    major_mm = optics["objective_rms_major_diameter_in"] * 25.4 + offset
    model = create_part("cbc_rms_thread_coupon_r001", "matte_black_petg_coupon", (36.0, 36.0, 10.0))
    add_centered_plate(model, *model.bbox_mm)
    add_hole(model, 0, 0, major_mm, True, "rms_test_thread_bore")
    model.metadata["purpose"] = "Print before objective holder to tune RMS thread compensation."
    return model


def m3_insert_coupon(data: dict[str, Any]) -> PartModel:
    c = data["clearances"]
    model = create_part("cbc_m3_insert_coupon_r001", "coupon_target_material", (45.0, 18.0, 8.0))
    add_centered_plate(model, *model.bbox_mm)
    for idx, dia in enumerate((3.8, c["m3_insert_pilot_mm"], 4.2), start=1):
        add_hole(model, -15.0 + idx * 10.0, 0, dia, False, f"insert_pilot_{dia:g}mm")
    model.metadata["purpose"] = "Validate heat-set insert pilot diameter in final material."
    return model


def part_by_stem(stem: str, data: dict[str, Any]) -> PartModel:
    if stem == "cbc_baseplate":
        return baseplate(data)
    if stem == "cbc_optical_tower":
        return optical_tower(data)
    if stem == "cbc_camera_mount_imx296":
        return camera_mount_imx296(data)
    if stem == "cbc_camera_mount_rpi_gs":
        return camera_mount_rpi_gs(data)
    if stem == "cbc_objective_holder_rms":
        return objective_holder(data)
    if stem == "cbc_optical_tube_section":
        return optical_tube(data)
    if stem == "cbc_led_ring_holder":
        return led_ring(data)
    if stem == "cbc_diffuser_frame":
        return diffuser_frame(data)
    if stem in ("cbc_x_rail_support_left", "cbc_x_rail_support_right", "cbc_y_rail_support_front", "cbc_y_rail_support_rear"):
        return rail_support(data, stem, stem.replace("cbc_", ""))
    if stem == "cbc_x_carriage":
        return carriage(data, stem, "x")
    if stem == "cbc_y_carriage":
        return carriage(data, stem, "y")
    if stem == "cbc_slide_holder":
        return slide_holder(data)
    if stem in ("cbc_slide_clamp_left", "cbc_slide_clamp_right"):
        return slide_clamp(data, stem, stem.rsplit("_", 1)[-1])
    if stem == "cbc_lead_nut_carrier_x":
        return lead_nut_carrier(data, stem, "x")
    if stem == "cbc_lead_nut_carrier_y":
        return lead_nut_carrier(data, stem, "y")
    if stem == "cbc_manual_knob_t8":
        return manual_knob(data)
    if stem == "cbc_nema17_mount_x":
        return nema17_mount(data, stem, "x")
    if stem == "cbc_nema17_mount_y":
        return nema17_mount(data, stem, "y")
    if stem == "cbc_pi4_mount":
        return pcb_mount(data, stem, "pi4")
    if stem == "cbc_pico_mount":
        return pcb_mount(data, stem, "pico")
    if stem == "cbc_tlc5947_mount":
        return pcb_mount(data, stem, "tlc5947")
    if stem == "cbc_permaproto_tray":
        return permaproto_tray(data)
    if stem == "cbc_cable_clip":
        return cable_clip(data)
    if stem == "cbc_rms_thread_coupon":
        return rms_thread_coupon(data)
    if stem == "cbc_m3_insert_coupon":
        return m3_insert_coupon(data)
    raise KeyError(stem)
