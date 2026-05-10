# Embedded Tech Stack

This document defines the software stack running on the Raspberry Pi.

## Core Stack
- **Language**: Python 3.11+
- **Environment**: `uv` for lightning-fast dependency management and isolated virtual environments.
- **Web Server**: `FastAPI` (running via Uvicorn). Provides high-performance async REST APIs for the local UI.
- **Camera API**: `Picamera2` (the official Python library built on top of `libcamera`). Critical for accessing low-level sensor controls of the IMX296.
- **Data Validation**: `pydantic` for strictly typing API payloads and metadata manifests.
- **Local Database**: `SQLite` (optional, for tracking scan history locally before cloud upload).
- **Local Preprocessing**: `OpenCV` (`cv2-python-headless`) for running fast local checks like the focus metric before saving the image.
- **Service Management**: `systemd` to ensure the FastAPI server and hardware daemons start automatically on boot.

## Hardware IO Libraries
- **GPIO Control**: `gpiozero` or `RPi.GPIO` for toggling LED drivers and basic limit switches.
- **I2C/SPI**: `smbus2` or `spidev` for communicating with potential external ADCs, DACs, or motor controllers.

## Future Architecture (Real-Time Control)
If precise microsecond timing is needed for strobing LEDs in sync with the global shutter:
- **Microcontroller Option**: Raspberry Pi Pico (RP2040) or STM32.
- **Microcontroller Firmware**: Written in C/C++ (PlatformIO/Arduino) or MicroPython.
- **Communication Protocol**: Standard UART serial or I2C between the Pi and the MCU.
