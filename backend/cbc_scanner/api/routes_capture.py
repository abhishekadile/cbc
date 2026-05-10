from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/capture", tags=["capture"])

class CaptureResponse(BaseModel):
    success: bool
    message: str
    scan_id: str = None

@router.post("/single")
def capture_single(background_tasks: BackgroundTasks):
    from cbc_scanner.acquisition.scan_runner import run_single_capture
    return run_single_capture()

@router.post("/demo-multispectral")
def capture_demo_multispectral(background_tasks: BackgroundTasks):
    from cbc_scanner.acquisition.scan_runner import run_demo_multispectral
    return run_demo_multispectral()
