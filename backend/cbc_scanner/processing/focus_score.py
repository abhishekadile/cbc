import cv2
import numpy as np

def focus_score(image: np.ndarray) -> float:
    # Basic Laplacian variance focus measure
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    return cv2.Laplacian(gray, cv2.CV_64F).var()
