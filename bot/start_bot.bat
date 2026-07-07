@echo off
cd /d "%~dp0"
if "%PYTHON%"=="" set PYTHON=python
"%PYTHON%" main.py >> "%~dp0bot.log" 2>&1
exit /b %errorlevel%
