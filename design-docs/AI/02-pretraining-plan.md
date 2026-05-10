# Pretraining Plan

This document details the strategy for bootstrapping the AI models using public datasets before fine-tuning them on our device-specific imagery.

## Verified Dataset Sources

See `design-docs/sources/dataset-sources.csv` for full details.

- **BCCD (Blood Cell Count and Detection)**: Small dataset (364 images) with Bounding Boxes for RBC, WBC, and Platelets. Good for initial YOLO detection pipeline testing.
- **PBC (Acevedo Peripheral Blood Cells)**: Large dataset (17k+ images) for WBC sub-classification.
- **Raabin-WBC**: Comprehensive dataset with cell locations, types, and segmented nuclei/cytoplasm. Excellent for U-Net / instance segmentation pretraining.
- **BloodMNIST**: Part of MedMNIST v2. 28x28 classification dataset. Good for testing model architectures quickly, but too low-res for final production use.
- **BBBC (Broad Bioimage Benchmark Collection)**: Contains various microscopy datasets useful for general cell segmentation pretraining.

## Dataset Handling & Preprocessing

- **Detection labels**: Convert all bounding box datasets (e.g., Pascal VOC XML from BCCD) to standard YOLO format and COCO JSON format.
- **Segmentation masks**: Standardize all masks to a common format (e.g., binary PNGs where 0=background, 255=object, or indexed PNGs for multi-class).
- **Classification datasets**: Organize into standard PyTorch ImageFolder structures or use a central CSV mapping file.
- **Unlabeled datasets**: Utilize for self-supervised learning (e.g., training a DINOv2 backbone) or process through the CV pseudo-labeling pipeline.
- **RGB vs. Monochrome**: Most public datasets are RGB (stained). If our prototype uses a monochrome sensor, we must create grayscale versions of the public data during preprocessing.
- **Multispectral Device Images**: Store as aligned per-wavelength channels (e.g., a 4-channel TIFF instead of 3-channel RGB).
- **Locked Test Set**: A portion of the data (especially device-specific data) must be locked away. It must *never* be auto-labeled, pseudo-labeled, or used during any training phase.

## Proposed Dataset Structure

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

## Training Stages

1. **Collect datasets**: Download from sources listed in the CSV.
2. **Verify licenses**: Ensure usage complies with MIT, CC BY 4.0, etc.
3. **Normalize labels**: Run scripts to convert everything to YOLO/COCO.
4. **Create grayscale versions**: Synthesize monochrome data from RGB stains.
5. **Train baseline detector**: Train YOLO11 on BCCD (grayscale) to prove the pipeline works.
6. **Train baseline segmenter**: Train UNet on Raabin-WBC segmentation masks.
7. **Train WBC classifier**: Train EfficientNet on the PBC dataset.
8. **Fine-tune on device images**: Freeze backbones, train on images captured by the prototype hardware.
9. **Add multispectral channels**: Modify the input layer of the models to accept N-channels instead of 1 or 3, and train on multispectral data.
10. **Active learning loop**: Deploy the model, flag uncertain predictions, have humans review them, and add them back to the training set.
11. **Evaluate on locked test set**: Perform the final benchmark.
