#!/bin/bash
set -e

REPO_DIR=$(pwd)
USER_NAME=$(whoami)
SERVICE_FILE="/etc/systemd/system/cbc-scanner.service"

echo "Creating systemd service for cbc-scanner..."

sudo bash -c "cat > $SERVICE_FILE" << EOL
[Unit]
Description=CBC Scanner Backend and UI
After=network.target

[Service]
User=$USER_NAME
WorkingDirectory=$REPO_DIR
ExecStart=$REPO_DIR/scripts/run_ui.sh
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOL

sudo systemctl daemon-reload

echo "Service created successfully!"
echo "To enable and start the service, run:"
echo "  sudo systemctl enable cbc-scanner"
echo "  sudo systemctl start cbc-scanner"
echo "  sudo systemctl status cbc-scanner"
