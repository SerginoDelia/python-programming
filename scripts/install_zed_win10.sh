#!/bin/bash

# win-10-zed-install.sh
# make it executeable: chmod +x install_zed_win11.sh
# run it: ./install_zed_win10.sh
# Script to install Zed Editor on Windows 10

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Zed installation for Windows 10...${NC}"

# Create temporary directory
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

# Download Zed installer
echo "Downloading Zed installer..."
curl -L -o ZedSetup.exe "https://zed.dev/download/windows"

if [ $? -ne 0 ]; then
    echo -e "${RED}Failed to download Zed installer${NC}"
    exit 1
fi

# Make the installer executable
chmod +x ZedSetup.exe

# Check if running in WSL
if grep -q Microsoft /proc/version; then
    echo "Running in WSL environment"
    # Get Windows username
    WIN_USER=$(cmd.exe /c "echo %USERNAME%" 2>/dev/null | tr -d '\r')
    
    # Convert the path to Windows format
    WIN_PATH=$(wslpath -w "$TEMP_DIR/ZedSetup.exe")
    
    echo "Starting installation..."
    # Run the installer using cmd.exe
    cmd.exe /c "start $WIN_PATH"
    
    echo -e "${GREEN}Installation started! Please follow the on-screen instructions in the Windows installer.${NC}"
else
    echo -e "${RED}This script must be run in Windows Subsystem for Linux (WSL)${NC}"
    exit 1
fi

# Cleanup
echo "Cleaning up temporary files..."
cd ..
rm -rf "$TEMP_DIR"

echo -e "${GREEN}Script completed!${NC}"
echo "Note: Please complete the installation in the Windows installer window that opened."
