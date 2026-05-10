import logging
import numpy as np
import cv2
from .base import BaseCamera

logger = logging.getLogger(__name__)

class MockCamera(BaseCamera):
    def __init__(self):
        self.is_connected = False
        self.width = 1440
        self.height = 1080

    def start(self):
        self.is_connected = True
        logger.info("Mock camera started.")

    def stop(self):
        self.is_connected = False

    def test(self) -> bool:
        return True

    def capture_array(self):
        if not self.is_connected:
            raise RuntimeError("Camera not connected")
        # Generate a synthetic image (e.g. noise + some circles simulating cells)
        img = np.random.randint(50, 100, (self.height, self.width, 3), dtype=np.uint8)
        for _ in range(50):
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            r = np.random.randint(10, 30)
            cv2.circle(img, (x, y), r, (150, 50, 50), -1)
        return img

    def capture_to_file(self, filepath: str):
        img = self.capture_array()
        cv2.imwrite(filepath, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

    def get_status(self) -> dict:
        return {
            "model": "Mock Camera",
            "source": "mock",
            "connected": self.is_connected,
            "simulated": True
        }

    def set_controls(self, controls: dict):
        logger.info(f"Mock camera controls set: {controls}")
