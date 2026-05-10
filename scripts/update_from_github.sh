#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "Pulling latest changes from GitHub..."
git pull

echo "Syncing Python dependencies..."
uv sync

echo "Rebuilding frontend..."
cd frontend
npm install
npm run build

echo "Update complete."
