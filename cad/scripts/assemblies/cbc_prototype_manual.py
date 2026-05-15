from __future__ import annotations

from cad.scripts.common.envelopes import add_box_envelope, add_cylinder_envelope
from cad.scripts.common.exports import export_model
from cad.scripts.common.fusion_context import create_part
from cad.scripts.common.naming import filename
from cad.scripts.common.params import load_all, unresolved_paths
from cad.scripts.common.part_templates import part_by_stem


PRINTED_PARTS = [
    "cbc_baseplate",
    "cbc_optical_tower",
    "cbc_camera_mount_imx296",
    "cbc_objective_holder_rms",
    "cbc_optical_tube_section",
    "cbc_led_ring_holder",
    "cbc_diffuser_frame",
    "cbc_x_rail_support_left",
    "cbc_x_rail_support_right",
    "cbc_y_rail_support_front",
    "cbc_y_rail_support_rear",
    "cbc_x_carriage",
    "cbc_y_carriage",
    "cbc_slide_holder",
    "cbc_slide_clamp_left",
    "cbc_slide_clamp_right",
    "cbc_lead_nut_carrier_x",
    "cbc_lead_nut_carrier_y",
    "cbc_manual_knob_t8",
    "cbc_pi4_mount",
    "cbc_pico_mount",
    "cbc_tlc5947_mount",
    "cbc_permaproto_tray",
    "cbc_cable_clip",
]


def derived_imaging(data):
    cam = data["locked_dimensions"]["camera_rpi_gs"]
    mag = data["locked_dimensions"]["optics"]["objective_nominal_mag"]
    fov_x_um = cam["sensor_resolution_x_px"] * cam["pixel_pitch_um"] / mag
    fov_y_um = cam["sensor_resolution_y_px"] * cam["pixel_pitch_um"] / mag
    return {
        "fov_x_um": fov_x_um,
        "fov_y_um": fov_y_um,
        "scan_steps_um": {
            "40_percent_overlap": {"x": fov_x_um * 0.60, "y": fov_y_um * 0.60},
            "50_percent_overlap": {"x": fov_x_um * 0.50, "y": fov_y_um * 0.50},
            "60_percent_overlap": {"x": fov_x_um * 0.40, "y": fov_y_um * 0.40},
        },
    }


def build(data=None):
    data = data or load_all()
    assembly = create_part("cbc_prototype_manual_r001", "assembly_reference", (190.0, 180.0, 245.0))
    assembly.metadata["printed_parts"] = [part_by_stem(stem, data).name for stem in PRINTED_PARTS]
    assembly.metadata["variant"] = "manual_xy"
    assembly.metadata["optical_stack_mm"] = part_by_stem("cbc_optical_tube_section", data).metadata
    assembly.metadata["derived_imaging"] = derived_imaging(data)

    add_box_envelope(assembly, "glass_slide_75x25", 75.0, 25.0, 1.2, (0, 0, 35), "locked standard slide")
    add_box_envelope(assembly, "raspberry_pi_4_envelope", 85.0, 56.0, 18.0, (55, -55, 22), "locked board outline")
    add_box_envelope(assembly, "pico_envelope", 51.3, 21.0, 8.0, (55, -10, 18), "locked board outline")
    add_box_envelope(assembly, "tlc5947_envelope", 51.1, 25.39, 8.0, (55, -30, 18), "locked board outline")
    add_cylinder_envelope(assembly, "objective_envelope_todo", 28.0, 45.0, (0, 20, 140), "z", "unresolved objective body")
    add_cylinder_envelope(assembly, "x_t8_lead_screw_envelope", 8.0, 190.0, (0, -35, 28), "x", "bought T8 lead screw")
    add_cylinder_envelope(assembly, "y_t8_lead_screw_envelope", 8.0, 140.0, (-35, 0, 42), "y", "bought T8 lead screw")
    add_box_envelope(assembly, "mgn12_x_rail_envelope_pair", 190.0, 12.0, 8.0, (0, -50, 20), "bought MGN12 rail")
    add_box_envelope(assembly, "mgn12_y_rail_envelope_pair", 12.0, 140.0, 8.0, (-45, 0, 36), "bought MGN12 rail")

    unresolved_motion = [p for p in unresolved_paths(data) if ".rail_system." in p or ".lead_screw." in p]
    if unresolved_motion:
        assembly.add_warning("Unresolved motion dimensions remain: " + ", ".join(unresolved_motion))
    return assembly


if __name__ == "__main__":
    from pathlib import Path

    export_model(build(), Path(__file__).resolve().parents[2] / "f3d" / "assemblies" / filename("cbc_prototype_manual", "f3d"))
