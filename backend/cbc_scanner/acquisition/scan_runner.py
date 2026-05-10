import logging
import time
from datetime import datetime
import os
import json
from cbc_scanner.hardware.device_status import get_camera_instance
from cbc_scanner.storage.scan_storage import create_scan_session, finalize_manifest
from cbc_scanner.utils.settings import get_config

logger = logging.getLogger(__name__)

def generate_thumbnail(filepath: str, thumbpath: str):
    try:
        from PIL import Image
        img = Image.open(filepath)
        img.thumbnail((320, 240))
        img.save(thumbpath)
    except Exception as e:
        logger.error(f"Thumbnail generation failed: {e}")

def run_single_capture() -> dict:
    cam = get_camera_instance()
    scan_id, scan_dir = create_scan_session()
    
    logger.info(f"Running single capture for scan {scan_id}")
    filename = "capture_000001_white.jpg"
    filepath = os.path.join(scan_dir, "raw", filename)
    thumb_name = "capture_000001_white_thumb.jpg"
    thumbpath = os.path.join(scan_dir, "thumbnails", thumb_name)
    
    cam.capture_to_file(filepath)
    generate_thumbnail(filepath, thumbpath)
    
    status = cam.get_status()
    
    image_meta = {
        "capture_id": 1,
        "filename": filename,
        "relative_path": f"raw/{filename}",
        "thumbnail": f"thumbnails/{thumb_name}",
        "label": "white",
        "wavelength_nm": None,
        "camera_source": status.get("source", "unknown"),
        "image_simulated": status.get("simulated", True),
        "light_simulated": True,
        "url": f"/api/scans/{scan_id}/images/{filename}",
        "thumbnail_url": f"/api/scans/{scan_id}/thumbnails/{thumb_name}",
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    
    manifest_updates = {
        "images": [image_meta],
        "notes": "Single capture mode"
    }
    finalize_manifest(scan_id, manifest_updates)
    
    return {
        "scan_id": scan_id,
        "created_at": image_meta["created_at"],
        "camera_source": image_meta["camera_source"],
        "simulated": image_meta["image_simulated"],
        "images": [image_meta]
    }

def run_demo_multispectral() -> dict:
    cam = get_camera_instance()
    config = get_config()
    scan_id, scan_dir = create_scan_session()
    
    wavelengths = config.get("scanner", {}).get("channels", [
        {"id": "white", "name": "White Light", "nm": None},
        {"id": "405nm", "name": "405 nm (Violet)", "nm": 405},
        {"id": "530nm", "name": "530 nm (Green)", "nm": 530},
        {"id": "660nm", "name": "660 nm (Red)", "nm": 660},
        {"id": "850nm", "name": "850 nm (NIR)", "nm": 850}
    ])
    
    images = []
    
    logger.info(f"Running demo multispectral capture for scan {scan_id}")
    status = cam.get_status()
    created_at = datetime.utcnow().isoformat() + "Z"
    
    for i, w in enumerate(wavelengths, start=1):
        w_id = w["id"]
        logger.info(f"Simulating capture for channel: {w_id}")
        
        time.sleep(0.5) 
        
        filename = f"capture_{i:06d}_{w_id}.jpg"
        filepath = os.path.join(scan_dir, "raw", filename)
        thumb_name = f"capture_{i:06d}_{w_id}_thumb.jpg"
        thumbpath = os.path.join(scan_dir, "thumbnails", thumb_name)
        
        cam.capture_to_file(filepath)
        generate_thumbnail(filepath, thumbpath)
        
        image_meta = {
            "capture_id": i,
            "filename": filename,
            "relative_path": f"raw/{filename}",
            "thumbnail": f"thumbnails/{thumb_name}",
            "label": w_id,
            "wavelength_nm": w.get("nm"),
            "camera_source": status.get("source", "unknown"),
            "image_simulated": status.get("simulated", True),
            "light_simulated": True,
            "url": f"/api/scans/{scan_id}/images/{filename}",
            "thumbnail_url": f"/api/scans/{scan_id}/thumbnails/{thumb_name}",
            "created_at": datetime.utcnow().isoformat() + "Z"
        }
        images.append(image_meta)
        
    manifest_updates = {
        "images": images,
        "notes": "Demo multispectral mode (simulated lighting)"
    }
    finalize_manifest(scan_id, manifest_updates)
    
    return {
        "scan_id": scan_id,
        "created_at": created_at,
        "camera_source": status.get("source", "unknown"),
        "simulated": status.get("simulated", True),
        "images": images
    }
