#!/bin/bash

echo "Uninstalling cbc-scanner systemd service..."

sudo systemctl stop cbc-scanner || true
sudo systemctl disable cbc-scanner || true
sudo rm -f /etc/systemd/system/cbc-scanner.service
sudo systemctl daemon-reload

echo "Service uninstalled."
