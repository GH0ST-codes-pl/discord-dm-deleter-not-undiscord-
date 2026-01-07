#!/bin/bash
# Setup script for Linux/macOS/Termux

echo "========================================="
echo "Discord DM Auto-Deleter - Setup"
echo "========================================="
echo ""

# Check Python version
echo "[1/4] Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✓ Found Python $PYTHON_VERSION"
echo ""

# Create virtual environment
echo "[2/4] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠ Virtual environment already exists, skipping..."
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi
echo ""

# Activate and install dependencies
echo "[3/4] Installing dependencies..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    pip install --upgrade pip > /dev/null 2>&1
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
else
    echo "❌ Failed to activate virtual environment"
    exit 1
fi
echo ""

# Create .env file
echo "[4/4] Creating configuration file..."
if [ -f ".env" ]; then
    echo "⚠ .env file already exists, skipping..."
else
    cp .env.example .env
    echo "✓ Created .env file from template"
fi
echo ""

echo "========================================="
echo "✅ Setup complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your USER_TOKEN and CHANNEL_ID"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python bot.py"
echo ""
echo "For more information, read README.md"
