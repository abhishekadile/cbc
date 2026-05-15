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
    clearances = data["clearances"]
    pocket_x = locked["slide"]["slide_x_mm"] + 2 * clearances["slide_end_clearance_mm"]
    pocket_y = locked["slide"]["slide_y_mm"] + 2 * clearances["slide_side_clearance_mm"]
    corrected = []
    if locked["slide"]["pocket_x_mm"] == pocket_x and locked["slide"]["pocket_y_mm"] == pocket_y:
        corrected.append(
            f"Slide pocket corrected and locked at {pocket_x:.1f} x {pocket_y:.1f} mm "
            f"from slide size plus end/side clearances."
        )
    corrected.append(
        "Perma-Proto Quarter dimensions corrected to the Adafruit 1608 policy values: "
        "50.8 x 43.0 x 1.6 mm with a two-hole 35.56 mm span."
    )
    (reports / "stage1_dimensions_report.md").write_text(
        "\n".join([
            "# Stage 1 Dimensions Report",
            "",
            "Stage 1 is a static optical/base assembly. It is not the final XY-motion microscope and does not freeze unresolved vendor geometry.",
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
            "## Corrections Applied",
            *(f"- {item}" for item in corrected),
            "",
            "## Real Export Policy",
            "- `build_stage1` writes reports/spec metadata and may build live Fusion geometry when run inside Fusion.",
            "- Manufacturing STL/STEP/F3D files are written only by `export_stage1` through Fusion ExportManager.",
            "- Offline placeholder manufacturing files are intentionally not produced.",
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
        + "\n\nThese remain unresolved by design. Do not replace slots/placeholders with fixed geometry until measured or backed by reliable vendor drawings.\n\n"
        + "## Measure Before Stage 2\n\n"
        + "- InnovaMaker IMX296 board outline, mounting pattern, thickness, and sensor-plane offset.\n"
        + "- AmScope 40X objective shoulder geometry, body outer diameter, body length, and any printed thread compensation.\n"
        + "- Raspberry Pi 4 connector keepout zones for the exact board revision used.\n"
        + "- Raspberry Pi Pico and TLC5947 mounting-hole positions if dedicated board mounts are added.\n"
        + "- Perma-Proto Quarter product ID/orientation if a retained tray replaces simple slots or walls.\n"
        + "- Rail, carriage, T8 lead nut, and motor pilot dimensions before Stage 2 XY-motion CAD.\n",
        encoding="utf-8",
    )
    (reports / "dimensions_locked.md").write_text(
        "\n".join([
            "# Locked Dimensions",
            "",
            "## Exact / Locked",
            "- System envelope: `200 x 200 x 300 mm` maximum.",
            "- Stage 1 baseplate: `180 x 160 x 6 mm` with `8 mm` corner radius.",
            f"- Slide: `{locked['slide']['slide_x_mm']} x {locked['slide']['slide_y_mm']} mm`.",
            f"- Slide pocket: `{locked['slide']['pocket_x_mm']} x {locked['slide']['pocket_y_mm']} mm`, derived from slide size plus clearances.",
            f"- Viewing window: `{locked['slide']['viewing_window_x_mm']} x {locked['slide']['viewing_window_y_mm']} mm`.",
            "- Finite objective stack datum: objective shoulder to sensor plane = `160.0 mm`.",
            "- RMS objective standard: `0.8 in x 36 TPI`; printed thread fit is still coupon-gated.",
            "- Raspberry Pi Global Shutter camera: `38 x 38 mm` board, `30 x 30 mm` hole span, `2.5 mm` holes.",
            "- Raspberry Pi 4: `85 x 56 mm` board, `58 x 49 mm` hole span, `2.7 mm` holes.",
            "- Raspberry Pi Pico board envelope only: `51.3 x 21.0 x 3.9 mm`.",
            "- TLC5947 board envelope only: `51.1 x 25.39 x 4.0 mm`.",
            "- Perma-Proto Quarter policy values: `50.8 x 43.0 x 1.6 mm`, two mounting holes `35.56 mm` apart.",
            "- Pololu 2267 NEMA17 envelope: `42.3 x 42.3 x 38.0 mm`, `5.0 mm` shaft, `31 x 31 mm` mount span.",
            "",
            "## Corrections",
            "- Slide pocket X was corrected from `75.5 mm` to `76.0 mm` because end clearance is applied at both slide ends.",
            "- Perma-Proto Quarter was corrected from the earlier `55 x 44 mm` placeholder to the Adafruit 1608 policy dimensions.",
            "- Pico and TLC5947 mounting-hole spans are not locked here; they remain unresolved unless backed by a mechanical drawing or measurement.",
            "",
            "## Verification Notes",
            "- Verify Raspberry Pi 4 connector keepout zones against the specific Raspberry Pi 4 revision before final enclosure design.",
            "- The BOM/product ID for the Perma-Proto Quarter must be checked before final tray geometry; Stage 1 avoids a four-hole rectangular assumption.",
        ]),
        encoding="utf-8",
    )
    (reports / "bom_to_cad_mapping.md").write_text(
        "\n".join([
            "# BOM to CAD Mapping",
            "",
            "| Bought part | Stage | CAD relationship |",
            "| --- | --- | --- |",
            "| Glass microscope slide | Stage 1 | Held by `cbc_slide_holder_r001`; uses a removable pocket, window, M3 holes, and retainer slots. |",
            "| Raspberry Pi 4 | Stage 1 | Mounted by `cbc_pi4_mount_r001`; board envelope and hole span are locked, connector keepouts remain to verify. |",
            "| Raspberry Pi Global Shutter Camera | Stage 1 | Mounted by `cbc_camera_mount_rpi_gs_r001`; board and hole pattern are locked, sensor-plane offset remains unresolved. |",
            "| AmScope 40X RMS objective | Stage 1 placeholder | Represented by `cbc_objective_holder_placeholder_r001`; this is not a final RMS threaded holder. |",
            "| Optical axis / sensor datum | Stage 1 | Represented by `cbc_optical_axis_datum_r001` for alignment only, not a printed manufacturing part. |",
            "| InnovaMaker IMX296 camera | Stage 2 | Future alternate camera mount; actual board and sensor offset must be measured. |",
            "| MGN12 rails/carriages | Stage 2 | Future XY-motion rail supports and carriages; exact holes remain unresolved. |",
            "| T8 lead screws and nuts | Stage 2 | Future lead-nut carriers and knobs; nut body and hole pattern remain unresolved. |",
            "| NEMA17 steppers | Stage 2 optional | Future motor mounts; shaft length and pilot boss geometry remain unresolved. |",
            "| Raspberry Pi Pico | Stage 2 electronics | Board envelope locked; mount holes unresolved. |",
            "| Adafruit TLC5947 | Stage 2 electronics | Board envelope locked; mount holes unresolved. |",
            "| Adafruit Perma-Proto Quarter | Stage 2 electronics | Two-hole board policy dimensions locked; tray orientation/product ID must be verified. |",
            "| M3 screws and heat-set inserts | Stage 1/2 | Clearance and pilot parameters are in `clearances.yaml`; insert pilot is insert-dependent and should be coupon-tested. |",
        ]),
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
