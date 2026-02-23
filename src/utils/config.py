import os
from dotenv import load_dotenv
from src.utils.logger import get_logger

load_dotenv()

def get_config(key: str, default=None):
    return os.getenv(key, default)
