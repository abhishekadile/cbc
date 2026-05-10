# Production Hardware Specification

The production hardware represents the evolution of the system from a rapidly iteratable prototype into a reliable, repeatable, and manufacturable device suitable for field use and data collection at scale.

## Production Design Goals
- **Manufacturability**: Design for Assembly (DFA) using standard fasteners, minimal manual adjustment, and easily sourced core components.
- **Reliability**: Withstand shipping and daily field use without losing optical alignment.
- **Serviceability**: Allow easy field replacement of the camera module, LED array, or main compute board without requiring full optical recalibration.

## Core Advancements from Prototype

- **Cartridge Interface**: The system will move away from standard glass slides and manual clamping to a custom, engineered cartridge slot.
- **Known-Volume Imaging**: The core goal of the production hardware is to enable absolute concentration calculations. This requires the hardware to image a tightly controlled, specific volume of fluid.
- **Optical Stability**: Transition from 3D printed towers to sheet metal, machined aluminum, or rigid injection-molded chassis components to ensure the focal plane remains perfectly perpendicular to the sensor.
- **Controlled Illumination**: Replace generic white LEDs with a custom-designed PCB containing calibrated multispectral LEDs (e.g., 405nm, 470nm, 530nm, 660nm) with current-controlled feedback to ensure intensity does not drift over time.
- **Controlled Motion**: Use precision linear guides (e.g., HIWIN/THK) and closed-loop steppers (steppers with encoders) to prevent missed steps, stage backlash, and ensure perfect overlap for stitching.
- **Calibration Workflow**: Integrate a hardware calibration routine, potentially using a fixed optical target within the device or a special calibration cartridge inserted periodically.

## Production Materials
- **Parts that should be machined/folded metal**: Main chassis, Z-axis optical tower, objective lens mount.
- **Parts that should be injection molded**: Exterior enclosure, cartridge receiver.
- **Parts that can remain 3D printed or low-cost**: Internal cable routing clips, non-load-bearing baffles for light blocking.

## Failure Modes & Mitigations
- **Failure**: LED intensity degrades over thousands of scans, changing image brightness and breaking AI models.
    - **Mitigation**: Implement a photodiode feedback loop on the LED board to automatically adjust PWM/current to maintain constant lux.
- **Failure**: Dust accumulating on the sensor over time.
    - **Mitigation**: Sealed optical path from the objective lens to the camera sensor.
- **Failure**: User inserts cartridge incorrectly.
    - **Mitigation**: Asymmetric cartridge design (poka-yoke) so it only fits one way.

## Validation Plan
1. **Vibration testing**: Verify optical alignment holds after simulated transit.
2. **Thermal testing**: Verify image quality does not degrade as the internal enclosure temperature rises from Pi/LED heat.
3. **Repeatability testing**: Scan the same calibration target 100 times, dismounting and remounting the target each time, to verify XY positioning and focus repeatability.
