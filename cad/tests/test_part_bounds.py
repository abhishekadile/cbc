import importlib

from cad.scripts.common.assertions import assert_bbox_within, assert_positive_bbox
from cad.scripts.common.params import load_all
from cad.scripts.parts import PART_STEMS


def test_all_parts_build_and_fit_system_bounds():
    data = load_all()
    system = data["locked_dimensions"]["system"]
    for stem in PART_STEMS:
        module = importlib.import_module(f"cad.scripts.parts.{stem}")
        model = module.build(data)
        assert_positive_bbox(model)
        assert_bbox_within(
            model,
            system["max_footprint_x_mm"],
            system["max_footprint_y_mm"],
            system["max_height_mm"],
        )
        assert model.name.endswith("_r001")
        assert model.features
