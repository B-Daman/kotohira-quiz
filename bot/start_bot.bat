@echo off
cd /d "%~dp0"
if "%PYTHON%"=="" set PYTHON=python
"%PYTHON%" main.py
