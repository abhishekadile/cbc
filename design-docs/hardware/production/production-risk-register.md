# Production Risk Register

This document tracks anticipated risks in transitioning from prototype to production hardware.

| Risk | Likelihood | Impact | Affected Subsystem | Mitigation | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Blurry images | High | High | Optics/Focus | Implement robust autofocus algorithm; ensure Z-axis rigidity. | Open |
| Poor focus repeatability | Medium | High | Motion (Z) | Use high-precision lead screw and closed-loop control. | Open |
| Stage backlash | High | Medium | Motion (XY) | Use pre-loaded linear rails and anti-backlash nuts. | Open |
| Uneven illumination | Medium | Medium | Illumination | Calibrate LED array; use high-quality diffuser. | Open |
| Misaligned multispectral images | Medium | High | Optics/Capture | Ensure rigid camera mount; implement software alignment. | Open |
| Public dataset mismatch | High | Medium | AI Pipeline | Extensive fine-tuning on device-specific data. | Open |
| Poor segmentation on device images | Medium | High | AI/CV Pipeline | Active learning loop; human review of edge cases. | Open |
| Stitching failure | Low | High | Software/Motion | Ensure 40-60% overlap; improve feature extraction. | Open |
| Cartridge optical distortion | Medium | High | Sample | Work with manufacturer to control material clarity. | Open |
| Dust/debris false positives | High | Medium | AI/CV Pipeline | Enclosure; software filtering of static artifacts. | Open |
| Production tolerance issues | Medium | Medium | Manufacturing | Define strict tolerances for critical optical mounts. | Open |
