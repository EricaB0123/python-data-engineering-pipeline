import os
from dotenv import load_dotenv
from src.utils.paths import RAW_DIR, PROCESSED_DIR, LOG_DIR

load_dotenv()

class Config:
    DATA_RAW_DIR = RAW_DIR
    DATA_PROCESSED_DIR = PROCESSED_DIR
    LOGS_DIR = LOG_DIR

    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("API_KEY")

    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

    TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"

    @classmethod
    def validate(cls):
        if not cls.API_URL:
            raise ValueError("API_URL missing")
        if not cls.API_KEY:
            raise ValueError("API_KEY missing")
