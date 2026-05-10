from cbc_scanner.utils.settings import get_config
from cbc_scanner.camera.imx296_picamera2 import IMX296PiCamera2
from cbc_scanner.camera.mock_camera import MockCamera
import logging

logger = logging.getLogger(__name__)

_camera_instance = None

def get_camera_instance():
    global _camera_instance
    if _camera_instance:
        return _camera_instance

    config = get_config()
    cam_config = config.get("scanner", {}).get("camera", {})
    mode = cam_config.get("mode", "auto")
    allow_mock = cam_config.get("mock_fallback", True)
    
    if mode == "mock":
        logger.info("Camera mode set to 'mock'. Using MockCamera.")
        _camera_instance = MockCamera()
        _camera_instance.start()
        return _camera_instance
        
    _camera_instance = IMX296PiCamera2()
    _camera_instance.start()
    
    if not _camera_instance.started:
        if allow_mock and mode == "auto":
            logger.warning("Falling back to MockCamera")
            _camera_instance = MockCamera()
            _camera_instance.start()
        else:
            logger.error("Failed to start IMX296PiCamera2 and mock fallback is disabled/not applicable.")
            
    return _camera_instance

def get_all_device_statuses():
    cam = get_camera_instance()
    
    # Placeholder statuses for simulated/mock hardware
    return {
        "camera": cam.get_status(),
        "xy_stage": {"connected": True, "simulated": True, "position": {"x": 0, "y": 0}},
        "z_focus": {"connected": True, "simulated": True, "position": 0},
        "lights": {"connected": True, "simulated": True, "active_channel": "white"},
        "storage": {"connected": True, "simulated": False, "free_space_gb": 10.5},
        "network": {"connected": True, "simulated": False, "mode": "local"}
    }
