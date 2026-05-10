# AI and Computer Vision

This directory contains the design documentation for the Artificial Intelligence and classical Computer Vision (CV) pipelines used to process images captured by the CBC scanner.

The goal is to transform raw microscope images into robust object counts and classifications.

## Workflow Overview

1. **Model Strategy (`01-model-strategy.md`)**: Deciding the core architectures (e.g., YOLO vs. U-Net) and whether to train from scratch or fine-tune.
2. **Pretraining Plan (`02-pretraining-plan.md`)**: Leveraging open-source datasets (like BCCD or BloodMNIST) to build foundational model weights before using our own device data.
3. **Computer Vision System (`03-computer-vision-system.md`)**: Using classical algorithms (thresholding, watershed) for immediate object detection, quality control, and generating pseudo-labels for the AI.
4. **Final AI/CV Pipeline (`04-final-ai-cv-pipeline.md`)**: The integrated production flow that merges hardware acquisition, CV, and AI models into a single continuous loop.
5. **AI Tech Stack (`05-ai-tech-stack.md`)**: The specific Python libraries (PyTorch, Ultralytics), environment managers (uv), and best practices used for development.
6. **Dataset Format and Labeling (`06-dataset-format-and-labeling.md`)**: How data is structured, annotated, and prepared for training.
7. **Evaluation Metrics (`07-evaluation-metrics.md`)**: The statistical methods used to prove the models are actually working (e.g., mAP, Dice score, Count Error).
