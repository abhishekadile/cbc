from fastapi import APIRouter
from cbc_scanner.hardware.device_status import get_all_device_statuses

router = APIRouter(prefix="/api/devices", tags=["devices"])

@router.get("/status")
def get_device_status():
    return get_all_device_statuses()
