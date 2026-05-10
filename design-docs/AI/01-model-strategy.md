# Model Strategy

**Question**: Should we train from scratch or start from pretrained image models?

**Recommendation**: Do not train from scratch initially. Use a pretrained image backbone/model to save compute and improve generalization. Use available compute for domain-specific pretraining and fine-tuning, not full scratch training.

## Rationale

- **Training from scratch** requires huge amounts of labeled data and extensive hyperparameter tuning. We currently lack a massive internal dataset.
- **Starting from pretrained image models** is faster, as the lower layers already understand fundamental features like edges and textures.
- We will use self-supervised or supervised pretraining on public microscopy/blood datasets to bridge the gap between natural images and our domain.
- We will then fine-tune on device-specific images captured from the prototype.
- Later, if the dataset becomes large enough, evaluate training from scratch as a research experiment.

## Candidate Model Families

- **YOLO** (e.g., YOLOv8/v9): For fast, real-time detection and segmentation.
- **U-Net / UNet++**: The standard for biomedical image segmentation.
- **Mask R-CNN**: For a strong instance segmentation baseline.
- **Cellpose-style models**: Specifically designed for cell segmentation.
- **Backbones (ConvNeXt, EfficientNet, ResNet, ViT)**: For classification tasks.
- **SAM-style segmentation**: May be useful for assisted labeling (human-in-the-loop), but should be validated carefully before automated use.

## Defined Model Tasks

1. **Image quality detection**: Flagging out-of-focus, under/overexposed, or blank images.
2. **Cell/object segmentation**: Generating precise pixel masks for objects of interest.
3. **Cell detection**: Identifying bounding boxes around objects.
4. **Cell classification**: Categorizing detected objects (e.g., differentiating types).
5. **Count estimation**: Deriving counts from masks/boxes.
6. **Quality control and uncertainty scoring**: Providing confidence metrics for AI outputs.
