import json
import os
from datetime import datetime

def generate_initial_manifest(scan_id: str, profile_name: str, camera_model: str) -> dict:
    return {
        "scan_id": scan_id,
        "created_at": datetime.utcnow().isoformat(),
        "app_version": "0.1.0",
        "hardware_profile": profile_name,
        "camera_model": camera_model,
        "images": [],
        "wavelengths": [],
        "exposure_settings": {},
        "notes": ""
    }
