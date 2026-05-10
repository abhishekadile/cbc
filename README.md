# Multispectral CBC Image Acquisition System

This is a complete full-stack embedded systems project for capturing multispectral CBC (Complete Blood Count) imagery using a Raspberry Pi and an InnovaMaker IMX296 global shutter camera. 

> **Disclaimer:** This is a prototype/research image acquisition system. It does not provide medical diagnosis and is not for clinical use. An AI analysis module is planned for future versions.

## 🚀 Features
- **Hardware Integration**: Controls InnovaMaker IMX296 MIPI global shutter camera.
- **Data Management**: Robust directory structure for scan sessions ensuring no lost data.
- **User Interface**: Modern React/Vite-based investor demo dashboard.
- **Extensibility**: Hardware Abstraction Layers (HAL) for future microcontrollers, XY stages, Z focus actuators, and multispectral LED channels.

## 📦 Supported Hardware
- **Current**: Raspberry Pi + InnovaMaker IMX296 MIPI camera
- **Planned**: XY Stage, Z Focus Actuator, Multispectral LED Channels, RP2040/STM32 timing controller

---

## 🛠️ Step-by-Step Setup Guide for Raspberry Pi

Follow these exact steps to set up the software on a fresh Raspberry Pi.

### 1. Initial Raspberry Pi Configuration
1. Flash standard **Raspberry Pi OS (64-bit)** to an SD card using the Raspberry Pi Imager.
2. Boot the Pi, connect it to your local Wi-Fi, and enable SSH.
3. Connect the InnovaMaker IMX296 FPC cable to the CSI port on the Raspberry Pi.
4. Open the boot configuration file to enable the camera overlay:
   ```bash
   sudo nano /boot/firmware/config.txt
   ```
5. Add the following line at the end of the file:
   ```text
   dtoverlay=imx296
   ```
6. Save (`Ctrl+O`, `Enter`) and exit (`Ctrl+X`), then reboot:
   ```bash
   sudo reboot
   ```

### 2. Verify Hardware with Libcamera
After rebooting, test that the system recognizes the camera and the driver is loaded using the standard Raspberry Pi tools:
```bash
rpicam-hello -t 5000
rpicam-still -o test.jpg
```

### 2. Software Installation
Once the Pi has rebooted, open a terminal (or SSH into it) and run the one-line bootstrap script. This script will install Git, curl, uv (Python dependency manager), clone this repository, and install all required system and frontend dependencies.

```bash
curl -fsSL https://raw.githubusercontent.com/abhishekadile/cbc/main/scripts/bootstrap_pi.sh | bash
```

Alternatively, you can install manually:
```bash
git clone https://github.com/abhishekadile/cbc.git ~/cbc-scanner
cd ~/cbc-scanner
bash scripts/install_pi.sh
```

---

## 💻 Running the Application

### Starting the Main Interface (UI + Backend)
To run the full stack (FastAPI backend + Vite React frontend) locally on the Pi:
```bash
cd ~/cbc-scanner
bash scripts/run_ui.sh
```
Once running, open a web browser on your laptop or Pi and navigate to:
**`http://localhost:8000`** (or use the Pi's actual IP address).

### Testing the REST API
You can verify the backend is running properly via the terminal:
```bash
curl http://localhost:8000/api/devices/status
curl -X POST http://localhost:8000/api/camera/test
curl -X POST http://localhost:8000/api/capture/single
curl http://localhost:8000/api/scans
```

### Running as a Background Service (Auto-start on Boot)
If you want the software to run automatically every time the Pi turns on:
```bash
cd ~/cbc-scanner
bash scripts/create_systemd_service.sh
sudo systemctl enable cbc-scanner
sudo systemctl start cbc-scanner
```

---

## 🔬 Command Line Utilities

We provide several command-line tools for debugging and manual control. All commands should be run from the `~/cbc-scanner` directory using `uv run`.

**1. Test Camera Connection**
Verifies that the IMX296 camera is properly detected and can be communicated with via Picamera2.
```bash
cd ~/cbc-scanner
uv run cbc-test-camera
```

**2. Capture a Single Image**
Captures exactly one image and saves it in a new scan session.
```bash
cd ~/cbc-scanner
uv run cbc-capture
```

**3. Run a Demo Multispectral Scan**
Simulates a full multispectral acquisition loop. It captures frames representing 5 wavelengths (White, 405nm, 530nm, 660nm, 850nm). *Note: until the LED board is connected, these use the ambient lighting.*
```bash
cd ~/cbc-scanner
uv run cbc-demo-scan
```

**4. Check Storage Info**
Displays the local storage base directory and a table of recently acquired scans.
```bash
cd ~/cbc-scanner
uv run cbc-storage-info
```

---

## 🔄 Updating the Software
To pull the latest changes from this GitHub repository and rebuild the environment:
```bash
cd ~/cbc-scanner
bash scripts/update_from_github.sh
```

---

## 📂 Data Storage Format
Images and scan metadata are never overwritten. They are stored chronologically in:
`data/scans/YYYY/MM/DD/scan_YYYYMMDD_HHMMSS_ID/`

Each scan directory contains:
- `raw/`: Raw, unprocessed `.png` image captures.
- `thumbnails/`: Downsampled images for the UI dashboard.
- `stitched/`: Future location for multi-grid panoramas.
- `metadata/manifest.json`: Device status, time, hardware profile, and exposure data.
- `logs/`: Diagnostic logs specific to the scan.
