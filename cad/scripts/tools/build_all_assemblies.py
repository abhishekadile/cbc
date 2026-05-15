from __future__ import annotations

from pathlib import Path

from cad.scripts.assemblies import cbc_prototype_manual, cbc_prototype_stepper
from cad.scripts.common.exports import export_model
from cad.scripts.common.naming import filename
from cad.scripts.common.params import load_all


CAD_ROOT = Path(__file__).resolve().parents[2]


def build_all_assemblies():
    data = load_all()
    assemblies = [
        ("cbc_prototype_manual", cbc_prototype_manual.build(data)),
        ("cbc_prototype_stepper", cbc_prototype_stepper.build(data)),
    ]
    for stem, model in assemblies:
        export_model(model, CAD_ROOT / "f3d" / "assemblies" / filename(stem, "f3d"))
    return [model for _, model in assemblies]


if __name__ == "__main__":
    for model in build_all_assemblies():
        print(model.name)
