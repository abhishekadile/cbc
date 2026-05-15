# Locked and Unresolved Dimensions

## Exact / Locked

- System envelope: `200 x 200 x 300 mm` maximum.
- Standard slide: `75 x 25 mm`.
- Finite objective stack target: objective shoulder to sensor plane = `160.0 mm`.
- RMS objective standard: `0.8 in x 36 TPI`.
- Raspberry Pi Global Shutter camera reference geometry: `38 x 38 mm`, `30 x 30 mm` mounting span, `2.5 mm` holes.
- Raspberry Pi 4 board: `85 x 56 mm`, `58 x 49 mm` mounting span, `2.7 mm` holes.
- Pico board envelope: `51.3 x 21.0 x 3.9 mm`.
- TLC5947 board envelope: `51.1 x 25.39 x 4.0 mm`.
- Perma-Proto quarter board envelope: `55 x 44 mm`, `35.56 mm` locked one-axis hole span.
- Pololu 2267 NEMA17 envelope: `42.3 x 42.3 x 38.0 mm`, `5.0 mm` shaft, `31 x 31 mm` mount span.

## Unresolved / Must Be Measured

- InnovaMaker IMX296 board outline, thickness, mount hole diameter/span, and sensor-plane offset from mount face.
- AmScope 40X shoulder diameter, body outer diameter, body length, and final printed RMS thread compensation.
- MGN12 rail family details: rail hole pitch, rail hole diameter, carriage hole span, carriage thread.
- T8 lead screw nut geometry: body size and mount hole pattern.
- Stepper driver board holder footprint: A4988/TMC2209 exact holder intentionally not modeled; use electronics tray/perfboard placement until locked.

## TODOs Before Production Prints

- Measure the actual InnovaMaker IMX296 board with calipers before freezing that bracket.
- Print `cbc_rms_thread_coupon_r001` before printing the objective holder.
- Print `cbc_m3_insert_coupon_r001` in the target filament before installing inserts in structural parts.
- Lock selected rail and carriage datasheets before replacing rail/carriage slots with fixed holes.
