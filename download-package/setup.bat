@echo off
REM SG TOTO Analysis - Windows Setup Script
REM This script sets up the complete environment for the TOTO Analysis project

echo 🚀 Setting up SG TOTO Analysis Environment...
echo ==============================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python found:
python --version

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip is not installed. Please install pip.
    pause
    exit /b 1
)

echo ✅ pip found:
pip --version

REM Create virtual environment (optional)
set /p create_venv="🤔 Would you like to create a virtual environment? (y/n): "
if /i "%create_venv%"=="y" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment created and activated
)

REM Install Python dependencies
echo 📥 Installing Python dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install Python dependencies
    pause
    exit /b 1
) else (
    echo ✅ Python dependencies installed successfully
)

REM Check if Node.js is installed (for web app)
node --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Node.js not found. Web app setup skipped.
    echo    To run the web app, install Node.js from https://nodejs.org/
) else (
    echo ✅ Node.js found:
    node --version
    
    REM Check if npm is installed
    npm --version >nul 2>&1
    if errorlevel 1 (
        echo ⚠️  npm not found. Web app setup skipped.
    ) else (
        echo ✅ npm found:
        npm --version
        
        REM Install web app dependencies
        if exist "toto-web-app" (
            echo 📥 Installing web app dependencies...
            cd toto-web-app
            npm install
            
            if errorlevel 1 (
                echo ⚠️  Warning: Failed to install web app dependencies
            ) else (
                echo ✅ Web app dependencies installed successfully
            )
            cd ..
        )
    )
)

REM Create necessary directories
echo 📁 Creating necessary directories...
if not exist "logs" mkdir logs
if not exist "data" mkdir data
if not exist "reports" mkdir reports

echo.
echo 🎉 Setup completed successfully!
echo ==============================================
echo.
echo 📋 Next steps:
echo 1. Run analysis: python main.py
echo 2. Start web scraping: python scraper.py
echo 3. Launch web app: cd toto-web-app ^&^& npm run dev
echo 4. Open standalone app: TOTO-Standalone-App.html
echo.
echo 📚 Documentation:
echo - README_DOWNLOAD.md - Complete guide
echo - README.md - Main project documentation
echo - README_AUTOMATION.md - Automation setup
echo.
echo 🔧 For automation setup:
echo - python setup_cron.py
echo - python auto_update.py
echo.
echo Happy analyzing! 🎯
pause