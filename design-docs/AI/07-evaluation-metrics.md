# Evaluation Metrics

This document defines the statistical metrics used to evaluate the performance of the AI and CV pipelines.

## Detection Metrics
Evaluated on bounding box predictions (e.g., YOLO output).
- **Precision**: True Positives / (True Positives + False Positives). How many of the predicted cells are actually cells?
- **Recall**: True Positives / (True Positives + False Negatives). How many of the actual cells did we find?
- **mAP50**: Mean Average Precision at an Intersection over Union (IoU) threshold of 0.50. The primary metric for general detection capability.
- **mAP50-95**: Mean Average Precision averaged across IoU thresholds from 0.50 to 0.95. A strict metric that evaluates how perfectly the bounding box aligns with the object.

## Segmentation Metrics
Evaluated on pixel-perfect masks (e.g., U-Net output).
- **IoU (Intersection over Union) / Jaccard Index**: Area of Overlap / Area of Union between the predicted mask and ground truth mask.
- **Dice Coefficient (F1 Score for pixels)**: `2 * |Intersection| / (|Predicted| + |GroundTruth|)`. Highly correlated with IoU but penalizes false positives/negatives differently.
- **Boundary Quality**: Metrics evaluating the distance between the predicted contour and the ground truth contour, crucial for tightly clumped cells.

## Counting Metrics
The ultimate goal of the system is an accurate count, even if segmentation isn't perfect.
- **Absolute Count Error**: `|Predicted Count - Actual Count|` per image or per scan.
- **Percent Count Error**: `(|Predicted Count - Actual Count| / Actual Count) * 100`.
- **Mean Absolute Error (MAE)**: Average of the Absolute Count Errors across the test dataset.
- **Bland-Altman Analysis**: To be implemented later for reference comparison against clinical gold-standard hematology analyzers.

## Quality Control Metrics
Evaluates the robustness of the automated pipeline.
- **Bad Image Rejection Rate**: The percentage of truly bad images successfully caught and rejected by the CV focus/brightness checks.
- **False Rejection Rate**: The percentage of perfectly good images incorrectly flagged as bad.
- **CV/AI Disagreement Rate**: How often the classical CV pipeline and the Neural Network disagree on the count by more than a set threshold (e.g., 10%).
- **Stitching Success Rate**: Percentage of scans where the 5-10 overlapping images were successfully aligned into a mosaic without fatal errors.

## Dataset & Operations Metrics
- **Label Review Rate**: How many images are being sent to the human review queue per day.
- **Pseudo-label Acceptance Rate**: How often a human reviewer accepts an AI-generated pseudo-label without modification.
- **Class Imbalance**: Tracking the ratio of RBCs to WBCs to platelets in the training set to ensure minority classes are sampled correctly.
