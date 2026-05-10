import uvicorn
from cbc_scanner.utils.settings import get_config

def run_ui():
    config = get_config()
    host = config.get("settings", {}).get("host", "0.0.0.0")
    port = config.get("settings", {}).get("port", 8000)
    uvicorn.run("cbc_scanner.main:app", host=host, port=port, reload=True)
