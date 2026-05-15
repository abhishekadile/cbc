from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from cad.scripts.assemblies import cbc_stage1_static_optical_stack
from cad.scripts.common.exports import export_component, export_design_step, save_design_f3d
from cad.scripts.common.fusion_context import create_context
from cad.scripts.common.params import CAD_ROOT, load_all


PRINTED_EXPORTS = {
    "baseplate": "cbc_baseplate_r001",
    "slide_holder": "cbc_slide_holder_r001",
    "pi4_mount": "cbc_pi4_mount_r001",
    "camera_mount": "cbc_camera_mount_rpi_gs_r001",
    "objective_holder_placeholder": "cbc_objective_holder_placeholder_r001",
}


def export_stage1():
    data = load_all()
    ctx = create_context("cbc_stage1_static_optical_stack_r001")
    if not ctx.is_live_fusion:
        raise RuntimeError(
            "Real Stage 1 exports require running this script inside Autodesk Fusion. "
            "No placeholder STL/STEP files were written."
        )

    components = cbc_stage1_static_optical_stack.build_fusion(ctx, data)
    exported: list[Path] = []
    for key, stem in PRINTED_EXPORTS.items():
        component = components[key]
        exported.extend(
            export_component(
                ctx,
                component,
                CAD_ROOT / "exports" / "stl" / f"{stem}.stl",
                CAD_ROOT / "exports" / "step" / f"{stem}.step",
            )
        )

    exported.append(export_design_step(ctx, CAD_ROOT / "exports" / "step" / "cbc_stage1_static_optical_stack_r001.step"))
    exported.append(save_design_f3d(ctx, CAD_ROOT / "exports" / "f3d" / "cbc_stage1_static_optical_stack_r001.f3d"))
    return exported


if __name__ == "__main__":
    for path in export_stage1():
        print(path)
