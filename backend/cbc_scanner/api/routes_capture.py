from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/capture", tags=["capture"])

class CaptureResponse(BaseModel):
    success: bool
    message: str
    scan_id: str = None

@router.post("/single", response_model=CaptureResponse)
def capture_single(background_tasks: BackgroundTasks):
    from cbc_scanner.acquisition.scan_runner import run_single_capture
    scan_id = run_single_capture()
    return {"success": True, "message": "Capture initiated.", "scan_id": scan_id}

@router.post("/demo-multispectral", response_model=CaptureResponse)
def capture_demo_multispectral(background_tasks: BackgroundTasks):
    from cbc_scanner.acquisition.scan_runner import run_demo_multispectral
    scan_id = run_demo_multispectral()
    return {"success": True, "message": "Demo multispectral capture initiated.", "scan_id": scan_id}
