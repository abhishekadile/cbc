import yaml
import os
import logging
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)

class AppSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    environment: str = "development"
    camera_mock: bool = False
    storage_base_dir: str = "data"

    class Config:
        env_file = ".env"

settings = AppSettings()
global_config = {}

def load_config():
    global global_config
    config_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "config")
    
    scanner_conf = os.path.join(config_dir, "scanner.yaml")
    if os.path.exists(scanner_conf):
        with open(scanner_conf, "r") as f:
            global_config["scanner"] = yaml.safe_load(f)
            
    # Load default profile
    profile = global_config.get("scanner", {}).get("default_profile", "demo_pi_only")
    profile_path = os.path.join(config_dir, "hardware_profiles", f"{profile}.yaml")
    if os.path.exists(profile_path):
         with open(profile_path, "r") as f:
            global_config["profile"] = yaml.safe_load(f)
            
    logger.info(f"Loaded configuration for profile: {profile}")
    return global_config

def get_config():
    if not global_config:
        load_config()
    return global_config
