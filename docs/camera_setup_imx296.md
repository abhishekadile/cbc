# IMX296 Camera Setup

1. Ensure the FPC cable is connected to the CSI port on the Pi.
2. In `/boot/firmware/config.txt`, add:
   `dtoverlay=imx296`
3. Reboot.
4. Run `uv run cbc-test-camera` to verify.
