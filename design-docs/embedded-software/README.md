# Embedded Software Design Overview

The embedded software runs on the Raspberry Pi and is responsible for hardware orchestration, image acquisition, and data management.

## Core Responsibilities

- **Raspberry Pi Control**: Acts as the central hub, controlling the IMX296 camera capture process via libcamera/Picamera2.
- **Scan Session Manager**: Orchestrates the scanning process, handling the logic for capturing multiple fields of view.
- **Metadata Collection**: Gathers critical scan context (timestamp, exposure settings, wavelength, position) and stores it.
- **LED Control**: Manages the multispectral LED array, turning on specific wavelengths synchronously with camera exposure.
- **Future XY/Z Motion Control**: Interfaces with motor drivers to move the stage and adjust focus.
- **REST API/UI Integration**: Exposes endpoints for a local or remote user interface to start/stop scans and review data.
- **Future Microcontroller Option**: Real-time tasks (like exact step counting for motors or microsecond-level LED pulsing) may be offloaded to an RP2040 or STM32 communicating with the Pi over serial/I2C.

## File Organization & Expected Output

The embedded software organizes captured data systematically. A typical scan session output directory will include:

- `raw/`: Unprocessed raw images directly from the sensor.
- `thumbnails/`: Downscaled versions for quick UI rendering.
- `stitched/`: The final stitched mosaic image (if computed locally).
- `metadata/manifest.json`: Contains all scan parameters, timestamps, and hardware state.
- `logs/`: Diagnostic logs for the specific session.
