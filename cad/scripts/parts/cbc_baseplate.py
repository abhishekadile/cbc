from cad.scripts.common.params import load_all
from cad.scripts.common.fusion_context import write_spec
from cad.scripts.common.stage1_geometry import baseplate_spec, build_baseplate_fusion

STEM = "cbc_baseplate"

def build(data=None):
    return baseplate_spec(data or load_all())

def build_fusion(ctx, data=None):
    return build_baseplate_fusion(ctx, data or load_all())

if __name__ == "__main__":
    from cad.scripts.common.params import CAD_ROOT

    path = CAD_ROOT / "f3d" / "parts" / f"{STEM}_r001.non_printable_spec.json"
    write_spec(build(), path)
    print(path)
