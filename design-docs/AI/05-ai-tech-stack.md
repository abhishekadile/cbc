# AI Tech Stack & Best Practices

This document defines the software stack, project structure, and engineering best practices for developing the AI models.

## Recommended Stack

- **Language**: Python 3.11 or 3.12
- **Environment & Dependencies**: `uv` (significantly faster and more reliable than pip/conda).
- **Deep Learning Framework**: `PyTorch` and `torchvision`.
- **Model Libraries**: 
  - `ultralytics` (for YOLOv8/YOLO11).
  - `segmentation-models-pytorch` (for U-Net, DeepLab, etc.).
  - *Optional*: `Detectron2` (if Mask R-CNN is pursued).
- **Computer Vision**: `OpenCV` (`cv2`), `scikit-image` (`skimage`).
- **Data Science**: `NumPy`, `SciPy`, `pandas`, `matplotlib`.
- **Augmentation**: `albumentations` (crucial for medical imaging augmentations like elastic transform, grid distortion, and color jitter).
- **Utilities**: `tqdm` (progress bars), `pydantic` (data validation).
- **Configuration**: `hydra` or `OmegaConf` (for config-driven experiments).
- **Experiment Tracking**: `MLflow` or `Weights & Biases (W&B)` (for tracking loss, metrics, and hyperparameters).
- **Annotation & Review**: `FiftyOne`, `CVAT`, `Label Studio`, or `Roboflow`.
- **Data Versioning**: `DVC` (Data Version Control) or `Git LFS`.
- **Code Quality**: `pytest` (testing), `ruff` (linting/formatting), `mypy` (optional type checking), `pre-commit` hooks.

## Environment Setup (Using `uv`)

```bash
uv init
uv add torch torchvision opencv-python scikit-image pandas numpy scipy albumentations ultralytics segmentation-models-pytorch matplotlib tqdm pydantic
uv run python scripts/train_detector.py
```

## Suggested Project Structure

```
ai/
  pyproject.toml
  uv.lock
  src/
    cbc_ai/
      data/         # Dataset loaders, transforms
      cv/           # Classical CV pipelines
      models/       # PyTorch model definitions/wrappers
      training/     # Training loops, loss functions
      evaluation/   # Metrics calculation
      inference/    # Deployment and prediction scripts
      utils/        # Logging, config parsing
  configs/          # YAML configuration files
  notebooks/        # Jupyter notebooks for EDA and visualization
  scripts/          # Entry points (e.g., train.py, evaluate.py)
  tests/            # Pytest test suite
```

## Engineering Best Practices

- **Config-driven experiments**: Never hardcode hyperparameters. Use YAML configs.
- **Fixed random seeds**: Always seed PyTorch, NumPy, and Python's `random` module at the start of training to ensure reproducibility.
- **Version datasets**: Treat data like code. Use DVC to track dataset versions alongside model weights.
- **Locked test set**: Establish a representative test set immediately and *never* train on it. 
- **Save preprocessing config with the model**: The exact normalization values (mean/std) and resizing logic used during training must be saved alongside the `.pt` or `.onnx` model file to ensure inference matches training.
- **Log metrics every run**: Use MLflow/W&B to track every experiment.
- **Separate Pseudo-labels**: Keep a strict metadata separation between human-verified labels and AI/CV generated pseudo-labels. Train models primarily on human-verified data; use pseudo-labels only for pretraining or with weighted loss.
- **Model Cards**: Create a model card for every deployed model detailing its training data, performance metrics, and known limitations.
