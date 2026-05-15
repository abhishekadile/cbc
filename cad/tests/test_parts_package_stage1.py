from importlib import import_module

from cad.scripts.parts import PART_STEMS


def test_stage1_parts_package_is_limited_to_implemented_wrappers():
    assert PART_STEMS == [
        "cbc_baseplate",
        "cbc_slide_holder",
        "cbc_pi4_mount",
        "cbc_camera_mount_rpi_gs",
        "cbc_objective_holder_placeholder",
        "cbc_optical_axis_datum",
    ]


def test_stage1_part_wrappers_expose_build_functions():
    for stem in PART_STEMS:
        module = import_module(f"cad.scripts.parts.{stem}")
        assert callable(module.build)
        assert callable(module.build_fusion)
