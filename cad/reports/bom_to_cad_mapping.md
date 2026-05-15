# BOM to CAD Mapping

| Bought part | Stage | CAD relationship |
| --- | --- | --- |
| Glass microscope slide | Stage 1 | Held by `cbc_slide_holder_r001`; uses a removable pocket, window, M3 holes, and retainer slots. |
| Raspberry Pi 4 | Stage 1 | Mounted by `cbc_pi4_mount_r001`; board envelope and hole span are locked, connector keepouts remain to verify. |
| Raspberry Pi Global Shutter Camera | Stage 1 | Mounted by `cbc_camera_mount_rpi_gs_r001`; board and hole pattern are locked, sensor-plane offset remains unresolved. |
| AmScope 40X RMS objective | Stage 1 placeholder | Represented by `cbc_objective_holder_placeholder_r001`; this is not a final RMS threaded holder. |
| Optical axis / sensor datum | Stage 1 | Represented by `cbc_optical_axis_datum_r001` for alignment only, not a printed manufacturing part. |
| InnovaMaker IMX296 camera | Stage 2 | Future alternate camera mount; actual board and sensor offset must be measured. |
| MGN12 rails/carriages | Stage 2 | Future XY-motion rail supports and carriages; exact holes remain unresolved. |
| T8 lead screws and nuts | Stage 2 | Future lead-nut carriers and knobs; nut body and hole pattern remain unresolved. |
| NEMA17 steppers | Stage 2 optional | Future motor mounts; shaft length and pilot boss geometry remain unresolved. |
| Raspberry Pi Pico | Stage 2 electronics | Board envelope locked; mount holes unresolved. |
| Adafruit TLC5947 | Stage 2 electronics | Board envelope locked; mount holes unresolved. |
| Adafruit Perma-Proto Quarter | Stage 2 electronics | Two-hole board policy dimensions locked; tray orientation/product ID must be verified. |
| M3 screws and heat-set inserts | Stage 1/2 | Clearance and pilot parameters are in `clearances.yaml`; insert pilot is insert-dependent and should be coupon-tested. |