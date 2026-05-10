# Prototype Product List

This document details the exact components required for the prototype build, including researched pricing and links.
*Prices verified as of May 10, 2026. Do not invent unavailable prices.*

| Subsystem | Part (Qty) | Purpose | Selected Product | Price | Vendor Link | Image | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Compute | Raspberry Pi 4 (1) | Control & Capture | Raspberry Pi 4 (4GB) | $55.00 | [Adafruit/PiShop](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) | <img src="../../assets/images/hardware/prototype/raspberry_pi_4.jpg" width="80"/> | **High**: Need adequate cooling. |
| Compute | MicroSD Card (1) | OS Storage | Generic 32GB Class 10 | $8.00 | [Amazon](https://www.amazon.com/SanDisk-128GB-microSDXC-Memory-Adapter/dp/B073JYC4XM/) | <img src="../../assets/images/hardware/prototype/microsd_card.png" width="80"/> | **High**: High endurance preferred. |
| Compute | Power Supply (1) | Power RPi | Generic 5V 3A | $8.00 | [Amazon](https://www.amazon.com/Raspberry-Pi-Official-Supply-Type-C/dp/B07W8XHMJZ/) | <img src="../../assets/images/hardware/prototype/power_supply.png" width="80"/> | **High** |
| Camera | IMX296 Camera (1) | Image Sensor | InnovaMaker IMX296 | $60.00 | [InnovaMaker](https://www.inno-maker.com/product/imx296-camera-module/) | <img src="../../assets/images/hardware/prototype/imx296_module.jpg" width="80"/> | **Critical**: Global shutter required. |
| Camera | MIPI Cable (1) | Data connection | Included with camera | $0.00 | - | <img src="../../assets/images/hardware/prototype/mipi_cable.png" width="80"/> | **High**: Pi 5 uses different pitch. |
| Optics | 40X Objective (1) | Magnification | AmScope Standard 40X | $45.00 | [AmScope](https://amscope.com/products/40x-plan-achromatic-objective-lens-with-knurled-ring) | <img src="../../assets/images/hardware/prototype/amscope_40x_objective.png" width="80"/> | **Critical**: "Plan" is needed for flat fields. |
| Optics | Calibration Slide (1) | Scale reference | Printed Grid (Not rec) | $20.00 | [AmScope](https://amscope.com/products/microscope-stage-calibration-slide-for-usb-camera-0-01mm-stage-micrometer) | <img src="../../assets/images/hardware/prototype/calibration_slide.png" width="80"/> | **Medium**: Essential for measuring FOV. |
| Sample | Glass Slides (1) | Hold sample | Standard box of 72 | $10.00 | [Amazon](https://www.amazon.com/AmScope-BS-72P-100S-22-Pre-Cleaned-Microscope-Coverslips/dp/B0018N8N5K/) | <img src="../../assets/images/hardware/prototype/glass_slides.png" width="80"/> | **High** |
| Illumination/Control | LED Driver Board (1) | PWM LED Control | Adafruit TLC5947 | $17.50 | [Adafruit](https://www.adafruit.com/product/1429) | <img src="../../assets/images/hardware/prototype/tlc5947_led_driver.png" width="80"/> | **Critical**: Version 1 multispectral LED driver. 24 constant-current sink channels with 12-bit PWM. Suitable for low-power LEDs, not 1W/3W high-power LEDs. |
| Illumination/Timing | Microcontroller (1) | LED timing controller | Raspberry Pi Pico RP2040 | $4.00 | [Adafruit](https://www.adafruit.com/product/4864) | <img src="../../assets/images/hardware/prototype/raspberry_pi_pico.png" width="80"/> | **High**: High-level orchestration on RPi, lower-jitter LED timing on Pico. Communicates via USB serial. |
| Illumination/Carrier | LED Solder Board (1) | Mounting wavelength LEDs | Adafruit Perma-Proto Quarter | $5.95 | [Adafruit](https://www.adafruit.com/product/589) | <img src="../../assets/images/hardware/prototype/perma_proto_quarter.png" width="80"/> | **High**: Version 1 LED carrier board. Solder LEDs here, wire to TLC5947. Replace with custom circular PCB later. |
| Illumination/Optics | Diffuser Sheet (1) | Smooths LED illumination | LEE Filters 216 White Diffusion | $10.00 | [Amazon](https://www.amazon.com/Photography-Diffusion-Lighting-Filter-Continuous/dp/B07R451FZT) | <img src="../../assets/images/hardware/prototype/lee_216_diffuser_sheet.png" width="80"/> | **Critical**: Cut squares/circles and mount between LED carrier and sample to reduce hotspots. |
| Illumination/Wiring | Jumper Wire Kit (1) | Wiring Pico, TLC5947, Carrier | Premium Female/Female Jumper Wires | $3.95 | [Adafruit](https://www.adafruit.com/product/266) | <img src="../../assets/images/hardware/prototype/jumper_wires.png" width="80"/> | **Medium**: Use short wires to reduce clutter. |
| Illumination/Wiring | JST Connector Kit (1) | Removable carrier wiring | JST PH 2-pin Cable Set | $4.95 | [Adafruit](https://www.adafruit.com/product/3814) | <img src="../../assets/images/hardware/prototype/jst_connector_set.png" width="80"/> | **Medium**: Makes LED carrier board replaceable. |
| Motion | Linear Rails (2) | XY smooth travel | Generic MGN12 (KB3D) | $20.00 | [KB3D](https://kb-3d.com/store/linear-rails-carriages/1000-hiwin-mgn12h-linear-rail-carriage-1647468641973.html) | <img src="../../assets/images/hardware/prototype/mgn12_rail.png" width="80"/> | **High**: Avoid printed sliding parts. |
| Motion | Lead Screw (2) | XY actuation | Standard threaded rod | $15.00 | [Amazon](https://www.amazon.com/ReliaBot-400mm-Thread-Anti-Backlash-Printer/dp/B08CZGKS7D/) | <img src="../../assets/images/hardware/prototype/t8_lead_screw.png" width="80"/> | **High** |
| Motion | Stepper Motor (2) | Automated XY | 28BYJ-48 (Not rec) | $14.00 | [Pololu](https://www.pololu.com/product/2267) | <img src="../../assets/images/hardware/prototype/nema_17_stepper.png" width="80"/> | **Low**: Start with manual knobs. |
| Motion | Motor Driver (2) | Control Stepper | A4988 | $8.00 | [Pololu](https://www.pololu.com/product/3281) | <img src="../../assets/images/hardware/prototype/tmc2209_driver.png" width="80"/> | **Low**: TMC provides silent operation. |
| Fasteners | Screw Kit (1) | Assembly | Generic Kit | $15.00 | [Amazon](https://www.amazon.com/VIGRUE-Screws-Washers-Assortment-Wrenches/dp/B07FCQ4Q5Z/) | <img src="../../assets/images/hardware/prototype/fasteners.png" width="80"/> | **High** |
| Fasteners | Threaded Inserts (1) | Assembly | Generic M3 inserts | $12.00 | [Amazon](https://www.amazon.com/M3x5x4-Threaded-Insert-Embedment-Printing/dp/B0784VQ1T2/) | <img src="../../assets/images/hardware/prototype/fasteners.png" width="80"/> | **High**: Required for durable threads. |


## Version 1 Multispectral LED Diode Set

| Channel | Wavelength | Qty | Candidate Product | Verified Price | Vendor Link | Image | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Violet / Soret | 405 nm | 3-5 | Bivar UV5TZ-405-30 5mm | $1.00 ea | [Mouser](https://www.mouser.com/ProductDetail/Bivar/UV5TZ-405-30) | <img src="../../assets/images/hardware/prototype/led_405nm_bivar_uv5tz_405_30.png" width="80"/> | Hemoglobin/Soret-region contrast. Use eye safety precautions. |
| Blue | 470 nm | 3-5 | Kingbright WP7113QBC/D 5mm | $0.50 ea | [Mouser](https://www.mouser.com/ProductDetail/Kingbright/WP7113QBC-D) | <img src="../../assets/images/hardware/prototype/led_470nm_kingbright_wp7113qbc_d.png" width="80"/> | Blue channel for stain and WBC contrast. |
| Cyan | 505 nm | 3-5 | Kingbright WP7113CGCK 5mm | $0.50 ea | [Mouser](https://www.mouser.com/ProductDetail/Kingbright/WP7113CGCK) | <img src="../../assets/images/hardware/prototype/led_505nm_kingbright_wp7113cgck.png" width="80"/> | Optional extra channel between blue and green. |
| Green | 530 nm | 3-5 | Kingbright WP7113ZGC 5mm | $0.50 ea | [Mouser](https://www.mouser.com/ProductDetail/Kingbright/WP7113ZGC) | <img src="../../assets/images/hardware/prototype/led_530nm_kingbright_wp7113zgc.png" width="80"/> | Core morphology/RBC contrast channel. |
| Yellow | 590 nm | 3-5 | Kingbright WP7113SYC 5mm | $0.50 ea | [Mouser](https://www.mouser.com/ProductDetail/Kingbright/WP7113SYC) | <img src="../../assets/images/hardware/prototype/led_590nm_kingbright_wp7113syc.png" width="80"/> | Hemoglobin-related contrast channel. |
| Red | 625 nm | 3-5 | Kingbright WP7113ID 5mm | $0.35 ea | [Mouser](https://www.mouser.com/ProductDetail/Kingbright/WP7113ID) | <img src="../../assets/images/hardware/prototype/led_625nm_kingbright_wp7113id.png" width="80"/> | Lower absorption morphology and normalization channel. |
| Deep Red | 660 nm | 3-5 | Marktech MTE6600N2 660nm | $1.50 ea | [Mouser](https://www.mouser.com/ProductDetail/Marktech-Optoelectronics/MTE6600N2) | <img src="../../assets/images/hardware/prototype/led_660nm_marktech_mte6600n2.png" width="80"/> | Deep red comparison/normalization channel. |
| NIR (Optional) | 850 nm | 3-5 | Vishay TSHG6400 850nm | $1.00 ea | [Mouser](https://www.mouser.com/ProductDetail/Vishay-Semiconductors/TSHG6400) | <img src="../../assets/images/hardware/prototype/led_850nm_vishay_tshg6400.png" width="80"/> | Optional NIR channel. Verify camera sensitivity. |

> [!NOTE]
> **Recommended Version 1 Wiring:**
> Raspberry Pi -> USB serial -> Raspberry Pi Pico -> SPI-style pins -> Adafruit TLC5947 -> individual LED channels on solderable LED carrier board. Turn on one wavelength group at a time, capture an image, turn it off, then switch to the next wavelength.

> [!WARNING]
> The TLC5947 design is for low-power LEDs only. If illumination is too dim after the diffuser and microscope optics, upgrade to 1W narrowband LEDs mounted on aluminum star boards with dedicated constant-current drivers such as Mean Well LDD-350H or LDD-500H.

## Estimated Total Prototype Cost
- **Absolute cheapest build (Manual XY, 10X lens):** ~$150
- **Recommended prototype build (MGN12 rails, 40X Plan lens, manual):** ~$230
- **Automated motion build (add NEMA 17 & drivers):** ~$280
- **Multispectral low-power LED prototype add-on:** ~$50 to $100 depending on LED quantities, diffuser, connectors, and shipping.
- **High-power multispectral LED upgrade:** Future version, not included in current prototype BOM.
