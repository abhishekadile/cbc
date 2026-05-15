# BOM to CAD Mapping

| Bought part | CAD relationship |
| --- | --- |
| Raspberry Pi 4 | Mounted by `cbc_pi4_mount`; simplified envelope appears in both assemblies. |
| InnovaMaker IMX296 camera | Mounted by `cbc_camera_mount_imx296`; geometry remains slotted until board and sensor offset are measured. |
| Raspberry Pi Global Shutter camera | Alternate locked mount `cbc_camera_mount_rpi_gs`. |
| AmScope 40X RMS objective | Held by `cbc_objective_holder_rms`; stack completed with `cbc_optical_tube_section`. |
| Glass microscope slide | Held by `cbc_slide_holder`, `cbc_slide_clamp_left`, and `cbc_slide_clamp_right`. |
| MGN12 rails/carriages | Supported by `cbc_x_rail_support_*`, `cbc_y_rail_support_*`, `cbc_x_carriage`, and `cbc_y_carriage`; exact hole geometry unresolved, so slots are used. |
| T8 lead screws and nuts | Carried by `cbc_lead_nut_carrier_x`, `cbc_lead_nut_carrier_y`, and `cbc_manual_knob_t8`; nut geometry unresolved. |
| NEMA17 steppers | Optional mounts `cbc_nema17_mount_x` and `cbc_nema17_mount_y`; used only in stepper assembly. |
| Raspberry Pi Pico | Mounted by `cbc_pico_mount`. |
| Adafruit TLC5947 | Mounted by `cbc_tlc5947_mount`. |
| Adafruit Perma-Proto Quarter | Held in `cbc_permaproto_tray` as LED carrier/electronics prototyping board. |
| Diffuser sheet | Captured by `cbc_diffuser_frame`. |
| 5 mm LEDs | Arranged by `cbc_led_ring_holder`, parameterized by LED count. |
| M3 screws and heat-set inserts | Reflected in clearance and insert pilot parameters; validated by `cbc_m3_insert_coupon`. |
