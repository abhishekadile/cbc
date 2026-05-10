# Model Strategy

**Question**: Should we train from scratch or use a pretrained model?

**Recommendation**: Start from pretrained models. Do not train from scratch initially. Use our compute budget for domain adaptation, public dataset pretraining/fine-tuning, self-supervised learning, and internal device fine-tuning.

Training from scratch requires massive datasets and extensive tuning. Leveraging existing foundation models accelerates development and improves generalization.

## Model Families and Specific Options

### Detection and Segmentation
- **Ultralytics YOLOv8-seg or YOLO11-seg**: Highly recommended for fast, real-time instance segmentation and detection. Excellent ecosystem and easy export to edge devices (like the Raspberry Pi or an attached Coral TPU).
- **Ultralytics YOLOv8/YOLO11 (Detection only)**: A solid baseline if bounding boxes are sufficient and full masks are too computationally expensive.
- **RT-DETR**: A strong transformer-based alternative to YOLO for the detection baseline.
- **Mask R-CNN (via Detectron2 or TorchVision)**: The classical standard for instance segmentation. Heavier than YOLO, but highly accurate.
- **U-Net / UNet++ (via `segmentation_models_pytorch`)**: The standard for semantic segmentation in biomedical imaging. Great for delineating complex cell boundaries.
- **Cellpose / StarDist**: Specialized models pre-trained specifically on cellular structures. Excellent for out-of-the-box cell segmentation, though they may require tuning for blood cells specifically.
- **Segment Anything (SAM 2)**: Useful for *assisted labeling* (human-in-the-loop annotation). It should not be used for unsupervised, automated counting in production unless rigorously validated, due to hallucination risks and high compute costs.

### Classification (WBC Subtyping)
- **ResNet50**: The reliable, standard baseline.
- **EfficientNet-B0/B3**: Better accuracy-to-parameter ratio, excellent for edge deployment.
- **ConvNeXt-Tiny**: Modern CNN architecture that competes with Vision Transformers.
- **ViT-B/16**: Vision Transformer, requires more data to train effectively but offers high performance.
- **DINOv2**: Excellent for extracting embeddings for self-supervised learning.
- **BioMedCLIP**: Experimental feature extractor for zero-shot or few-shot tasks.

### Image Quality Model
- **Classical**: Sharpness metrics such as Laplacian variance (requires no training).
- **Deep Learning**: A small CNN classifier (or a lightweight EfficientNet/ResNet) trained as a binary classifier to flag images as "usable" or "unusable" (e.g., severe blur, totally empty, huge bubble).

### Counting Strategy
- **Primary Method**: Count directly from the resulting masks or bounding boxes produced by the detection/segmentation models.
- **Future Research Option**: Direct density-map counting models (e.g., CSRNet style) if cell density becomes too high for instance segmentation to handle clumps.
- **Validation**: Constantly compare the classical CV count vs. the AI count vs. human-reviewed labels to track drift.

## Defined Tasks

1. **Image quality detection**: Reject bad frames immediately.
2. **Object detection**: Draw bounding boxes around cells.
3. **Instance segmentation**: Draw precise pixel masks for individual overlapping cells.
4. **Semantic segmentation**: Classify every pixel in the image (e.g., background, RBC, WBC).
5. **WBC classification**: Categorize segmented WBCs into subtypes (Neutrophil, Lymphocyte, etc.).
6. **Pseudo-labeling**: Use classical CV to auto-generate training data.
7. **Active learning**: Automatically flag edge cases for human review.
8. **Uncertainty estimation**: Ensure the model provides a confidence score for its counts.
9. **Count error tracking**: Monitor performance against clinical baselines.

## Decision Table

| Task | Recommended First Model | Alternative | Reason |
| :--- | :--- | :--- | :--- |
| **Detection / Instance Seg** | YOLO11-seg | Mask R-CNN | YOLO is significantly faster and easier to deploy on edge hardware while maintaining high accuracy. |
| **Semantic Seg** | UNet (EfficientNet backbone) | DeepLabV3+ | UNet is the proven standard for biomedical tasks. `segmentation_models_pytorch` makes it trivial to swap backbones. |
| **Classification** | EfficientNet-B0 | ResNet50 | EfficientNet offers a better trade-off between speed and accuracy for classifying cropped cell images. |
| **Quality Control** | Variance of Laplacian (CV) | Small CNN | Classical CV is instant and requires zero labeled data. Neural networks can be added later for complex artifact detection. |
