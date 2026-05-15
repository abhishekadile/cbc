# Current Fusion Output Audit

The current Fusion model built through the bridge is a smoke-test / concept placeholder only.

It is not printable CAD and must not be used for assembly, manufacturing, fit checks, or procurement decisions.

Observed issues:

- The model is made from generic boxes, cylinders, and rough envelope bodies.
- It lacks real functional interfaces such as engineered mounting holes, heat-set insert bosses, board nests, pockets, cable reliefs, and controlled tolerances.
- It does not contain separate production-ready printable components with validated export boundaries.
- It does not encode actual assembly constraints or verified purchased-part interfaces.
- It includes placeholder envelopes for unresolved components, but those envelopes are not final vendor geometry.
- It should not be exported as final STL, STEP, or F3D manufacturing data.

Disposition:

- Supersede this model with the parametric Stage 1 Fusion scripts in `cad/scripts/parts/`, `cad/scripts/assemblies/`, and `cad/scripts/tools/`.
- Generate one real printable component at a time from locked YAML dimensions.
- Keep unresolved camera, objective, rail, and lead-screw dimensions in `cad/params/unresolved_dimensions.yaml` and `cad/reports/unresolved_dimensions.md`.
- Use Stage 1 only for the static microscope base, slide holder, Pi mount, camera reference mount, objective placeholder holder, and optical-axis datum.
