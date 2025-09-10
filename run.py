#!/usr/bin/env python3
"""
Fritz IP Updater - Entry Point

This script serves as the main entry point for the Fritz IP Updater application.
"""

import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app.main import main

if __name__ == "__main__":
    main()