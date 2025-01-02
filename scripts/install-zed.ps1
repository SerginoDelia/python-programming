# Requires -RunAsAdministrator
#Set-ExecutionPolicy Bypass -Scope Process -Force
#.\install-zed.ps1

# Colors for output
$Green = [System.ConsoleColor]::Green
$Red = [System.ConsoleColor]::Red

# Function to check if a command exists
function Test-Command($CommandName) {
    return $null -ne (Get-Command -Name $CommandName -ErrorAction SilentlyContinue)
}

# Function to write error and exit
function Write-ErrorAndExit($Message) {
    Write-Host "Error: $Message" -ForegroundColor $Red
    exit 1
}

Write-Host "Starting Zed installation..." -ForegroundColor $Green

# Enable long path support
Write-Host "Enabling long path support..."
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
    -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force

# Check for required commands
if (-not (Test-Command "git")) {
    Write-ErrorAndExit "Git is not installed. Please install Git first."
}

# Install rustup if not present
if (-not (Test-Command "cargo")) {
    Write-Host "Installing rustup..."
    $rustupInit = "$env:TEMP\rustup-init.exe"
    Invoke-WebRequest -Uri "https://win.rustup.rs/x86_64" -OutFile $rustupInit
    Start-Process -FilePath $rustupInit -ArgumentList "-y" -Wait
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}

# Enable git long paths
Write-Host "Configuring git for long paths..."
git config --system core.longpaths true

# Create temporary directory
$tempDir = New-Item -ItemType Directory -Path "$env:TEMP\zed-install-$(Get-Random)"
Set-Location $tempDir

# Clone Zed repository
Write-Host "Cloning Zed repository..."
git clone https://github.com/zed-industries/zed.git
Set-Location zed

# Check for Visual Studio Build Tools
if (-not (Test-Path "${env:ProgramFiles(x86)}\Microsoft Visual Studio")) {
    Write-Host "Visual Studio Build Tools not found. Please install Visual Studio with C++ build tools."
    Start-Process "https://visualstudio.microsoft.com/downloads/"
    Write-ErrorAndExit "Please run this script again after installing Visual Studio Build Tools."
}

# Check for Windows SDK
$sdkPath = "${env:ProgramFiles(x86)}\Windows Kits\10"
if (-not (Test-Path $sdkPath)) {
    Write-Host "Windows SDK not found. Please install Windows 10 SDK."
    Start-Process "https://developer.microsoft.com/windows/downloads/windows-sdk/"
    Write-ErrorAndExit "Please run this script again after installing Windows SDK."
}

# Build Zed
Write-Host "Building Zed..."
$env:ZED_RC_TOOLKIT_PATH = "${env:ProgramFiles(x86)}\Windows Kits\10\bin\10.0.20348.0\x64"
cargo build --release

# Create installation directory
$installDir = "$env:LOCALAPPDATA\Programs\Zed"
New-Item -ItemType Directory -Path $installDir -Force

# Copy built files
Copy-Item "target\release\zed.exe" -Destination $installDir
Copy-Item "target\release\*.dll" -Destination $installDir -ErrorAction SilentlyContinue

# Add to PATH
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$installDir*") {
    [Environment]::SetEnvironmentVariable(
        "Path",
        "$userPath;$installDir",
        "User"
    )
}

# Cleanup
Set-Location $env:USERPROFILE
Remove-Item $tempDir -Recurse -Force

Write-Host "Zed has been successfully installed!" -ForegroundColor $Green
Write-Host "You may need to restart your terminal for the PATH changes to take effect."
Write-Host "You can now run Zed by typing 'zed' in your terminal"
