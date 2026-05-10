#!/bin/bash
set -e

echo "Starting cbc-scanner bootstrap..."

# 1. Check OS and architecture
if [ -f /etc/os-release ]; then
    # shellcheck disable=SC1091
    . /etc/os-release
    echo "OS: $PRETTY_NAME"
else
    echo "Warning: /etc/os-release not found."
fi

# 2 & 3. Install git and curl if needed
if ! command -v git >/dev/null 2>&1 || ! command -v curl >/dev/null 2>&1; then
    echo "Installing git and curl..."
    sudo apt-get update
    sudo apt-get install -y git curl
fi

ensure_uv_on_path() {
    if [ -f "$HOME/.local/bin/env" ]; then
        # shellcheck disable=SC1091
        source "$HOME/.local/bin/env"
    elif [ -f "$HOME/.cargo/env" ]; then
        # shellcheck disable=SC1091
        source "$HOME/.cargo/env"
    else
        export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
    fi

    if ! command -v uv >/dev/null 2>&1; then
        echo "ERROR: uv was installed but is not available on PATH."
        echo "Expected uv in one of:"
        echo "  $HOME/.local/bin/uv"
        echo "  $HOME/.cargo/bin/uv"
        echo "Try running:"
        echo "  export PATH=\"\$HOME/.local/bin:\$HOME/.cargo/bin:\$PATH\""
        exit 1
    fi
}

# 4. Install uv if missing
if ! command -v uv >/dev/null 2>&1; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ensure_uv_on_path
else
    echo "uv already installed: $(uv --version)"
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

# Make sure uv is on path right before running the install script in case this shell needs it
ensure_uv_on_path

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
