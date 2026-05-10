# Computer Vision System

This document describes the classical Computer Vision (CV) algorithms used for initial object detection, quality control, and pseudo-label generation. These algorithms provide immediate utility without requiring labeled training data.

## Recommended Packages
- `OpenCV` (`cv2`)
- `scikit-image` (`skimage`)
- `NumPy`, `SciPy`, `pandas`
- `tifffile` / `imageio` (for handling multi-page TIFFs or multispectral stacks)
- `napari` or `FiftyOne` / `CVAT` / `Label Studio` (for visual review of CV outputs)

## Concrete Pipeline Algorithms

### 1. Preprocessing & Enhancement
- **Flat-field correction**: Corrects for uneven illumination (vignetting) caused by the LED/diffuser setup. `Corrected = (Raw - DarkFrame) / (FlatField - DarkFrame)`.
- **Dark-frame subtraction**: Removes fixed-pattern sensor noise.
- **Filtering**: Apply Gaussian, Median, or Bilateral filtering to reduce noise while preserving edges.
- **Contrast Enhancement**: Use CLAHE (Contrast Limited Adaptive Histogram Equalization) to normalize contrast across different imaging sessions.

### 2. Segmentation & Detection
- **Thresholding**: Otsu's method for global thresholding, or Adaptive Thresholding for images with varying background illumination.
- **Edge Detection**: Canny edge detection (useful for finding sharp boundaries of cells).
- **Morphological Operations**: Opening (removes small noise) and Closing (fills small holes inside cells).
- **Instance Separation**: 
    - Compute the **Distance Transform**.
    - Apply **Watershed Segmentation** using local maxima as markers to split clumped cells.
- **Feature Extraction**:
    - **Connected Components** / **Contour Detection**.
    - **Blob Detection** (Laplacian of Gaussian - LoG).
    - *Optional Baseline*: Hough circles (only useful for perfectly spherical, non-clumped RBCs).

### 3. Filtering & Quality Control
- **Shape Filtering**: Filter detected contours based on Area, Perimeter, Circularity, Eccentricity, and Aspect Ratio to reject artifacts (dust, scratches).
- **Focus Metric**: Calculate the Variance of the Laplacian. Images falling below a certain threshold are rejected as "blurry".
- **Brightness/Saturation Checks**: Reject images that are entirely black (LED failed) or entirely white (overexposed).

## Multispectral Processing Strategy
1. **Capture**: The hardware captures the same FOV under different LED wavelengths.
2. **Registration**: Align the channels to correct for micro-vibrations between captures. Use Phase Correlation for translations, or ECC (Enhanced Correlation Coefficient) alignment.
3. **Stacking**: Create a multi-channel NumPy array.
4. **Feature Engineering**: Compute wavelength contrast ratios (e.g., `(Ch1 - Ch2) / (Ch1 + Ch2)`) to highlight specific cell structures that absorb specific wavelengths.
5. **Selection**: Choose the best wavelength (or computed ratio) to run the segmentation pipeline on for specific object types.

## Pseudo-Labeling Export
The CV pipeline acts as the first "annotator". It exports:
- Bounding boxes in **YOLO format**.
- Polygons in **COCO format**.
- Binary **Segmentation Masks**.
- **CSV** with center coordinates and calculated shape metrics.
- **Confidence/Quality flags**: E.g., "High Confidence" if the object is perfectly circular and isolated; "Low Confidence" if it was split by the watershed algorithm.

**Human Review Queue**: Low-confidence CV predictions are pushed to Label Studio/CVAT for human correction before being fed into the AI training loop.
