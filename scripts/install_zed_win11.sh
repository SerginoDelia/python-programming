#!/bin/bash

# install_zed_win11.sh
# make it executeable: chmod +x install_zed_win11.sh
# run it: ./install_zed_win11.sh
# Script to install Zed Editor on Windows 11

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to check Windows version
check_windows_version() {
    local version=$(cmd.exe /c "ver" 2>/dev/null)
    if [[ $version == *"Version 10"* ]] && [[ $version == *"22"* ]]; then
        return 0 # Windows 11
    else
        return 1 # Not Windows 11
    fi
}

# Function to check WSL version
check_wsl_version() {
    if [ -f /proc/version ]; then
        if grep -q "microsoft" /proc/version || grep -q "WSL" /proc/version; then
            return 0 # WSL detected
        fi
    fi
    return 1 # WSL not detected
}

# Main installation function
install_zed() {
    echo -e "${GREEN}Starting Zed installation for Windows 11...${NC}"

    # Create temporary directory
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"

    # Check if curl is installed
    if ! command -v curl &> /dev/null; then
        echo -e "${YELLOW}curl is not installed. Installing curl...${NC}"
        sudo apt update && sudo apt install -y curl
    fi

    # Download Zed installer
    echo "Downloading Zed installer..."
    curl -L -o ZedSetup.exe "https://zed.dev/download/windows" --progress-bar

    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to download Zed installer${NC}"
        cleanup
        exit 1
    fi

    # Make the installer executable
    chmod +x ZedSetup.exe

    # Get Windows username
    WIN_USER=$(cmd.exe /c "echo %USERNAME%" 2>/dev/null | tr -d '\r')
    
    # Convert the path to Windows format
    WIN_PATH=$(wslpath -w "$TEMP_DIR/ZedSetup.exe")
    
    echo "Starting installation..."
    # Run the installer using PowerShell for better Windows 11 compatibility
    powershell.exe -Command "Start-Process '$WIN_PATH' -Wait"
    
    echo -e "${GREEN}Installation started! Please follow the on-screen instructions in the Windows installer.${NC}"

    # Cleanup
    cleanup
}

# Cleanup function
cleanup() {
    echo "Cleaning up temporary files..."
    cd ..
    rm -rf "$TEMP_DIR"
}

# Main script execution
main() {
    # Check if running in WSL
    if ! check_wsl_version; then
        echo -e "${RED}This script must be run in Windows Subsystem for Linux (WSL)${NC}"
        exit 1
    fi

    # Check Windows version
    if ! check_windows_version; then
        echo -e "${YELLOW}Warning: This script is optimized for Windows 11. You might be running a different version.${NC}"
        read -p "Do you want to continue anyway? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi

    # Install Zed
    install_zed

    echo -e "${GREEN}Script completed!${NC}"
    echo "Note: Please complete the installation in the Windows installer window that opened."
}

# Run the script
main
