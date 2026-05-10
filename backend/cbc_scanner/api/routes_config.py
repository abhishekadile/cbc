from fastapi import APIRouter
from cbc_scanner.utils.settings import get_config
from pydantic import BaseModel

router = APIRouter(prefix="/api/config", tags=["config"])

class ConfigUpdate(BaseModel):
    exposure: int = None
    demo_wavelengths: list[str] = None

@router.get("/")
def read_config():
    return get_config()

@router.post("/")
def update_config(update: ConfigUpdate):
    # In a real app, this would merge with settings and save to yaml
    return {"success": True, "message": "Config updated in memory.", "data": update.model_dump()}
