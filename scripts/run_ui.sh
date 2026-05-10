#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "Starting cbc-scanner UI..."
uv sync
uv run cbc-ui
