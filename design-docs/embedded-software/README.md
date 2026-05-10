# Embedded Software

The embedded software runs on the Raspberry Pi and acts as the brain of the acquisition hardware. It orchestrates the camera, the lighting, the motion stage, and the data packaging.

## Core Responsibilities

- **Raspberry Pi as Acquisition Controller**: The Pi handles all high-level scheduling, file system operations, and network communication.
- **Camera Control**: Interfaces with the IMX296 sensor via `Picamera2` or `libcamera`, configuring exposure, gain, and format.
- **LED Control**: Toggles GPIO pins to control the multispectral LED array, ensuring the correct wavelength is active during exposure.
- **Future XY/Z Motion Control**: Interfaces with stepper motor drivers (via GPIO or I2C) to move the stage for stitching and adjust focus.
- **Scan Session Manager**: Orchestrates the multi-step process of capturing a full slide (move stage -> set LED -> capture -> next wavelength -> next position).
- **REST API**: Exposes endpoints (via FastAPI) to start, stop, and configure scans.
- **Local UI**: Serves a local React dashboard for the user operating the machine.
- **Metadata**: Collects hardware state (temperature, exposure settings) and packages it with the images.
- **Logs**: Maintains detailed diagnostic logs for troubleshooting.

## Future Microcontroller Option
As the system scales to closed-loop motors and microsecond-level LED pulsing, the Raspberry Pi's non-real-time Linux OS may introduce jitter. Future architectures will delegate real-time hardware IO to an attached microcontroller (like an RP2040 or STM32), which will communicate with the Pi via Serial/I2C.
