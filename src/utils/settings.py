"""
Centralised project settings.

This file gathers environment variables, directory paths, and global
configuration values in one place so the rest of the project stays clean.
"""

import os
from dotenv import load_dotenv
from src.utils.paths import RAW_DIR, PROCESSED_DIR, LOG_DIR

# Load .env file
load_dotenv()

# ---------------------------------------------------------------------
# Environment variables
# ---------------------------------------------------------------------

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

# Optional defaults
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))

# ---------------------------------------------------------------------
# Project directories
# ---------------------------------------------------------------------

DATA_RAW_DIR = RAW_DIR
DATA_PROCESSED_DIR = PROCESSED_DIR
LOGS_DIR = LOG_DIR

# ---------------------------------------------------------------------
# Pipeline behaviour
# ---------------------------------------------------------------------

# Whether to print verbose logs to console
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Default timestamp format for the entire project
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
