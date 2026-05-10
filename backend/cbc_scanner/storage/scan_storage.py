import os
import json
import secrets
from datetime import datetime
from cbc_scanner.utils.settings import get_config
from cbc_scanner.acquisition.manifest import generate_initial_manifest
import glob

def get_storage_base() -> str:
    config = get_config()
    base = config.get("settings", {}).get("storage_base_dir", "data")
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    return os.path.join(project_root, base, "scans")

def create_scan_session():
    now = datetime.utcnow()
    scan_id = f"scan_{now.strftime('%Y%m%d_%H%M%S')}_{secrets.token_hex(3)}"
    
    base_dir = get_storage_base()
    scan_dir = os.path.join(
        base_dir,
        now.strftime("%Y"),
        now.strftime("%m"),
        now.strftime("%d"),
        scan_id
    )
    
    os.makedirs(os.path.join(scan_dir, "raw"), exist_ok=True)
    os.makedirs(os.path.join(scan_dir, "thumbnails"), exist_ok=True)
    os.makedirs(os.path.join(scan_dir, "stitched"), exist_ok=True)
    os.makedirs(os.path.join(scan_dir, "metadata"), exist_ok=True)
    os.makedirs(os.path.join(scan_dir, "logs"), exist_ok=True)
    
    config = get_config()
    profile = config.get("profile", {}).get("name", "unknown")
    cam_type = config.get("scanner", {}).get("components", {}).get("camera", {}).get("type", "unknown")
    
    manifest = generate_initial_manifest(scan_id, profile, cam_type)
    
    with open(os.path.join(scan_dir, "metadata", "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
        
    return scan_id, scan_dir

def finalize_manifest(scan_id: str, updates: dict):
    # Search for scan_id in the directory tree
    manifest_path = find_manifest(scan_id)
    if manifest_path:
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
        
        manifest.update(updates)
        
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

def find_manifest(scan_id: str) -> str:
    base_dir = get_storage_base()
    # Find the scan_id directory
    for root, dirs, files in os.walk(base_dir):
        if scan_id in dirs:
            return os.path.join(root, scan_id, "metadata", "manifest.json")
    return None

def list_scans():
    base_dir = get_storage_base()
    scans = []
    for root, dirs, files in os.walk(base_dir):
        if "metadata" in dirs and "raw" in dirs:
            # Looks like a scan directory
            manifest_path = os.path.join(root, "metadata", "manifest.json")
            if os.path.exists(manifest_path):
                try:
                    with open(manifest_path, "r") as f:
                        scans.append(json.load(f))
                except Exception:
                    pass
    return sorted(scans, key=lambda x: x.get("created_at", ""), reverse=True)

def get_scan_manifest(scan_id: str):
    path = find_manifest(scan_id)
    if path and os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None

def get_image_path(scan_id: str, filename: str) -> str:
    base_dir = get_storage_base()
    for root, dirs, files in os.walk(base_dir):
        if scan_id in dirs:
            # security path traversal check
            if ".." in filename: return None
            return os.path.join(root, scan_id, "raw", filename)
    return None

def get_thumbnail_path(scan_id: str, filename: str) -> str:
    base_dir = get_storage_base()
    for root, dirs, files in os.walk(base_dir):
        if scan_id in dirs:
            # security path traversal check
            if ".." in filename: return None
            return os.path.join(root, scan_id, "thumbnails", filename)
    return None

def save_image(filepath: str, image_data):
    # Not used directly by capture_to_file but useful for array captures
    import cv2
    cv2.imwrite(filepath, image_data)
