#!/bin/bash

# List installed Homebrew packages and filter for Python
# Save Python packages in a variable
# -E enables extended regular expressions
# ^(python@|python$) matches lines that start with python@ or end with python
python_packages=$(brew list --formula | grep -E '^(python@|python$)')

# If python_packages is empty, display message and exit with status code 0
if [ -z "$python_packages" ]; then
  echo "No Python packages installed with Homebrew found."
  exit 0
else
  echo "Found Python Packages:"
  # List the found packages
  echo "$python_packages"
  echo "Uninstalling Python Packages..."
fi

# Uninstall Python packages
for package in $python_packages; do
  brew uninstall --ignore-dependencies "$package"
done

# List of commands to execute
commands=(
  "brew install python"
  "python3 -m venv my_env"
  "source my_env/bin/activate"
  "pip3 install requests"
  "pip install openpyxl"
)

# Iterate through the list of commands and execute each command one by one
for cmd in "${commands[@]}"; do
  echo "Executing $cmd..."
  eval $cmd
done
