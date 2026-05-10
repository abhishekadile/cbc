# Prototype Hardware Specification

## Purpose
The purpose of the prototype hardware is to provide an initial, rapidly iterable platform for capturing multispectral microscope images, testing stitching algorithms, and developing the initial CV/AI pipeline.

## Design Goals
- Accessible and easy to assemble.
- Sufficient optical clarity to capture cellular structures.
- Ability to move the sample for overlapping captures.
- First milestone: capture 5 to 10 images and stitch them successfully.

## Architecture

- **Mechanical Architecture**: 3D printed main frame with modular mounts. While a fully 3D printed XY stage is acceptable for early proof of concept, metal rods/rails and screws are preferred even in the prototype for better stability.
- **Optical Architecture**: Standard microscope objective/lens system. Recommend 40% to 60% image overlap to make stitching easier.
- **Illumination Architecture**: LED array with a diffuser to ensure even lighting across the field of view.
- **Motion Architecture**: Metal rods or small linear rails for XY movement. Threaded rod or lead screw for motion. Optional manual knobs initially, to be replaced by stepper motors later. Optional limit switches later.
- **Electronics Mounting**: Dedicated mounts for the Raspberry Pi and future motor control boards.

## Prototype Design & 3D Printing Guidelines

- **What can be 3D printed**: Main frame, camera mount, objective/lens holder, slide holder, LED/diffuser holder, Raspberry Pi mount, motor brackets.
- **What should not be 3D printed**: Precision motion components (use metal rails/rods), primary optical elements.
- **Acceptable Prototype Tolerances**: Sufficient to hold components securely without excessive wobble that would blur images during capture.

## Expected Limitations
- Not clinically accurate.
- Susceptible to vibration and temperature variations.
- Manual or semi-manual focus initially.
