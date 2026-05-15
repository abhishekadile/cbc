from __future__ import annotations

from cad.scripts.common.envelopes import add_box_envelope
from cad.scripts.common.exports import export_model
from cad.scripts.common.naming import filename
from cad.scripts.common.params import load_all
from cad.scripts.common.part_templates import part_by_stem
from cad.scripts.assemblies.cbc_prototype_manual import PRINTED_PARTS, build as build_manual


STEPPER_EXTRA_PARTS = ["cbc_nema17_mount_x", "cbc_nema17_mount_y"]


def build(data=None):
    data = data or load_all()
    assembly = build_manual(data)
    assembly.name = "cbc_prototype_stepper_r001"
    assembly.metadata["variant"] = "optional_nema17_motorized_xy"
    assembly.metadata["printed_parts"] = [part_by_stem(stem, data).name for stem in PRINTED_PARTS + STEPPER_EXTRA_PARTS]
    n = data["locked_dimensions"]["nema17_pololu_2267"]
    add_box_envelope(assembly, "x_nema17_motor_envelope", n["face_x_mm"], n["face_y_mm"], n["body_length_mm"], (95, -35, 36), "Pololu 2267 NEMA17")
    add_box_envelope(assembly, "y_nema17_motor_envelope", n["face_x_mm"], n["face_y_mm"], n["body_length_mm"], (-55, 85, 50), "Pololu 2267 NEMA17")
    assembly.add_warning("Stepper driver footprint is not locked; keep A4988/TMC2209 on electronics tray or perfboard.")
    return assembly


if __name__ == "__main__":
    from pathlib import Path

    export_model(build(), Path(__file__).resolve().parents[2] / "f3d" / "assemblies" / filename("cbc_prototype_stepper", "f3d"))
