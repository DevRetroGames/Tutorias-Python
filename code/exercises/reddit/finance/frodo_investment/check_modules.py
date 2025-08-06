#!/usr/bin/env python3

import importlib.util
import subprocess
import sys

# Check if a given module is installed
def _is_module_installed(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None

# Ensure that the given module is installed; install it via pip if not
def _ensure_module(module_name: str, pip_name: str = None) -> None:
    if not _is_module_installed(module_name):
        # Use pip_name if provided, otherwise default to module_name
        pip_install_name = pip_name if pip_name else module_name
        print(f"🔧 Installing {pip_install_name}...")
        try:
            # Call pip install via subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_install_name])
            print(f"✅ {pip_install_name} installed successfully.")
        except subprocess.CalledProcessError:
            # If installation fails, print an error and exit
            print(f"❌ Failed to install {pip_install_name}. Please install it manually.")
            sys.exit(1)
    else:
        print(f"✅ Module '{module_name}' is already installed.")

# Read a file (e.g., requirements.txt) and verify/install listed modules
def verify_from_file(file_path: str = "requirements.txt") -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                # Skip empty lines and comments
                if not clean_line or clean_line.startswith("#"):
                    continue
                # Support custom pip install name with format: module:pip-package
                if ":" in clean_line:
                    module_name, pip_name = map(str.strip, clean_line.split(":"))
                else:
                    module_name = pip_name = clean_line
                _ensure_module(module_name, pip_name)
    except FileNotFoundError:
        print(f"❌ File '{file_path}' not found.")
        sys.exit(1)