from cad.scripts.assemblies.cbc_prototype_manual import build
from cad.scripts.common.assertions import assert_optical_stack
from cad.scripts.common.params import load_all
from cad.scripts.parts.cbc_optical_tube_section import build as build_tube


def test_optical_stack_is_160mm():
    data = load_all()
    tube = build_tube(data)
    terms = tube.metadata["stack_terms_mm"]
    distance = terms["objective_holder"] + terms["tube"] + terms["camera_mount_face_to_sensor"]
    assert_optical_stack(distance)


def test_assembly_has_fov_and_scan_steps():
    assembly = build(load_all())
    imaging = assembly.metadata["derived_imaging"]
    assert imaging["fov_x_um"] > 0
    assert imaging["fov_y_um"] > 0
    assert "50_percent_overlap" in imaging["scan_steps_um"]
