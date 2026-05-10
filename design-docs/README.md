# CBC Multispectral Imaging System Design Documentation

This is a research and engineering prototype for a multispectral CBC image acquisition system. It is not for diagnosis, treatment, or clinical use.

## Folder Structure Guide

- **`hardware/`**: Contains specifications, product lists, 3D printing plans, and assembly guides for both the prototype and future production hardware.
- **`embedded-software/`**: Details the Raspberry Pi control software, scan session management, API integration, and metadata collection.
- **`AI/`**: Outlines the AI workstream, including model strategy, pretraining plans, CV segmentation, and the final hybrid pipeline.
- **`cloud/`**: Describes the future cloud architecture for data storage, experiment tracking, and device management.

## Build Phases

The project will follow these sequential build phases:

1. **Prototype imaging system**: Build the initial 3D-printed hardware, integrate the IMX296 camera, and establish basic control.
2. **CV-first segmentation**: Implement classical computer vision to detect objects and create pseudo-labels.
3. **AI pretraining and fine-tuning**: Pretrain models on public datasets and fine-tune on device-captured images.
4. **Hybrid AI/CV pipeline**: Integrate both approaches for robust counting and quality control.
5. **Production hardware and cartridge**: Transition to a rigid frame, controlled cartridge, and repeatable optical path.
6. **Cloud scaling and data management**: Implement cloud uploads, scan dashboards, and a model registry.

## Prototype Goals

The first prototype goal is *not* clinical accuracy. The initial objectives are to:
- capture clear microscope images
- capture 5 to 10 overlapping images
- stitch them together
- segment visible objects
- count objects
- create a dataset loop
- compare CV counts, AI counts, and reviewed labels
