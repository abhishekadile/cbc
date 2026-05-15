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
python -m cad.scripts.tools.build_stage1
python -m pytest cad/tests
```

`build_all_parts`, `build_all_assemblies`, and `build_stage1` are safe offline commands. They build deterministic specs/reports and do not create manufacturing STL/STEP files outside Fusion.

Fusion bridge smoke tests assume the existing local MCP/Fusion bridge is active at:

```text
http://127.0.0.1:8765
```

Stage 1 generated naming follows:

- Native assembly: `cbc_stage1_static_optical_stack_r001.f3d`
- STEP part: `cbc_slide_holder_r001.step`
- STL part: `cbc_slide_holder_r001.stl`

## Real Fusion Exports vs Offline Specs

Only files generated inside Autodesk Fusion through `ExportManager` should be treated as printable/manufacturing CAD.

Offline Python runs may write deterministic `.non_printable_spec.json` files for validation and CI. Those files are not STL/STEP manufacturing outputs.

The first real printable Fusion part implemented is:

```powershell
python -m cad.scripts.parts.cbc_slide_holder
```

Run that command from Fusion's Python environment, or run the script through Fusion's Scripts and Add-Ins workflow. When Fusion is live, it creates a separate component/body named `cbc_slide_holder_r001` and exports:

- `cad/exports/stl/cbc_slide_holder_r001.stl`
- `cad/exports/step/cbc_slide_holder_r001.step`

When run outside Fusion, the same command writes only a non-printable JSON spec and does not claim to create printable CAD.

For the full Stage 1 export set, run this from Fusion's Python environment:

```powershell
python -m cad.scripts.tools.export_stage1
```

Outside Fusion, `export_stage1` and `export_all` refuse with a `RuntimeError` and do not write placeholder manufacturing files.
