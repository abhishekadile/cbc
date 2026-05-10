from fastapi import APIRouter
from cbc_scanner.utils.system_info import get_system_info
from cbc_scanner.utils.settings import get_config

router = APIRouter(prefix="/api", tags=["health"])

@router.get("/health")
def health_check():
    config = get_config()
    profile_name = config.get("profile", {}).get("name", "unknown")
    version = config.get("scanner", {}).get("version", "unknown")
    
    return {
        "status": "healthy",
        "version": version,
        "hardware_profile": profile_name,
        "system": get_system_info()
    }
