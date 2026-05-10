# Production Risk Register

This document tracks anticipated risks in transitioning from prototype to production hardware and deploying the device at scale.

| Risk | Likelihood | Impact | Affected Subsystem | Mitigation | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Blurry images from vibration** | High | High | Optics/Focus | Implement robust autofocus algorithm; ensure Z-axis rigidity; use vibration-dampening feet. | Open |
| **Poor focus repeatability** | Medium | High | Motion (Z) | Use high-precision lead screw and closed-loop control; switch to machined metal mounts. | Open |
| **Stage backlash ruining stitching** | High | Medium | Motion (XY) | Use pre-loaded linear rails (Z1 preload) and anti-backlash nuts; implement software backlash compensation. | Open |
| **Uneven illumination (vignetting)**| Medium | Medium | Illumination | Calibrate LED array; use high-quality diffuser; implement software flat-field correction. | Open |
| **LED intensity degradation** | Medium | High | Illumination | Implement closed-loop photodiode feedback to maintain constant lux over the device lifespan. | Open |
| **Misaligned multispectral images** | Medium | High | Optics/Capture | Ensure extremely rigid camera mount; implement software-based phase correlation alignment. | Open |
| **Public dataset mismatch** | High | Medium | AI Pipeline | Extensive fine-tuning on device-specific data; use color augmentation during pretraining. | Open |
| **Poor segmentation on device images**| Medium | High | AI/CV Pipeline | Implement an active learning loop; enforce human review of edge cases and low-confidence predictions. | Open |
| **Stitching failure** | Low | High | Software/Motion | Ensure 40-60% overlap hardware capability; improve feature extraction algorithms (SIFT/ORB). | Open |
| **Cartridge optical distortion** | Medium | High | Sample/Cartridge | Work closely with medical plastics manufacturer to control material clarity and chamber depth tolerance. | Open |
| **Dust/debris false positives** | High | Medium | AI/CV Pipeline | Design a sealed optical enclosure; implement software filtering of static artifacts using background subtraction. | Open |
| **Production tolerance issues** | Medium | Medium | Manufacturing | Define strict GD&T tolerances for critical optical mounts and linear rail mating surfaces. | Open |
