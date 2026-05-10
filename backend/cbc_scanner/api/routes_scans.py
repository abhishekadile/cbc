from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
import glob
from cbc_scanner.storage.scan_storage import list_scans, get_scan_manifest, get_image_path

router = APIRouter(prefix="/api/scans", tags=["scans"])

@router.get("")
@router.get("/")
def get_scans():
    scans = list_scans()
    if isinstance(scans, list):
        return scans
    return []

@router.get("/{scan_id}")
def get_scan(scan_id: str):
    manifest = get_scan_manifest(scan_id)
    if not manifest:
        raise HTTPException(status_code=404, detail="Scan not found")
    return manifest

@router.get("/{scan_id}/images/{filename}")
def get_scan_image(scan_id: str, filename: str):
    path = get_image_path(scan_id, filename)
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(path)

@router.get("/{scan_id}/thumbnails/{filename}")
def get_scan_thumbnail(scan_id: str, filename: str):
    from cbc_scanner.storage.scan_storage import get_thumbnail_path
    path = get_thumbnail_path(scan_id, filename)
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Thumbnail not found")
    return FileResponse(path)

@router.get("/{scan_id}/manifest")
def get_scan_manifest_file(scan_id: str):
    from cbc_scanner.storage.scan_storage import find_manifest
    path = find_manifest(scan_id)
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Manifest not found")
    return FileResponse(path)
