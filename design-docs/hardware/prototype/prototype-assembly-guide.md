# Prototype Assembly Guide

This guide details the step-by-step process for assembling the CBC multispectral prototype.

## Tools Required
- Hex/Allen key set (Metric, 1.5mm to 3mm).
- Soldering iron (with heat-set insert tip).
- Small Phillips screwdriver.
- Digital calipers.
- Flush cutters (for cleaning prints).

## Fasteners Required
- M3 socket head cap screws (various lengths: 6mm, 8mm, 12mm, 20mm).
- M3 heat-set inserts.
- M2.5 screws (for Raspberry Pi mounting).

## Safety Notes
- Unplug power before wiring the LED driver or Raspberry Pi.
- Be careful with the soldering iron when pressing inserts.
- Do not touch the glass surface of the objective lens or the bare IMX296 sensor.

## Step-by-Step Assembly

### 1. Preparation
- **Print and inspect parts**: Ensure all 3D printed parts are clean and free of stringing. Ream out clearance holes with a 3mm drill bit if necessary.
- **Install heat-set inserts**: Use the soldering iron to press M3 inserts into the designated holes on the baseplate, optical tower, and carriage. Let them cool.

### 2. Base and Optics
- **Assemble base**: Attach rubber feet to the baseplate.
- **Mount vertical optical tower**: Bolt the Z-axis tower securely to the baseplate. Ensure it is perfectly perpendicular.
- **Mount camera**: Attach the IMX296 camera board to the printed camera mount using M2.5 screws. Attach this mount to the top of the optical tower.
- **Mount lens/objective**: Carefully thread the AmScope 40X objective into the printed RMS holder.
- **Align optical axis**: Ensure the camera sensor is centered directly above the objective lens. If using a 160mm objective, use calipers to verify the distance from the objective shoulder to the camera sensor is exactly 160mm.

### 3. Stage and Illumination
- **Mount LED/diffuser**: Assemble the LED ring and the diffuser plate. Mount this directly below the objective lens on the baseplate.
- **Assemble XY stage**:
    - Attach the MGN12 linear rails to the baseplate (X-axis).
    - Attach the Y-axis rails to the intermediate carriage.
    - Attach the slide holder top plate.
    - Thread the T8 lead screws through the anti-backlash nuts and attach the manual knobs.
- **Install slide holder**: Verify the slide clamps securely hold a standard 25x75mm glass slide.
- **Check movement**: Manually turn the X and Y knobs. The stage should move smoothly without binding.

### 4. Electronics
- **Mount Raspberry Pi**: Attach the Pi to its case/mount on the side of the chassis.
- **Wire LED**: Connect the LED ring to its power supply or driver board.
- **Connect camera ribbon**: Carefully insert the MIPI ribbon cable into the Pi's camera port and the IMX296 board. Ensure the silver contacts face the correct direction.

### 5. Testing and Validation
- **Boot Pi**: Connect power to the Raspberry Pi. Wait for it to boot.
- **Run camera test**: Open an SSH terminal and run `libcamera-hello` or `rpicam-hello` to verify the sensor is detected.
- **LED test**: Turn on the LED array and verify uniform illumination through the diffuser.
- **Capture first focused image**:
    - Place the calibration slide on the stage.
    - Run a continuous preview (`libcamera-vid -t 0`).
    - Adjust the Z-focus knob until the grid lines are sharp.
    - Save the image.
- **Capture 5 to 10 overlapping images**:
    - Move the X/Y knobs to pan across the slide.
    - Capture an image, move the stage so the next view overlaps by ~50%, capture again. Repeat for a 3x3 grid.
- **Stitching test**: Run the offline Python stitching script on the captured grid. Verify successful alignment.

## Troubleshooting Table

| Symptom | Likely Cause | Fix |
| :--- | :--- | :--- |
| Camera not detected | Ribbon cable upside down or loose | Re-seat cable at both ends; check Pi OS configuration |
| Image is completely black | LED off, or objective extremely out of focus | Turn on LED; move Z-axis significantly until light is visible |
| Image is blurry / won't focus | Distance from lens to sensor is incorrect | Adjust Z-axis position; verify 160mm tube length |
| Image is unevenly lit | Diffuser missing or misaligned | Add diffuser; center LED under objective |
| XY stage binds or stutters | Linear rails misaligned | Loosen rail screws, move carriage back and forth to self-align, retighten |
| Stitching fails | Insufficient overlap or out of focus | Ensure >40% overlap; ensure slide is perfectly flat relative to XY travel |

## Pass/Fail Checklist
| Assembly Step | Expected Result | Pass/Fail |
| :--- | :--- | :--- |
| Mechanical | Frame is rigid, no loose parts | [ ] |
| Motion | Stage moves smoothly across full travel | [ ] |
| Electronic | Pi boots, Camera streams preview | [ ] |
| Optical | Can achieve sharp focus on a slide | [ ] |
| Pipeline | Can stitch 5 manual images | [ ] |
