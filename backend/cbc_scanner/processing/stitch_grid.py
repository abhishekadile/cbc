import cv2
import numpy as np

def simple_stitch_grid(images: list[np.ndarray], grid_shape: tuple[int, int]) -> np.ndarray:
    """
    Very simple deterministic grid stitching. 
    Assumes images are in row-major order and perfectly aligned (simulated).
    """
    rows, cols = grid_shape
    if len(images) != rows * cols:
        raise ValueError("Number of images does not match grid shape")
        
    grid_rows = []
    idx = 0
    for r in range(rows):
        row_images = images[idx:idx+cols]
        grid_rows.append(np.hstack(row_images))
        idx += cols
        
    return np.vstack(grid_rows)
