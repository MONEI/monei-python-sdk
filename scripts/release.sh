#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo '🚀 Releasing new version of MONEI PYTHON SDK'

# Ensure we're in the project root directory
cd "$(dirname "$0")/.."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/* build/*

# Install or update uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Create/update virtual environment and sync dependencies
echo "🔄 Setting up virtual environment and syncing dependencies..."
uv venv
source .venv/bin/activate

# Install project with development dependencies from pyproject.toml
echo "📦 Installing project with dependencies..."
uv pip install -e ".[dev]"

# Run tests
echo "🧪 Running tests..."
uv run pytest

# Ask for confirmation to continue if tests pass
read -p "✅ Tests passed. Continue with build and release? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Release cancelled."
    exit 0
fi

# Build the package using uv
echo "🏗️ Building package with uv..."
uv build --sdist --wheel --out-dir dist

# Ask for confirmation before uploading
read -p "📤 Upload to PyPI? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Uploading to PyPI..."
    uv publish --token "${PYPI_TOKEN:-__token__}"
    echo "✅ Release completed successfully!"
else
    echo "❌ Upload cancelled. Package is built and available in the dist/ directory."
fi
