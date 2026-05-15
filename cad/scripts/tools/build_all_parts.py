from __future__ import annotations

import importlib
from pathlib import Path

from cad.scripts.common.exports import export_model
from cad.scripts.common.naming import filename
from cad.scripts.common.params import load_all
from cad.scripts.parts import PART_STEMS


CAD_ROOT = Path(__file__).resolve().parents[2]


def build_all_parts():
    data = load_all()
    built = []
    for stem in PART_STEMS:
        module = importlib.import_module(f"cad.scripts.parts.{stem}")
        model = module.build(data)
        export_model(model, CAD_ROOT / "f3d" / "parts" / filename(stem, "f3d"))
        built.append(model)
    return built


if __name__ == "__main__":
    for model in build_all_parts():
        print(model.name)
