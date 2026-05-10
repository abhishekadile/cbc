# Cartridge Design Notes

*Note: These notes focus purely on the engineering constraints of the imaging target. No biological sample handling procedures are provided.*

The production system requires transitioning from standard glass slides to a specialized cartridge to ensure reliable quantitative data.

## Key Engineering Requirements

- **Known Volume**: The imaging chamber must hold a precisely defined volume of fluid.
- **Known Depth**: The height of the imaging chamber (z-axis) must be tightly controlled so the entire depth can be imaged (or calculated).
- **Optical Clarity**: The materials used for the top and bottom of the imaging chamber must be optically clear, with minimal autofluorescence or distortion in the target wavelengths.
- **Consistent Imaging Region**: The cartridge must define a specific area intended for the scanning process.
- **Cartridge Alignment**: The cartridge must feature physical keying or registration marks to ensure it seats identically in the scanner every time.
- **Anti-Bubble Design Consideration**: The fluidic path must be designed to minimize the introduction or trapping of air bubbles in the imaging region, as these interfere with CV/AI segmentation.
- **Manufacturing Tolerances**: The dimensional tolerances of the imaging chamber directly impact the count-to-concentration calculation. These tolerances must be defined and validated.

## Enabling Concentration Calculations

The primary purpose of the known-volume cartridge is to enable the transition from a raw "object count" to a "concentration." 

By knowing:
1. The area imaged (Field of View X * Field of View Y * Number of frames)
2. The depth of the cartridge chamber
3. Any dilution factors introduced prior to imaging

The system can convert the count derived from the AI/CV pipeline into a standard concentration metric.
