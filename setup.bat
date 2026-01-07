@echo off
REM Setup script for Windows

echo =========================================
echo Discord DM Auto-Deleter - Setup
echo =========================================
echo.

REM Check Python version
echo [1/4] Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python not found. Please install Python 3.8 or higher.
    echo   Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo + Found Python %PYTHON_VERSION%
echo.

REM Create virtual environment
echo [2/4] Creating virtual environment...
if exist venv (
    echo ! Virtual environment already exists, skipping...
) else (
    python -m venv venv
    echo + Virtual environment created
)
echo.

REM Activate and install dependencies
echo [3/4] Installing dependencies...
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    python -m pip install --upgrade pip >nul 2>&1
    pip install -r requirements.txt
    echo + Dependencies installed
) else (
    echo X Failed to activate virtual environment
    pause
    exit /b 1
)
echo.

REM Create .env file
echo [4/4] Creating configuration file...
if exist .env (
    echo ! .env file already exists, skipping...
) else (
    copy .env.example .env >nul
    echo + Created .env file from template
)
echo.

echo =========================================
echo Setup complete!
echo =========================================
echo.
echo Next steps:
echo 1. Edit .env file and add your USER_TOKEN and CHANNEL_ID
echo 2. Run: venv\Scripts\activate.bat
echo 3. Run: python bot.py
echo.
echo For more information, read README.md
echo.
pause
