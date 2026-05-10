import logging
import time
from datetime import datetime
import os
from cbc_scanner.hardware.device_status import get_camera_instance
from cbc_scanner.storage.scan_storage import create_scan_session, save_image, finalize_manifest
from cbc_scanner.utils.settings import get_config

logger = logging.getLogger(__name__)

def run_single_capture() -> str:
    cam = get_camera_instance()
    scan_id, scan_dir = create_scan_session()
    
    logger.info(f"Running single capture for scan {scan_id}")
    filename = "capture_000001_white.png"
    filepath = os.path.join(scan_dir, "raw", filename)
    
    cam.capture_to_file(filepath)
    
    manifest_updates = {
        "images": [filename],
        "wavelengths": ["white"],
        "notes": "Single capture mode"
    }
    finalize_manifest(scan_id, manifest_updates)
    
    return scan_id

def run_demo_multispectral() -> str:
    cam = get_camera_instance()
    config = get_config()
    scan_id, scan_dir = create_scan_session()
    
    wavelengths = config.get("scanner", {}).get("channels", [
        {"id": "white", "name": "White Light"},
        {"id": "405nm", "name": "405 nm (Violet)"},
        {"id": "530nm", "name": "530 nm (Green)"},
        {"id": "660nm", "name": "660 nm (Red)"},
        {"id": "850nm", "name": "850 nm (NIR)"}
    ])
    
    images = []
    w_ids = []
    
    logger.info(f"Running demo multispectral capture for scan {scan_id}")
    
    for i, w in enumerate(wavelengths, start=1):
        w_id = w["id"]
        logger.info(f"Simulating capture for channel: {w_id}")
        
        # Simulate wavelength change time
        time.sleep(0.5) 
        
        filename = f"capture_{i:06d}_{w_id}.png"
        filepath = os.path.join(scan_dir, "raw", filename)
        
        # Real camera is triggered, but since no real multispectral LEDs exist,
        # it just captures what it sees.
        cam.capture_to_file(filepath)
        
        images.append(filename)
        w_ids.append(w_id)
        
    manifest_updates = {
        "images": images,
        "wavelengths": w_ids,
        "notes": "Demo multispectral mode (simulated lighting)"
    }
    finalize_manifest(scan_id, manifest_updates)
    
    return scan_id
