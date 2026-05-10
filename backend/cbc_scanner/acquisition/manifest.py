import json
import os
from datetime import datetime

def generate_initial_manifest(scan_id: str, profile_name: str, camera_model: str) -> dict:
    from cbc_scanner.hardware.device_status import get_all_device_statuses, get_camera_instance
    from cbc_scanner.utils.settings import get_config
    
    config = get_config()
    cam_config = config.get("scanner", {}).get("camera", {})
    hardware = get_all_device_statuses()
    cam_status = hardware.get("camera", {})
    
    return {
        "scan_id": scan_id,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "app_version": "0.1.0",
        "camera": {
            "model": cam_status.get("model", camera_model),
            "source": cam_status.get("source", "unknown"),
            "simulated": cam_status.get("simulated", True),
            "resolution": cam_config.get("resolution", [1456, 1088]),
            "exposure_us": cam_config.get("exposure_us", 5000),
            "gain": cam_config.get("gain", 1.0)
        },
        "hardware": {
            "xy_stage": hardware.get("xy_stage"),
            "lights": hardware.get("lights")
        },
        "images": []
    }
