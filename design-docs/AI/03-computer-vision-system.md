# Computer Vision System

This document describes the classical Computer Vision (CV) pipeline used for initial object segmentation and pseudo-label generation.

## Rationale for CV-First Approach

- **Why CV is useful before AI**: Classical CV methods (like thresholding and watershed) do not require training data. They provide immediate utility on the first captured images.
- **How CV can create pseudo-labels**: The outputs of the CV pipeline (masks, bounding boxes) can be used as initial, noisy labels to bootstrap the AI training dataset.
- **How CV can count objects**: Connected component analysis and contour detection can directly yield counts.
- **How CV can flag bad images**: Algorithms can detect low variance (blur) or extreme intensity (over/underexposed) to reject bad frames.
- **How CV and AI can cross-check each other**: Once the AI is trained, comparing the CV count to the AI count provides a valuable quality control metric. Large discrepancies flag the image for human review.

## General Pipeline

1. **Raw image**
2. -> Flat-field correction
3. -> Denoise
4. -> Contrast normalization
5. -> Thresholding
6. -> Morphological operations
7. -> Distance transform
8. -> Watershed splitting
9. -> Contour detection
10. -> Size/circularity filtering
11. -> Coordinate extraction
12. -> Mask generation
13. -> Count calculation
14. -> Pseudo-label export

## Multispectral Pipeline

1. Same field captured under multiple wavelengths
2. -> Align images
3. -> Create wavelength stack
4. -> Compute per-wavelength contrast features
5. -> Select best wavelength for segmentation
6. -> Export masks and labels

## Pseudo-Label Output

The CV pipeline generates the following outputs formatted for AI training:
- Bounding boxes (YOLO format)
- Segmentation masks
- Center coordinates
- Class guess if available (based on size/shape heuristics)
- Confidence score (based on shape clarity)
- Quality flags

## Human Review Loop

**Important**: CV labels are pseudo-labels, not ground truth.

Human review is needed for:
- Uncertain cases
- Dense regions (clumped cells)
- Artifacts (dust, bubbles)
- Disagreement between CV and AI outputs
