#!/bin/bash

# SG TOTO Analysis - Setup Script
# This script sets up the complete environment for the TOTO Analysis project

echo "🚀 Setting up SG TOTO Analysis Environment..."
echo "=============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✅ pip3 found: $(pip3 --version)"

# Create virtual environment (optional)
read -p "🤔 Would you like to create a virtual environment? (y/n): " create_venv
if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ Virtual environment created and activated"
fi

# Install Python dependencies
echo "📥 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed successfully"
else
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

# Check if Node.js is installed (for web app)
if command -v node &> /dev/null; then
    echo "✅ Node.js found: $(node --version)"
    
    # Check if npm is installed
    if command -v npm &> /dev/null; then
        echo "✅ npm found: $(npm --version)"
        
        # Install web app dependencies
        if [ -d "toto-web-app" ]; then
            echo "📥 Installing web app dependencies..."
            cd toto-web-app
            npm install
            
            if [ $? -eq 0 ]; then
                echo "✅ Web app dependencies installed successfully"
            else
                echo "⚠️  Warning: Failed to install web app dependencies"
            fi
            cd ..
        fi
    else
        echo "⚠️  npm not found. Web app setup skipped."
    fi
else
    echo "⚠️  Node.js not found. Web app setup skipped."
    echo "   To run the web app, install Node.js from https://nodejs.org/"
fi

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p logs
mkdir -p data
mkdir -p reports

# Set up permissions for scripts
echo "🔧 Setting up script permissions..."
chmod +x *.py

echo ""
echo "🎉 Setup completed successfully!"
echo "=============================================="
echo ""
echo "📋 Next steps:"
echo "1. Run analysis: python3 main.py"
echo "2. Start web scraping: python3 scraper.py"
echo "3. Launch web app: cd toto-web-app && npm run dev"
echo "4. Open standalone app: open TOTO-Standalone-App.html"
echo ""
echo "📚 Documentation:"
echo "- README_DOWNLOAD.md - Complete guide"
echo "- README.md - Main project documentation"
echo "- README_AUTOMATION.md - Automation setup"
echo ""
echo "🔧 For automation setup:"
echo "- python3 setup_cron.py"
echo "- python3 auto_update.py"
echo ""
echo "Happy analyzing! 🎯"