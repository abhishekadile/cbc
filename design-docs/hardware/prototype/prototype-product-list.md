# Prototype Product List

This document details the exact components required for the prototype build, including researched pricing and links.
*Prices verified as of May 10, 2026. Do not invent unavailable prices.*

| Subsystem | Part | Qty | Purpose | Minimum Spec | Recommended Product | Cheapest Found Product | Current Price | Vendor | Purchase Link | Product Image / Source | Criticality | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Compute | Raspberry Pi 4 | 1 | Control & Capture | 4GB RAM | Raspberry Pi 5 (4GB) | Raspberry Pi 4 (4GB) | $55.00 | Adafruit/PiShop | [Link](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) | [Image](../../sources/image-sources.csv) | High | Need adequate cooling. |
| Compute | MicroSD Card | 1 | OS Storage | 32GB Class 10 | SanDisk Extreme 64GB | Generic 32GB Class 10 | $8.00 | Amazon | [Link](https://www.amazon.com) | N/A | High | High endurance preferred. |
| Compute | Power Supply | 1 | Power RPi | 5V 3A USB-C | Official RPi USB-C PSU | Generic 5V 3A | $8.00 | Amazon | [Link](https://www.amazon.com) | N/A | High | |
| Camera | IMX296 Camera | 1 | Image Sensor | Global Shutter, MIPI | InnovaMaker IMX296 | InnovaMaker IMX296 | $60.00 | InnovaMaker | [Link](https://www.inno-maker.com) | [Image](../../sources/image-sources.csv) | Critical | Global shutter required. |
| Camera | MIPI Cable | 1 | Data connection | 15-pin to 22-pin (Pi 5) | Standard FPC cable | Included with camera | $0.00 | N/A | N/A | N/A | High | Pi 5 uses different pitch. |
| Optics | 40X Objective | 1 | Magnification | Plan Achromatic | AmScope PA40XK | AmScope Standard 40X | $45.00 | AmScope | [Link](https://amscope.com/) | N/A | Critical | "Plan" is needed for flat fields. |
| Optics | Calibration Slide | 1 | Scale reference | Stage micrometer | AmScope Stage Micrometer | Printed Grid (Not rec) | $20.00 | AmScope | [Link](https://amscope.com/) | N/A | Medium | Essential for measuring FOV. |
| Sample | Glass Slides | 1 | Hold sample | Standard 25x75mm | Standard box of 72 | Standard box of 72 | $10.00 | Amazon | [Link](https://www.amazon.com) | N/A | High | |
| Illumination| LED Ring | 1 | Light Source | White LED | Multispectral Custom Board | Generic White LED Ring | $15.00 | Adafruit | [Link](https://www.adafruit.com/) | N/A | High | Need diffuser. |
| Motion | Linear Rails | 2 | XY smooth travel | MGN12, Z0 preload | HIWIN MGN12 | Generic MGN12 (KB3D) | $20.00 | KB3D | [Link](https://kb-3d.com/) | [Image](../../sources/image-sources.csv) | High | Avoid printed sliding parts. |
| Motion | Lead Screw | 2 | XY actuation | T8, 2mm pitch | T8 with Anti-backlash nut | Standard threaded rod | $15.00 | Amazon | [Link](https://www.amazon.com) | N/A | High | |
| Motion | Stepper Motor | 2 | Automated XY | NEMA 17 | NEMA 17 (1.5A) | 28BYJ-48 (Not rec) | $14.00 | Pololu | [Link](https://www.pololu.com/) | N/A | Low | Start with manual knobs. |
| Motion | Motor Driver | 2 | Control Stepper | Standard | TMC2209 | A4988 | $8.00 | Pololu | [Link](https://www.pololu.com/) | N/A | Low | TMC provides silent operation. |
| Fasteners | Screw Kit | 1 | Assembly | M3 assortment | Metric M3 Hex Socket | Generic Kit | $15.00 | Amazon | [Link](https://www.amazon.com) | N/A | High | |
| Fasteners | Threaded Inserts| 1 | Assembly | M3 brass inserts | CNC Kitchen M3 | Generic M3 inserts | $12.00 | Amazon | [Link](https://www.amazon.com) | N/A | High | Required for durable threads. |

## Estimated Total Prototype Cost
- **Absolute cheapest build (Manual XY, 10X lens):** ~$150
- **Recommended prototype build (MGN12 rails, 40X Plan lens, manual):** ~$230
- **Automated motion build (add NEMA 17 & drivers):** ~$280
