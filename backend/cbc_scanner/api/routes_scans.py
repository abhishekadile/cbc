from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
import glob
from cbc_scanner.storage.scan_storage import list_scans, get_scan_manifest, get_image_path

router = APIRouter(prefix="/api/scans", tags=["scans"])

@router.get("/")
def get_scans():
    return list_scans()

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
