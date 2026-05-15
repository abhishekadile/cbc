from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from cad.scripts.assemblies.cbc_stage1_static_optical_stack import build, build_fusion
from cad.scripts.common.fusion_context import create_context
from cad.scripts.common.params import CAD_ROOT, load_all, unresolved_paths
from cad.scripts.parts import (
    cbc_baseplate,
    cbc_camera_mount_rpi_gs,
    cbc_objective_holder_placeholder,
    cbc_optical_axis_datum,
    cbc_pi4_mount,
    cbc_slide_holder,
)


PART_MODULES = [
    cbc_baseplate,
    cbc_slide_holder,
    cbc_pi4_mount,
    cbc_camera_mount_rpi_gs,
    cbc_objective_holder_placeholder,
    cbc_optical_axis_datum,
]


def write_stage1_reports(data) -> None:
    reports = CAD_ROOT / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    assembly = build(data)
    locked = data["locked_dimensions"]
    stage = data["prototype_v1"]["stage1"]
    (reports / "stage1_dimensions_report.md").write_text(
        "\n".join([
            "# Stage 1 Dimensions Report",
            "",
            "## Locked Geometry",
            f"- Baseplate: {locked['system']['stage1_baseplate_x_mm']} x {locked['system']['stage1_baseplate_y_mm']} x {locked['system']['stage1_baseplate_z_mm']} mm.",
            f"- Slide pocket: {locked['slide']['pocket_x_mm']} x {locked['slide']['pocket_y_mm']} mm for a 75 x 25 mm slide.",
            f"- Viewing window: {locked['slide']['viewing_window_x_mm']} x {locked['slide']['viewing_window_y_mm']} mm.",
            f"- Pi 4 board nest: {locked['pi4']['board_nest_x_mm']} x {locked['pi4']['board_nest_y_mm']} mm.",
            f"- Pi 4 mount span: {locked['pi4']['mount_hole_span_x_mm']} x {locked['pi4']['mount_hole_span_y_mm']} mm.",
            f"- RPi GS camera board nest: {locked['camera_rpi_gs']['board_nest_x_mm']} x {locked['camera_rpi_gs']['board_nest_y_mm']} mm.",
            f"- RPi GS camera hole span: {locked['camera_rpi_gs']['mount_hole_span_x_mm']} x {locked['camera_rpi_gs']['mount_hole_span_y_mm']} mm.",
            f"- Optical axis location: X={stage['optical_axis_x_mm']} mm, Y={stage['optical_axis_y_mm']} mm.",
            f"- Objective shoulder to sensor plane datum: {locked['optics']['objective_shoulder_to_sensor_plane_mm']} mm.",
            "",
            "## Assembly Warnings",
            *(f"- {warning}" for warning in assembly.warnings),
            "",
        ]),
        encoding="utf-8",
    )
    unresolved = unresolved_paths(data)
    (reports / "unresolved_dimensions.md").write_text(
        "# Unresolved Dimensions\n\n"
        + "\n".join(f"- `{path}`" for path in unresolved)
        + "\n\nThese remain unresolved by design. Do not replace slots/placeholders with fixed geometry until measured or backed by reliable vendor drawings.\n",
        encoding="utf-8",
    )


def build_stage1():
    data = load_all()
    write_stage1_reports(data)
    specs = [module.build(data) for module in PART_MODULES]
    specs.append(build(data))
    ctx = create_context("cbc_stage1_static_optical_stack_r001")
    if ctx.is_live_fusion:
        build_fusion(ctx, data)
    return specs


if __name__ == "__main__":
    for item in build_stage1():
        print(item.name)
