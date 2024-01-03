@echo off
echo Installing required Python modules...

:: Install colorama and psutil modules
pip install colorama psutil

:: Check if the installation was successful
if %errorlevel% equ 0 (
    echo Modules installed successfully.
) else (
    echo Error: Failed to install modules.
)

:: Pause to keep the window open
pause
