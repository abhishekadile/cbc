# AI and Computer Vision

This directory outlines the AI and classical Computer Vision (CV) strategies for processing images captured by the CBC scanner.

The goal is to move from initial image capture to robust object segmentation, classification, and counting.

## Workstream Overview

- **Model Strategy**: Deciding between training from scratch vs. fine-tuning pretrained models.
- **Pretraining**: Leveraging public datasets to build foundational capabilities.
- **Device-Specific Fine-Tuning**: Adapting models to the specific optics and illumination of the prototype.
- **CV Segmentation**: Using classical methods for initial object detection and quality control.
- **Pseudo-Labeling**: Using CV outputs to bootstrap the AI training dataset.
- **Final Hybrid Pipeline**: Integrating both approaches for maximum accuracy and error detection.
