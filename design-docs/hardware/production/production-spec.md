# Production Hardware Specification

The production hardware evolves the prototype into a reliable, repeatable, and manufacturable device suitable for field use and data collection at scale.

## Evolution from Prototype

The production system should *not* rely on fully 3D printed precision motion components. 3D printing can be used for fixtures, brackets, early prototypes, and low-load non-critical parts.

- **Rigid frame**: Transition to sheet metal, machined aluminum, or injection-molded chassis for stability.
- **Repeatable optical path**: Machined or tightly toleranced optical mounts to ensure consistent focus and alignment.
- **Controlled cartridge**: Move away from standard glass slides to a custom, known-volume cartridge system.
- **Known imaged volume**: Ensure the system images a specific volume of fluid to enable accurate concentration calculations.
- **Calibrated XY motion**: Utilize precision linear rails and closed-loop steppers or high-quality open-loop steppers to prevent stage backlash and missed steps.
- **Stable Z focus**: Implement a reliable automated focus mechanism with fine resolution.
- **Controlled multispectral illumination**: Use a calibrated LED array with feedback to ensure consistent intensity and wavelength output over time.
- **Enclosure**: Implement a light-tight, dust-resistant enclosure.
- **Manufacturability**: Design for assembly (DFA) using standard fasteners and minimal manual adjustment.
- **Serviceability**: Allow easy access to the camera, optics, and electronics for maintenance.
- **Calibration workflow**: Integrate a calibration slide or target for automated system checks.
