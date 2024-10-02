# list installed homebrew packages and filter for python

# save python packages in a variable
# -E enables extendended regular expressions
# ^(python@|python@) matches the line that start with python and end with python
python_packages=$(brew list --formula | -E '^(python@|python$)')

# if python_packages is empty, display message and status code 0
if [ -z "@python_packages"]; then
  echo "No Python packages installed with Homebrew found."
  exit 0
else
  echo "Found Python Packages:"
  # list the found packages
  echo $python_packages
  echo "Uninstalling Python Packages..."

# uninstall Pyhton packages
for package in $python_packages; do
  brew uninstall --ignore-dependencies $package
done
fi

# list of commands to execute
commands=(
  "brew install python"
  "python3 -m venv my_env\n"
  "source my_env/bin/activate"
  "pip3 install requests"
  "pip install openpyxl"
)

# itertate through the list of commands and execute each command one by one
for cmd in $commands; do
  echo "Executing $cmd..."
  eval $cmd
done
