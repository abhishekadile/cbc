# CBC Microscope Prototype CAD

This `cad/` system contains Fusion-oriented Python scripts for the custom printed parts and simplified assemblies for the CBC microscope prototype.

Design policy:

- Bought precision parts stay bought: optics, rails, lead screws/nuts, boards, screws, inserts, motors, and drivers.
- Printed parts are modular bolt-together components, not a monolithic frame.
- Manual XY is the first assembly variant; NEMA17 motorized XY is optional.
- The optical datum is the sensor plane. For the finite objective path, objective shoulder to sensor plane is held at `160.0 mm`.
- Unresolved vendor geometry remains parameterized and uses slots or placeholders.
- No arbitrary shell execution, subprocess command runner, or network code is present in this CAD tree.

Key commands from the repo root:

```powershell
python -m cad.scripts.tools.build_all_parts
python -m cad.scripts.tools.build_all_assemblies
python -m cad.scripts.tools.export_all
python -m pytest cad/tests
```

Fusion bridge smoke tests assume the existing local MCP/Fusion bridge is active at:

```text
http://127.0.0.1:8765
```

Generated naming follows:

- Native: `cbc_x_carriage_r001.f3d`
- STEP: `cbc_x_carriage_r001.step`
- STL: `cbc_x_carriage_r001.stl`
- Assemblies: `cbc_prototype_manual_r001.*`, `cbc_prototype_stepper_r001.*`

The offline exports are deterministic script-spec placeholders when Autodesk Fusion is not executing the scripts. The same scripts are organized around Fusion concepts: sketches, extrudes, holes, slots, bought-part envelopes, and ExportManager-compatible export boundaries.
