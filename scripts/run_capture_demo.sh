#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "Running demo multispectral capture..."
uv run cbc-demo-scan
