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
| Illumination | LED Ring (1) | Light Source | Generic White LED Ring | $15.00 | [Adafruit](https://www.adafruit.com/product/1463) | <img src="../../assets/images/hardware/prototype/led_ring.png" width="80"/> | **High**: Need diffuser. |
| Motion | Linear Rails (2) | XY smooth travel | Generic MGN12 (KB3D) | $20.00 | [KB3D](https://kb-3d.com/store/linear-rails-carriages/1000-hiwin-mgn12h-linear-rail-carriage-1647468641973.html) | <img src="../../assets/images/hardware/prototype/mgn12_rail.png" width="80"/> | **High**: Avoid printed sliding parts. |
| Motion | Lead Screw (2) | XY actuation | Standard threaded rod | $15.00 | [Amazon](https://www.amazon.com/ReliaBot-400mm-Thread-Anti-Backlash-Printer/dp/B08CZGKS7D/) | <img src="../../assets/images/hardware/prototype/t8_lead_screw.png" width="80"/> | **High** |
| Motion | Stepper Motor (2) | Automated XY | 28BYJ-48 (Not rec) | $14.00 | [Pololu](https://www.pololu.com/product/2267) | <img src="../../assets/images/hardware/prototype/nema_17_stepper.png" width="80"/> | **Low**: Start with manual knobs. |
| Motion | Motor Driver (2) | Control Stepper | A4988 | $8.00 | [Pololu](https://www.pololu.com/product/3281) | <img src="../../assets/images/hardware/prototype/tmc2209_driver.png" width="80"/> | **Low**: TMC provides silent operation. |
| Fasteners | Screw Kit (1) | Assembly | Generic Kit | $15.00 | [Amazon](https://www.amazon.com/VIGRUE-Screws-Washers-Assortment-Wrenches/dp/B07FCQ4Q5Z/) | <img src="../../assets/images/hardware/prototype/fasteners.png" width="80"/> | **High** |
| Fasteners | Threaded Inserts (1) | Assembly | Generic M3 inserts | $12.00 | [Amazon](https://www.amazon.com/M3x5x4-Threaded-Insert-Embedment-Printing/dp/B0784VQ1T2/) | <img src="../../assets/images/hardware/prototype/fasteners.png" width="80"/> | **High**: Required for durable threads. |

## Estimated Total Prototype Cost
- **Absolute cheapest build (Manual XY, 10X lens):** ~$150
- **Recommended prototype build (MGN12 rails, 40X Plan lens, manual):** ~$230
- **Automated motion build (add NEMA 17 & drivers):** ~$280
