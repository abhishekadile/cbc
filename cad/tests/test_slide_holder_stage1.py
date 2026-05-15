from cad.scripts.common.params import load_all
from cad.scripts.parts.cbc_slide_holder import build


def test_slide_holder_pocket_uses_locked_slide_clearances():
    data = load_all()
    assert data["locked_dimensions"]["slide"]["pocket_x_mm"] == 76.0
    assert data["locked_dimensions"]["slide"]["pocket_y_mm"] == 25.6
    model = build(data)
    pocket = model.metadata["calculated_slide_pocket_mm"]
    assert pocket["x"] == 76.0
    assert pocket["y"] == 25.6


def test_slide_holder_has_required_functional_features():
    model = build(load_all())
    feature_kinds = [feature.kind for feature in model.features]
    feature_names = [feature.name for feature in model.features]

    assert "extrude_box" in feature_kinds
    assert "slide_pocket" in feature_kinds
    assert "viewing_window" in feature_kinds
    assert feature_names.count("left_clamp_retainer_slot") == 1
    assert feature_names.count("right_clamp_retainer_slot") == 1
    assert sum(1 for name in feature_names if name.startswith("m3_mounting_holes_")) == 4
