import logging
import time
from .base import BaseCamera
from cbc_scanner.utils.settings import get_config

logger = logging.getLogger(__name__)

class IMX296PiCamera2(BaseCamera):
    def __init__(self):
        self.picam2 = None
        self.started = False
        self.last_error = None
        
        config = get_config().get("scanner", {}).get("camera", {})
        res = config.get("resolution", [1456, 1088])
        self.resolution = tuple(res)
        self.exposure_us = config.get("exposure_us", 5000)
        self.gain = config.get("gain", 1.0)
        
    def start(self):
        try:
            from picamera2 import Picamera2
            self.picam2 = Picamera2()
            config = self.picam2.create_still_configuration(
                main={"size": self.resolution}
            )
            self.picam2.configure(config)
            self.picam2.start()
            time.sleep(1.0) # Warmup time
            self.picam2.set_controls({
                "ExposureTime": int(self.exposure_us),
                "AnalogueGain": float(self.gain)
            })
            self.started = True
            self.last_error = None
            logger.info("IMX296 camera started successfully via Picamera2")
        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to start Picamera2: {e}")
            self.started = False

    def stop(self):
        if self.picam2:
            self.picam2.stop()
            self.started = False

    def test(self) -> bool:
        if not self.picam2:
            self.start()
        return self.started

    def capture_array(self):
        if not self.started:
            self.start()
            if not self.started:
                raise RuntimeError(f"Camera not connected. Last error: {self.last_error}")
        return self.picam2.capture_array()

    def capture_to_file(self, filepath: str):
        if not self.started:
            self.start()
            if not self.started:
                raise RuntimeError(f"Camera not connected. Last error: {self.last_error}")
                
        arr = self.capture_array()
        from PIL import Image
        img = Image.fromarray(arr)
        img.save(filepath)
        return filepath

    def get_status(self) -> dict:
        return {
            "model": "IMX296 MIPI",
            "source": "picamera2",
            "connected": self.started,
            "simulated": False,
            "last_error": self.last_error
        }

    def set_controls(self, controls: dict):
        if self.picam2:
            self.picam2.set_controls(controls)
