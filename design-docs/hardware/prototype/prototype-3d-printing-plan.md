# 3D Printing Plan

## 1. Purpose
This document outlines the engineering plan for fabricating the prototype chassis using Fused Deposition Modeling (FDM) 3D printing. The goal is to produce rigid, accurate parts that maintain optical alignment while allowing rapid iteration.

## 2. Printing Strategy
- **Rigidity over speed**: Print with higher wall counts rather than high infill.
- **Optical considerations**: Use matte black materials for any parts near the optical path to reduce stray light reflections.
- **Modularity**: Design parts to bolt together rather than printing massive single unibodies. This reduces print failure risk and allows replacing single brackets.

## 3. Printer/Material Assumptions
- Standard FDM printer (e.g., Prusa i3, Bambu Lab, Ender 3).
- 0.4mm nozzle.
- Textured or smooth PEI build plate.

## 4. Material Selection
- **PLA**: Acceptable for the first, quick prototype. It is stiff and easy to print.
- **PETG**: Recommended for parts near the LEDs or motors, as PLA will deform under heat.
- **ABS/ASA**: Best for long-term prototypes due to high heat deflection, but harder to print without an enclosure.
- **Matte Black PLA/PETG**: Strongly preferred for the optical tower and lens mounts. Flocking material or matte black paint can be applied post-print if standard shiny filament is used.

## 5. Print Settings
- **Layer Height**: 0.2mm (standard). Use 0.12mm for fine threaded parts if not using metal inserts.
- **Wall Count (Perimeters)**: Minimum 4 walls. This is where the part gets its strength.
- **Infill**: 20% - 40% Gyroid or Cubic.
- **Supports**: Avoid where possible. Orient parts so critical mounting holes print cleanly.

## 6. Printable Parts Breakdown

| Part | Function | Print or Buy? | Existing STL/CAD Link | License | Material | Infill | Walls | Orientation | Hardware Needed | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseplate | Main foundation | Print | Custom CAD required | Open | PETG | 25% | 4 | Flat | M3 inserts | Heavy and rigid |
| Optical Tower | Z-axis support | Print | [OpenFlexure v7 Base](https://openflexure.org/projects/microscope/build) | CERN OHL | Black PETG | 40% | 5 | Vertical | M3 screws | Use as reference design |
| Camera Mount | Holds IMX296 | Print | [Raspberry Pi HQ Mount](TODO: verify link) | CC BY | PETG | 30% | 4 | Flat | M2.5 screws | Modify for IMX296 hole spacing |
| Objective Holder| Holds RMS lens | Print | [RMS to C-mount adapter](TODO: verify link) | CC BY | Black PETG | 50% | 5 | Flat | None | Thread tolerances are critical. May need 0.12mm layers |
| XY Carriage | Moves sample | Print | Custom CAD required | Open | PLA/PETG | 30% | 4 | Flat | MGN12 blocks | Must mount to linear rails |
| Rail Holders | Secures MGN12 | Print | Custom CAD required | Open | PETG | 40% | 4 | Flat | M3 screws | |
| Lead Nut Mount | Drives XY | Print | Custom CAD required | Open | PETG | 30% | 4 | Flat | Anti-backlash nut | |
| Pi Case/Mount | Holds RPi | Print | [RPi 4 Snap-fit Case](TODO: verify link) | CC BY-NC | PLA | 20% | 3 | Flat | None | |

## 7. Parts Not Suitable for Printing
- Precision linear rails (MGN12).
- Lead screws and nuts.
- Bearings.
- Optical lenses.
**Rule:** Avoid plastic-on-plastic sliding for anything requiring repeatable movement (like the XY stage). It causes stiction and backlash.

## 8. Downloadable STL/CAD Options
We leverage open-source designs where possible:
- **OpenFlexure Microscope**: Excellent reference for 3D printed flexure mechanisms if we decide to avoid linear rails for the Z-axis.
- **UC2 Modular Microscopy**: Great reference for magnetic, modular optical cubes.

## 9. Tolerance and Fit Guidance
- Add **0.2 mm to 0.4 mm** clearance to CAD dimensions for printed fits (e.g., a peg going into a hole).
- Holes intended for M3 screws to pass through freely should be modeled at **3.2mm - 3.4mm**.
- Holes for heat-set inserts should be sized according to the insert manufacturer's spec (typically ~4.0mm diameter for an M3 insert).
- Use chamfers (not fillets) for overhangs near the build plate to prevent elephant's foot from ruining tolerances.

## 10. Heat-Set Insert Guidance
Use M3 heat-set inserts (like those from CNC Kitchen) for parts that will be repeatedly assembled/disassembled. Press them in using a soldering iron set to the melting temperature of the filament (e.g., 200°C for PLA).

## 11. Part Versioning
Append a version number to all exported STLs: `XY_Carriage_v1.2.stl`. Store them in `design-docs/assets/stl/`.

## 12. Quality Checklist
- [ ] No stringing or blobs inside the optical path.
- [ ] Dimensions measure within 0.1mm of CAD using calipers.
- [ ] M3 screws pass through clearance holes freely.
- [ ] Heat set inserts sit flush with the surface.
