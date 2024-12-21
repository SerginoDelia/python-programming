# Python installion on Apple Silicon

brew install pyenv;
# change to the latest version of Python
pyenv install 3.13.1;

# Setup path for MacOS pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc;
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc;
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init --path)"\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc;

# Set Python version to Global Default
pyenv global 3.13.1;
pyenv versions;

echo "Close your terminal and restart it"

# command: curl -L https://raw.githubusercontent.com/SerginoDelia/python-programming/refs/heads/main/apple-silicon.sh -o python-setup.sh; chmod 700 python-setup.sh; ./python-setup.sh
