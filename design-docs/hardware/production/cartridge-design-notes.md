# Cartridge Design Notes

*Note: These notes focus purely on the engineering constraints of the imaging target. No biological sample handling procedures are provided.*

The transition from a prototype using standard glass slides to a production system requires a specialized cartridge. This is the single most critical component for ensuring reliable quantitative data.

## Key Engineering Requirements

- **Known Volume**: The imaging chamber must hold a precisely defined volume of fluid.
- **Known Depth**: The height of the imaging chamber (z-axis) must be tightly controlled across its entire area. If the depth varies, the calculated volume per field-of-view varies, ruining concentration accuracy.
- **Fixed Imaging Window**: The cartridge must define a specific area intended for the scanning process, ensuring the AI only processes the valid region.
- **Alignment Keying**: The cartridge must feature physical keying or registration marks (asymmetric design) to ensure it seats identically in the scanner every time, preventing user error.
- **Optical Clarity**: The materials used for the top and bottom of the imaging chamber must be optically clear, with minimal autofluorescence or distortion in the target wavelengths (400nm - 700nm).
- **Manufacturing Tolerance**: The dimensional tolerances of the imaging chamber directly impact the count-to-concentration calculation. These tolerances must be rigorously defined and validated during molding.
- **Anti-Bubble Geometry Consideration**: The fluidic path must be designed to minimize the introduction or trapping of air bubbles in the imaging region. Bubbles cause massive optical distortion, ruining both CV and AI segmentation.

## Enabling Concentration Calculations

The primary purpose of the known-volume cartridge is to enable the transition from a raw "object count" to an absolute "concentration."

By knowing:
1. The **Area Imaged** (Field of View X * Field of View Y * Number of stitched frames).
2. The **Depth** of the cartridge chamber.
3. Any **Dilution Factors** introduced prior to imaging.

The system can convert the count derived from the AI/CV pipeline into a standard concentration metric (e.g., cells per microliter).

*Formula:*
`Volume Imaged = Area Imaged * Chamber Depth`
`Concentration = (Total Count / Volume Imaged) * Dilution Factor`

## Calibration Relationship
The system software must maintain a calibration profile that maps the camera's pixel dimensions to physical microns to accurately calculate the *Area Imaged*.
