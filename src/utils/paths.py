import os

# Base project directory (the folder where your project lives)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Data directories
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

# Logs directory
LOG_DIR = os.path.join(BASE_DIR, "logs")


#absolute paths
#no reliance on where Python is run from
#no repeated strings
#no surprises when running modules
