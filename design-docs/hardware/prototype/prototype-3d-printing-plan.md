# 3D Printing Plan

## Guidelines

- **Printable Parts List**: See table below.
- **Suggested Material**: PLA for early prototype (easy to print). PETG or ABS for better heat resistance and durability in later iterations.
- **Recommended Infill Ranges**: 20% - 40% for most parts. 50%+ for structural mounts (e.g., camera, objective).
- **Wall Count**: Minimum 3 perimeters (walls) for strength. 4-5 for parts receiving heat-set inserts.
- **Orientation Notes**: Orient parts to maximize strength along load-bearing axes. Avoid supports in critical mounting holes where possible.
- **Heat-Set Insert Recommendations**: Use soldering iron with a specific insert tip. Size holes appropriately (e.g., 4.0mm for M3 inserts).
- **Tolerances**: Design with 0.2mm clearance for sliding parts, 0.1mm for press-fit.
- **Parts that need post-processing**: Holes may need to be reamed with a drill bit. Remove stringing to prevent debris in the optical path.
- **What NOT to print**: Precision rails, optical lenses, lead screws.
- **Versioning Convention**: Use suffix versioning (e.g., `SlideHolder_v1.2.stl`).
- **Where STL files should be stored**: `design-docs/assets/stl/`.

## Printable Parts List

| Part Name | Function | Material | Infill | Print Orientation | Hardware Needed | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Main Base | Foundation | PETG | 30% | Flat on bottom | M3 screws, inserts | Largest part |
| Camera Mount | Holds IMX296 | PETG | 40% | Flat on back | M3 inserts | Needs to be rigid |
| Objective Holder | Secures lens | PETG | 50% | Vertical | M3 screws | Threaded if possible |
| Slide Carrier | Holds glass slide | PLA/PETG | 20% | Flat | None initially | Must slide smoothly |
| LED Mount | Holds illumination | PETG | 30% | Flat | M3 screws | Watch for heat |
| Pi Bracket | Mounts RPi | PLA/PETG | 20% | Flat | M2.5 standoffs | Ensure airflow |
| Motor Brackets | Mounts Steppers | PETG | 40% | Flat | M3 screws | |
