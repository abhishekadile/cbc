#!/bin/bash
set -e

echo "Starting Pi installation for cbc-scanner..."

# 1. Be idempotent
# 2. Update apt package index
echo "Updating apt package index..."
sudo apt-get update -y

# 3, 4, 5. Install system packages for Raspberry Pi camera and image processing
echo "Installing system dependencies..."
sudo apt-get install -y python3-picamera2 python3-libcamera python3-opencv python3-numpy v4l-utils i2c-tools

# 6. Install Node.js LTS
if ! command -v node &> /dev/null; then
    echo "Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# 7. Install frontend dependencies
echo "Installing frontend dependencies..."
cd frontend
npm install

# 9. Build the frontend
echo "Building frontend..."
npm run build
cd ..

# 8. Run uv sync using system site packages
echo "Syncing python dependencies with uv..."
# Note: Since picamera2 is a system package, we need --system-site-packages.
uv venv --system-site-packages
uv sync

# 10. Create required data directories
echo "Creating data directories..."
mkdir -p data/scans
mkdir -p data/logs

echo "========================================="
echo "Installation complete!"
echo "To start the UI:"
echo "cd ~/cbc-scanner"
echo "bash scripts/run_ui.sh"
echo "========================================="
