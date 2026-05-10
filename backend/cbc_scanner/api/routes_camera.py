from fastapi import APIRouter
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/camera", tags=["camera"])

class CameraTestResponse(BaseModel):
    success: bool
    message: str

@router.post("/test", response_model=CameraTestResponse)
def test_camera():
    from cbc_scanner.hardware.device_status import get_camera_instance
    cam = get_camera_instance()
    success = cam.test()
    if success:
        return {"success": True, "message": "Camera test passed."}
    return {"success": False, "message": "Camera test failed."}
