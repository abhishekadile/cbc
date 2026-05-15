from cad.scripts.common.fusion_context import write_spec
from cad.scripts.common.params import load_all
from cad.scripts.common.stage1_geometry import build_optical_axis_datum_fusion, optical_axis_datum_spec

STEM = "cbc_optical_axis_datum"


def build(data=None):
    return optical_axis_datum_spec(data or load_all())


def build_fusion(ctx, data=None):
    return build_optical_axis_datum_fusion(ctx, data or load_all())


if __name__ == "__main__":
    from cad.scripts.common.params import CAD_ROOT

    path = CAD_ROOT / "f3d" / "parts" / f"{STEM}_r001.non_printable_spec.json"
    write_spec(build(), path)
    print(path)
