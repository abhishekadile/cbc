# CBC Multispectral Imaging System Design Documentation

This is a research and engineering prototype for a multispectral CBC image acquisition system. It is not for diagnosis, treatment, or clinical use.

## Folder Structure Guide

This documentation is organized into four main pillars that map directly to the system's architecture and development lifecycle:

### 1. `hardware/`
Contains the physical design of the CBC scanner. It is split into two tracks:
- **`prototype/`**: Focuses on rapid iteration. It details the 3D-printing strategy, manual assembly guides, and off-the-shelf components required to build the first functional unit. The goal here is proving the optical path and software integration.
- **`production/`**: Focuses on reliability and scaling. It outlines the transition to rigid materials, precision linear guides, and the engineering requirements for a known-volume fluid cartridge necessary for absolute cell concentration calculations.

### 2. `embedded-software/`
Details the software running directly on the hardware (the Raspberry Pi). This folder covers:
- The tech stack (Python, FastAPI, `uv`, `libcamera`/`Picamera2`).
- How the device orchestrates the capture sequence, including multispectral LED synchronization and motor control.
- The precise data schema (`manifest.json`) used to package images and metadata into a "Scan Session" before sending it to the cloud or AI pipeline.

### 3. `AI/`
Outlines the entire data science and machine learning workstream. This is the brain of the system, responsible for counting and classifying cells:
- **Model Strategy**: Deciding which architectures to use (e.g., YOLO11-seg for detection, U-Net for precise segmentation, EfficientNet for classification).
- **Pretraining & Data**: How public datasets are used to bootstrap models before fine-tuning on device-specific images.
- **Computer Vision (CV) Pipeline**: The classical algorithms (thresholding, watershed) used for immediate object detection, image quality control, and generating pseudo-labels.
- **Labeling & Evaluation**: The strict workflow for human-in-the-loop annotation and the statistical metrics used to prove accuracy.

### 4. `cloud/`
Describes the off-device architecture needed to scale the project. While the scanner is designed to be "local-first," this folder covers:
- **Data Management**: How scan sessions are securely uploaded and stored in object storage (e.g., S3).
- **Fleet & Model Registries**: Tracking active devices in the field and managing over-the-air updates for newly trained AI models.
- **Experiment Tracking**: The infrastructure (like MLflow) used by researchers to track model training runs and dataset versions.

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
