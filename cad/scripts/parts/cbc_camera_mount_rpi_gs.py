from cad.scripts.common.params import load_all
from cad.scripts.common.fusion_context import write_spec
from cad.scripts.common.stage1_geometry import build_camera_mount_rpi_gs_fusion, camera_mount_rpi_gs_spec
STEM = "cbc_camera_mount_rpi_gs"
def build(data=None):
    return camera_mount_rpi_gs_spec(data or load_all())
def build_fusion(ctx, data=None):
    return build_camera_mount_rpi_gs_fusion(ctx, data or load_all())
if __name__ == "__main__":
    from cad.scripts.common.params import CAD_ROOT

    path = CAD_ROOT / "f3d" / "parts" / f"{STEM}_r001.non_printable_spec.json"
    write_spec(build(), path)
    print(path)
