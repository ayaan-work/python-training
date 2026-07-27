# 1) A virtual environment is an isolated Python environment that contains its own:

# Python interpreter
# Installed packages
# Dependencies

# This allows different projects to use different versions of the same package without interfering with each other.

# For example:

# Project A needs Django 4.2
# Project B needs Django 5.1

# Without virtual environments, installing one version could break the other. With a virtual environment, each project has its own isolated packages.

#to create a virtual environment
# Navigate to your project folder:
# cd my_project
# Create a virtual environment:
# python -m venv .venv

#2) Activating the Virtual Environment
# Windows (Command Prompt)
# venv\Scripts\activate
# Windows (PowerShell)
# venv\Scripts\Activate.ps1
# Windows (Git Bash)
# source venv/Scripts/activate
# macOS / Linux
# source venv/bin/activate

# When activated, the terminal changes:

# (venv) C:\Users\Ayaan\my_project>

# The (venv) prefix indicates that the virtual environment is active.

#3) A requirements.txt file lists all the Python packages required for a project.
# Example:

# Django==5.1
# requests==2.32.3
# numpy==2.2.1

# It allows anyone to recreate the same environment.
#pip freeze > requirements.txt (stores project dependencies inside requirements.txt)
#pip install -r requirements.txt (installs all dependencies from requirements.txt)