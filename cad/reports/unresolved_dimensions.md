# Unresolved Dimensions

- `unresolved_dimensions.camera_innomaker_imx296.board_x_mm`
- `unresolved_dimensions.camera_innomaker_imx296.board_y_mm`
- `unresolved_dimensions.camera_innomaker_imx296.board_z_mm`
- `unresolved_dimensions.camera_innomaker_imx296.mount_hole_dia_mm`
- `unresolved_dimensions.camera_innomaker_imx296.mount_hole_span_x_mm`
- `unresolved_dimensions.camera_innomaker_imx296.mount_hole_span_y_mm`
- `unresolved_dimensions.camera_innomaker_imx296.sensor_plane_offset_from_mount_face_mm`
- `unresolved_dimensions.objective_amscope_40x.shoulder_d_mm`
- `unresolved_dimensions.objective_amscope_40x.body_outer_d_mm`
- `unresolved_dimensions.objective_amscope_40x.body_length_mm`
- `unresolved_dimensions.stage1_optical_stack.imx296_sensor_plane_offset_from_mount_face_mm`
- `unresolved_dimensions.stage1_optical_stack.rpi_gs_sensor_plane_offset_from_mount_face_mm`
- `unresolved_dimensions.stage1_optical_stack.amscope_40x_objective_shoulder_geometry_mm`
- `unresolved_dimensions.stage1_optical_stack.objective_parfocal_distance_mm`
- `unresolved_dimensions.pi4_connector_keepouts.usb_ethernet_zone_mm`
- `unresolved_dimensions.pi4_connector_keepouts.usb_c_power_zone_mm`
- `unresolved_dimensions.pi4_connector_keepouts.hdmi_zone_mm`
- `unresolved_dimensions.pi4_connector_keepouts.gpio_header_zone_mm`
- `unresolved_dimensions.pico_mount.mount_hole_span_x_mm`
- `unresolved_dimensions.pico_mount.mount_hole_span_y_mm`
- `unresolved_dimensions.pico_mount.mount_hole_dia_mm`
- `unresolved_dimensions.tlc5947_mount.mount_hole_span_x_mm`
- `unresolved_dimensions.tlc5947_mount.mount_hole_span_y_mm`
- `unresolved_dimensions.tlc5947_mount.mount_hole_dia_mm`
- `unresolved_dimensions.permaproto_quarter.second_axis_mount_span_mm`
- `unresolved_dimensions.permaproto_quarter.orientation_on_tray`
- `unresolved_dimensions.nema17_pololu_2267.shaft_length_mm`
- `unresolved_dimensions.nema17_pololu_2267.pilot_boss_d_mm`
- `unresolved_dimensions.nema17_pololu_2267.pilot_boss_height_mm`
- `unresolved_dimensions.rail_system.selected_family`
- `unresolved_dimensions.rail_system.rail_hole_pitch_mm`
- `unresolved_dimensions.rail_system.rail_hole_dia_mm`
- `unresolved_dimensions.rail_system.carriage_hole_span_x_mm`
- `unresolved_dimensions.rail_system.carriage_hole_span_y_mm`
- `unresolved_dimensions.rail_system.carriage_hole_thread_mm`
- `unresolved_dimensions.lead_screw.screw_lead_mm_per_rev`
- `unresolved_dimensions.lead_screw.nut_body_x_mm`
- `unresolved_dimensions.lead_screw.nut_body_y_mm`
- `unresolved_dimensions.lead_screw.nut_body_z_mm`
- `unresolved_dimensions.lead_screw.nut_mount_hole_span_x_mm`
- `unresolved_dimensions.lead_screw.nut_mount_hole_span_y_mm`
- `unresolved_dimensions.lead_screw.nut_mount_hole_dia_mm`

These remain unresolved by design. Do not replace slots/placeholders with fixed geometry until measured or backed by reliable vendor drawings.

## Measure Before Stage 2

- InnovaMaker IMX296 board outline, mounting pattern, thickness, and sensor-plane offset.
- AmScope 40X objective shoulder geometry, body outer diameter, body length, and any printed thread compensation.
- Raspberry Pi 4 connector keepout zones for the exact board revision used.
- Raspberry Pi Pico and TLC5947 mounting-hole positions if dedicated board mounts are added.
- Perma-Proto Quarter product ID/orientation if a retained tray replaces simple slots or walls.
- Rail, carriage, T8 lead nut, and motor pilot dimensions before Stage 2 XY-motion CAD.
