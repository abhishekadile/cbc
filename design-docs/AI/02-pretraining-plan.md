# Pretraining Plan

This document outlines the strategy for pretraining AI models using public datasets before fine-tuning on device-specific imagery.

## Dataset Categories

We will collect and standardize datasets across these categories:

- RBC/WBC/platelet detection datasets
- WBC classification datasets
- Microscopy segmentation datasets
- Unlabeled microscope image datasets if available
- Internally captured device images

## Known Useful Datasets

- **BCCD**: Blood Cell Count and Detection Dataset. `TODO: verify dataset link and license`
- **PBC / Acevedo**: Peripheral blood cell dataset. `TODO: verify dataset link and license`
- **Raabin-WBC**: `TODO: verify dataset link and license`
- **LISC**: `TODO: verify dataset link and license`
- **BloodMNIST**: `TODO: verify dataset link and license`
- **ALL-IDB** or **C-NMC**: Only for later abnormal WBC research. `TODO: verify dataset link and license`
- **BBBC**: Broad Bioimage Benchmark Collection (microscopy datasets where relevant). `TODO: verify dataset link and license`

## Handling Dataset Variability

- **Labeled detection datasets**: Convert to YOLO or COCO format.
- **Labeled classification datasets**: Convert to standardized CSV/folder structures.
- **Segmentation mask datasets**: Normalize mask values (e.g., 0 for background, 255 for object).
- **Unlabeled datasets**: Use for self-supervised learning if compute allows.
- **Mismatched stain/color/magnification**: Apply heavy data augmentation (color jitter, scaling) to simulate variation.
- **Monochrome camera images**: 
- **Multispectral images**: 

## Proposed Dataset Folder Structure

```
datasets/
  raw/
    public/
    internal/
  processed/
    detection/
    segmentation/
    classification/
    multispectral/
  labels/
    yolo/
    coco/
    masks/
    classification_csv/
  splits/
    train.txt
    val.txt
    test_locked.txt
  metadata/
    dataset_registry.csv
    label_schema.json
    preprocessing_config.yaml
```

## Dataset Registry Columns

The `dataset_registry.csv` will track:
- `dataset_name`
- `source`
- `license`
- `image_type`
- `label_type`
- `cell_types`
- `magnification`
- `stain`
- `color_mode`
- `number_of_images`
- `status`
- `notes`

## Pretraining Stages

1. Collect datasets and verify licenses.
2. Convert labels to common format.
3. Convert RGB to grayscale variants.
4. Normalize resolution and metadata.
5. Train baseline detector/segmenter.
6. Train WBC classifier.
7. Fine-tune on internal device images.
8. Evaluate on locked test set.

## Evaluation Metrics

- mAP (Mean Average Precision)
- Precision
- Recall
- Dice coefficient
- IoU (Intersection over Union)
- Count error
- Percent count error
- Bad image rejection rate
