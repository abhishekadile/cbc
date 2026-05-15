from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from cad.scripts.common.params import CAD_ROOT, load_all
from cad.scripts.common.exports import export_component
from cad.scripts.common.fusion_context import create_context, write_spec
from cad.scripts.common.stage1_geometry import build_slide_holder_fusion, slide_holder_spec

STEM = "cbc_slide_holder"


def build(data=None):
    return slide_holder_spec(data or load_all())


def build_fusion(ctx, data=None):
    return build_slide_holder_fusion(ctx, data or load_all())


def build_and_export():
    data = load_all()
    model = build(data)
    ctx = create_context("cbc_slide_holder_r001")
    if ctx.is_live_fusion:
        component = build_fusion(ctx, data)
        return export_component(
            ctx,
            component,
            CAD_ROOT / "exports" / "stl" / "cbc_slide_holder_r001.stl",
            CAD_ROOT / "exports" / "step" / "cbc_slide_holder_r001.step",
        )
    spec_path = CAD_ROOT / "f3d" / "parts" / "cbc_slide_holder_r001.non_printable_spec.json"
    write_spec(model, spec_path)
    return [spec_path]


def run(context):
    build_and_export()


def stop(context):
    return None


if __name__ == "__main__":
    for output in build_and_export():
        print(output)
