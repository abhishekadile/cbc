from cad.scripts.common.params import load_all


def test_yaml_schema_required_keys():
    data = load_all()
    assert data["locked_dimensions"]["system"]["max_footprint_x_mm"] == 200.0
    assert data["locked_dimensions"]["optics"]["objective_shoulder_to_sensor_plane_mm"] == 160.0
    assert data["locked_dimensions"]["camera_rpi_gs"]["mount_hole_span_x_mm"] == 30.0
    assert data["unresolved_dimensions"]["camera_innomaker_imx296"]["board_x_mm"] is None
    assert data["clearances"]["m3_clearance_hole_mm"]["easy"] == 3.4
    assert data["prototype_v1"]["exports"]["part_revision"] == "r001"
