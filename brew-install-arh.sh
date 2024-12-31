sudo pacman -S base-devel curl file git
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >>~/.bash_profile
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
