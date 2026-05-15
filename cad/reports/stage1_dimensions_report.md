# Stage 1 Dimensions Report

Stage 1 is a static optical/base assembly. It is not the final XY-motion microscope and does not freeze unresolved vendor geometry.

## Locked Geometry
- Baseplate: 180.0 x 160.0 x 6.0 mm.
- Slide pocket: 76.0 x 25.6 mm for a 75 x 25 mm slide.
- Viewing window: 22.0 x 12.0 mm.
- Pi 4 board nest: 85.5 x 56.5 mm.
- Pi 4 mount span: 58.0 x 49.0 mm.
- RPi GS camera board nest: 38.5 x 38.5 mm.
- RPi GS camera hole span: 30.0 x 30.0 mm.
- Optical axis location: X=0.0 mm, Y=12.0 mm.
- Objective shoulder to sensor plane datum: 160.0 mm.

## Corrections Applied
- Slide pocket corrected and locked at 76.0 x 25.6 mm from slide size plus end/side clearances.
- Perma-Proto Quarter dimensions corrected to the Adafruit 1608 policy values: 50.8 x 43.0 x 1.6 mm with a two-hole 35.56 mm span.

## Real Export Policy
- `build_stage1` writes reports/spec metadata and may build live Fusion geometry when run inside Fusion.
- Manufacturing STL/STEP/F3D files are written only by `export_stage1` through Fusion ExportManager.
- Offline placeholder manufacturing files are intentionally not produced.

## Assembly Warnings
- Unresolved Stage 1 optical dimensions: unresolved_dimensions.objective_amscope_40x.shoulder_d_mm, unresolved_dimensions.objective_amscope_40x.body_outer_d_mm, unresolved_dimensions.objective_amscope_40x.body_length_mm, unresolved_dimensions.stage1_optical_stack.imx296_sensor_plane_offset_from_mount_face_mm, unresolved_dimensions.stage1_optical_stack.rpi_gs_sensor_plane_offset_from_mount_face_mm, unresolved_dimensions.stage1_optical_stack.amscope_40x_objective_shoulder_geometry_mm, unresolved_dimensions.stage1_optical_stack.objective_parfocal_distance_mm
