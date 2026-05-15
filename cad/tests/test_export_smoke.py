from pathlib import Path

from cad.scripts.assemblies.cbc_prototype_manual import build as build_manual
from cad.scripts.common.exports import export_model
from cad.scripts.common.naming import filename
from cad.scripts.common.params import load_all
from cad.scripts.parts.cbc_baseplate import build as build_baseplate


def test_export_one_part_and_one_assembly():
    data = load_all()
    cad_root = Path(__file__).resolve().parents[1]

    part = build_baseplate(data)
    assembly = build_manual(data)

    outputs = [
        export_model(part, cad_root / "exports" / "stl" / filename("cbc_baseplate", "stl")),
        export_model(part, cad_root / "exports" / "step" / filename("cbc_baseplate", "step")),
        export_model(part, cad_root / "f3d" / "parts" / filename("cbc_baseplate", "f3d")),
        export_model(assembly, cad_root / "exports" / "f3d" / filename("cbc_prototype_manual", "f3d")),
        export_model(assembly, cad_root / "exports" / "step" / filename("cbc_prototype_manual", "step")),
    ]

    for path in outputs:
        assert path.exists()
        assert path.stat().st_size > 0
