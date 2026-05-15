from __future__ import annotations

import importlib
from pathlib import Path

from cad.scripts.assemblies import cbc_prototype_manual, cbc_prototype_stepper
from cad.scripts.common.exports import export_model
from cad.scripts.common.naming import filename
from cad.scripts.common.params import load_all
from cad.scripts.parts import PART_STEMS


CAD_ROOT = Path(__file__).resolve().parents[2]


def export_all():
    data = load_all()
    outputs = []
    for stem in PART_STEMS:
        module = importlib.import_module(f"cad.scripts.parts.{stem}")
        model = module.build(data)
        outputs.append(export_model(model, CAD_ROOT / "exports" / "stl" / filename(stem, "stl")))
        outputs.append(export_model(model, CAD_ROOT / "exports" / "step" / filename(stem, "step")))

    for stem, model in (
        ("cbc_prototype_manual", cbc_prototype_manual.build(data)),
        ("cbc_prototype_stepper", cbc_prototype_stepper.build(data)),
    ):
        outputs.append(export_model(model, CAD_ROOT / "exports" / "f3d" / filename(stem, "f3d")))
        outputs.append(export_model(model, CAD_ROOT / "exports" / "step" / filename(stem, "step")))
    return outputs


if __name__ == "__main__":
    for path in export_all():
        print(path)
