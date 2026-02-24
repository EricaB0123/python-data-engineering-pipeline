import logging
import os
from src.utils.settings import Config

# Ensure the logs directory exists
os.makedirs(Config.LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(Config.LOGS_DIR, "pipeline.log")

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def configure_logging():
    """
    Configure global logging for the entire pipeline.
    This function is called once when logger.py imports it.
    """
    logging.basicConfig(
        level=logging.DEBUG if Config.DEBUG else logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()  # console output
        ]
    )
