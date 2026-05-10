#!/bin/bash
set -e

# Change to the directory of the script's parent (repo root)
cd "$(dirname "$0")/.."

echo "Starting cbc-scanner UI..."
uv run cbc-ui
