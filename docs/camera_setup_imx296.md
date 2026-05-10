# IMX296 Camera Setup

1. Ensure the FPC cable is connected to the CSI port on the Pi.
2. In `/boot/firmware/config.txt`, add:
   `dtoverlay=imx296`
3. Reboot.

## Testing the Hardware

Run the standard Raspberry Pi camera tools to ensure the driver is loaded properly:
```bash
rpicam-hello -t 5000
rpicam-still -o test.jpg
```

## Running the Application

Update the repository and start the server:
```bash
cd ~/cbc-scanner
git pull origin main
bash scripts/install_pi.sh
bash scripts/run_ui.sh
```

Then open the browser: `http://localhost:8000`

## API Testing

You can also test the integration directly via the REST API:
```bash
curl http://localhost:8000/api/devices/status
curl -X POST http://localhost:8000/api/camera/test
curl -X POST http://localhost:8000/api/capture/single
curl http://localhost:8000/api/scans
```
