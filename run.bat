@echo off
REM One-click launcher for the Appointza certificate generator (Windows).
setlocal

cd /d "%~dp0"

if not exist ".venv" (
  echo Creating virtual environment...
  py -m venv .venv
)

call ".venv\Scripts\activate.bat"

echo Installing dependencies...
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

echo.
echo Starting the app at http://127.0.0.1:5000
echo Press Ctrl+C to stop.
echo.
python app.py
