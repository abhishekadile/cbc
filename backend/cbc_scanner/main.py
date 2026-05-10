import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from cbc_scanner.api import routes_health, routes_camera, routes_capture, routes_scans, routes_devices, routes_config

logger = logging.getLogger(__name__)

app = FastAPI(title="CBC Scanner API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_health.router)
app.include_router(routes_camera.router)
app.include_router(routes_capture.router)
app.include_router(routes_scans.router)
app.include_router(routes_devices.router)
app.include_router(routes_config.router)

# Serve frontend static files if they exist
frontend_path = os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "dist")
if os.path.isdir(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
else:
    logger.warning(f"Frontend dist not found at {frontend_path}. UI will not be served.")

@app.on_event("startup")
async def startup_event():
    logger.info("CBC Scanner API starting up...")
    # Initialization logic for hardware profiles and cameras would go here
    from cbc_scanner.utils.settings import load_config
    load_config()
