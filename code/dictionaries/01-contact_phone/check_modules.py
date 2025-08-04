#!/usr/bin/env python3

import importlib.util
import subprocess
import sys

def _is_module_installed(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None

def _ensure_module(module_name: str, pip_name: str = None) -> None:
    if not _is_module_installed(module_name):
        pip_install_name = pip_name if pip_name else module_name
        print(f"🔧 Installing {pip_install_name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_install_name])
            print(f"✅ {pip_install_name} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {pip_install_name}. Please install it manually.")
            sys.exit(1)
    else:
        print(f"✅ Module '{module_name}' is already installed.")

def verify_from_file(file_path: str = "requirements.txt") -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                if not clean_line or clean_line.startswith("#"):
                    continue
                if ":" in clean_line:
                    module_name, pip_name = map(str.strip, clean_line.split(":"))
                else:
                    module_name = pip_name = clean_line
                _ensure_module(module_name, pip_name)
    except FileNotFoundError:
        print(f"❌ File '{file_path}' not found.")
        sys.exit(1)