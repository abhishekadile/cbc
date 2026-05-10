import logging
import numpy as np
from .base import BaseCamera

logger = logging.getLogger(__name__)

class IMX296PiCamera2(BaseCamera):
    def __init__(self):
        self.picam2 = None
        self.is_connected = False
        
    def start(self):
        try:
            from picamera2 import Picamera2
            self.picam2 = Picamera2()
            self.picam2.configure("main", size=(1440, 1080), format="RGB888")
            self.picam2.start()
            self.is_connected = True
            logger.info("IMX296 camera started successfully via Picamera2")
        except Exception as e:
            logger.error(f"Failed to start Picamera2: {e}")
            self.is_connected = False

    def stop(self):
        if self.picam2:
            self.picam2.stop()
            self.is_connected = False

    def test(self) -> bool:
        if not self.picam2:
            self.start()
        return self.is_connected

    def capture_array(self):
        if not self.is_connected:
            raise RuntimeError("Camera not connected")
        return self.picam2.capture_array("main")

    def capture_to_file(self, filepath: str):
        if not self.is_connected:
            raise RuntimeError("Camera not connected")
        self.picam2.capture_file(filepath)

    def get_status(self) -> dict:
        return {
            "type": "IMX296",
            "connected": self.is_connected,
            "simulated": False
        }

    def set_controls(self, controls: dict):
        if self.picam2:
            self.picam2.set_controls(controls)
