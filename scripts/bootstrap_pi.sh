#!/bin/bash
set -e

echo "Starting cbc-scanner bootstrap..."

# 1. Check OS and architecture
if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "OS: $PRETTY_NAME"
else
    echo "Warning: /etc/os-release not found."
fi

# 2 & 3. Install git and curl if needed
if ! command -v git &> /dev/null || ! command -v curl &> /dev/null; then
    echo "Installing git and curl..."
    sudo apt-get update
    sudo apt-get install -y git curl
fi

# 4. Install uv if missing
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

# 5 & 6. Clone or update repository
REPO_DIR="$HOME/cbc-scanner"
if [ -d "$REPO_DIR" ]; then
    echo "Repository already exists at $REPO_DIR. Pulling latest..."
    cd "$REPO_DIR"
    git pull
else
    echo "Cloning repository into $REPO_DIR..."
    git clone https://github.com/abhishekadile/cbc.git "$REPO_DIR"
    cd "$REPO_DIR"
fi

# 7. Run install_pi.sh
echo "Running install_pi.sh..."
bash scripts/install_pi.sh

# 8. Print next steps
echo "========================================="
echo "Bootstrap complete!"
echo "To start the UI, run:"
echo "cd ~/cbc-scanner"
echo "bash scripts/run_ui.sh"
echo "========================================="
