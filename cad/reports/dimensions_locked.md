# Locked Dimensions

## Exact / Locked
- System envelope: `200 x 200 x 300 mm` maximum.
- Stage 1 baseplate: `180 x 160 x 6 mm` with `8 mm` corner radius.
- Slide: `75.0 x 25.0 mm`.
- Slide pocket: `76.0 x 25.6 mm`, derived from slide size plus clearances.
- Viewing window: `22.0 x 12.0 mm`.
- Finite objective stack datum: objective shoulder to sensor plane = `160.0 mm`.
- RMS objective standard: `0.8 in x 36 TPI`; printed thread fit is still coupon-gated.
- Raspberry Pi Global Shutter camera: `38 x 38 mm` board, `30 x 30 mm` hole span, `2.5 mm` holes.
- Raspberry Pi 4: `85 x 56 mm` board, `58 x 49 mm` hole span, `2.7 mm` holes.
- Raspberry Pi Pico board envelope only: `51.3 x 21.0 x 3.9 mm`.
- TLC5947 board envelope only: `51.1 x 25.39 x 4.0 mm`.
- Perma-Proto Quarter policy values: `50.8 x 43.0 x 1.6 mm`, two mounting holes `35.56 mm` apart.
- Pololu 2267 NEMA17 envelope: `42.3 x 42.3 x 38.0 mm`, `5.0 mm` shaft, `31 x 31 mm` mount span.

## Corrections
- Slide pocket X was corrected from `75.5 mm` to `76.0 mm` because end clearance is applied at both slide ends.
- Perma-Proto Quarter was corrected from the earlier `55 x 44 mm` placeholder to the Adafruit 1608 policy dimensions.
- Pico and TLC5947 mounting-hole spans are not locked here; they remain unresolved unless backed by a mechanical drawing or measurement.

## Verification Notes
- Verify Raspberry Pi 4 connector keepout zones against the specific Raspberry Pi 4 revision before final enclosure design.
- The BOM/product ID for the Perma-Proto Quarter must be checked before final tray geometry; Stage 1 avoids a four-hole rectangular assumption.