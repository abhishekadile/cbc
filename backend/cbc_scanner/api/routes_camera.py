from fastapi import APIRouter
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/camera", tags=["camera"])

@router.post("/test")
def test_camera() -> Dict[str, Any]:
    from cbc_scanner.hardware.device_status import get_camera_instance
    cam = get_camera_instance()
    success = cam.test()
    status = cam.get_status()
    
    if success:
        return {
            "ok": True,
            "camera": status
        }
    else:
        return {
            "ok": False,
            "error": status.get("last_error", "Unknown error"),
            "camera": status
        }
