# Architecture

The system uses a supervisor-controller architecture.

Currently, the Raspberry Pi acts as both supervisor and controller, directly managing the camera and running the web dashboard.

In the future, the Raspberry Pi will act solely as the supervisor and image processor. A dedicated microcontroller (e.g., STM32 or RP2040) will act as the timing controller, receiving high-level commands over serial and directly driving the XY stage, Z focus, and multispectral LEDs with microsecond precision, as well as triggering the camera externally.
