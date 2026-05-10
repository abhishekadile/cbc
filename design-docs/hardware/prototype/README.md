# Prototype Hardware Navigation

This folder contains the engineering design documentation for the first iteratable prototype of the CBC multispectral scanner.

## Purpose of the Prototype
The prototype's purpose is to validate the core optical path, imaging sensors, and software pipeline using rapidly accessible components (3D printed parts and off-the-shelf hardware) before committing to expensive production tooling. 

## What the First Prototype Must Prove
The first prototype is not for clinical testing. It must prove:
1. We can capture clear, focused microscope images using the IMX296 sensor.
2. We can move the sample to capture 5 to 10 overlapping images.
3. We can successfully stitch these images together using the CV pipeline.
4. We can run baseline computer vision segmentation on the stitched result.

**Clear Note:** Fully 3D-printed XY movement is acceptable *only* for an initial proof of concept. For smoother, repeatable movement, use metal rods or linear rails (like MGN12) even in the prototype phase.

## Files in This Folder

- `prototype-spec.md`: Detailed engineering requirements, tolerances, and design decisions.
- `prototype-product-list.md`: Bill of materials with researched prices and purchase links.
- `prototype-3d-printing-plan.md`: Strategy for 3D printing, materials, and STL/CAD references.
- `prototype-assembly-guide.md`: Step-by-step assembly, alignment, and testing procedures.
- `prototype-image-assets.md`: Image management guidelines and asset inventory.
- `prototype-test-plan.md`: (Coming soon) Test procedures for validating prototype success criteria.

## Recommended Build Order

1. **Source parts**: Procure items listed in the `prototype-product-list.md`.
2. **Print parts**: Slice and print components according to `prototype-3d-printing-plan.md`.
3. **Assemble optical path**: Mount the camera and objective lens, ensuring concentric alignment.
4. **Assemble slide holder / XY stage**: Build the motion system and attach the slide carriage.
5. **Connect Pi / Camera / LED**: Wire the electronics, install heat sinks, and boot the Raspberry Pi.
6. **Capture first image**: Use a calibration slide to focus and capture a single test image.
7. **Capture 5 to 10 overlapping images**: Manually (or via stepper motors) translate the stage, ensuring 40-60% overlap.
8. **Stitch**: Run the software pipeline to stitch the grid of images.
9. **Run CV segmentation**: Verify that the pipeline can extract features from the stitched image.
