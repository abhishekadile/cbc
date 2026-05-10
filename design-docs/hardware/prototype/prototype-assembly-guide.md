# Prototype Assembly Guide

This guide covers the initial assembly of the 3D-printed multispectral imaging prototype.

## Step-by-Step Assembly

1. **Print parts**: Print all necessary components listed in the 3D printing plan. Clean up any stringing or supports.
2. **Prepare fasteners/inserts**: Install all heat-set inserts into the printed parts using a soldering iron.
3. **Assemble base/frame**: Construct the main frame, securing components with M3 screws.
4. **Mount optics/camera**: Attach the objective lens holder to the frame. Mount the IMX296 camera to the camera mount, and secure the assembly to the frame, ensuring alignment with the objective.
5. **Mount slide holder**: Attach the slide holder mechanism to the XY stage.
6. **Mount LED/diffuser**: Assemble the LED ring and diffuser. Mount this assembly below the slide holder (for transmitted light).
7. **Assemble XY stage**: Install the metal rods or linear rails. Attach the sliding blocks and secure them to the frame and slide holder.
8. **Add manual movement or motors**: Install the lead screws/threaded rods. Add manual knobs or attach stepper motors depending on the current iteration.
9. **Cable Raspberry Pi and camera**: Secure the Raspberry Pi to its mount. Connect the MIPI ribbon cable from the IMX296 camera to the Pi. Wire the LED ring to power/control.
10. **Test camera**: Boot the Raspberry Pi and run a basic libcamera command to verify the sensor is detected and streaming.
11. **Capture first image**: Place a test slide and capture a single frame. Adjust Z-focus manually until sharp.
12. **Capture 5 to 10 overlapping images**: Move the XY stage manually or via motors to capture a grid of slightly overlapping images (40-60% overlap).
13. **Stitch images**: Transfer images to a PC (or run locally if performance permits) and run the initial image stitching script.
14. **Run basic CV segmentation**: Run the classical computer vision pipeline on the stitched image to verify object detection.

## Assembly Checklist
- [ ] All 3D parts printed and cleaned
- [ ] Heat-set inserts installed
- [ ] Frame assembled and rigid
- [ ] Camera and optics aligned
- [ ] LED/diffuser mounted and powered
- [ ] XY stage moving smoothly
- [ ] Raspberry Pi booted and camera detected
- [ ] Focus mechanism tested
- [ ] First overlapping image set captured
