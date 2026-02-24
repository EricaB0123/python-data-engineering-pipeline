import logging
import os
from logging.handlers import RotatingFileHandler
from src.utils.settings import Config

# Ensure the logs directory exists
os.makedirs(Config.LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(Config.LOGS_DIR, "pipeline.log")

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def configure_logging():
    """
    Configure global logging for the entire pipeline with log rotation.
    """

    # Create rotating file handler
    rotating_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5 MB per file
        backupCount=5,              # keep 5 old log files
        encoding="utf-8"
    )

    # Console handler
    console_handler = logging.StreamHandler()

    # Shared formatter
    formatter = logging.Formatter(LOG_FORMAT)
    rotating_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Configure root logger
    logging.basicConfig(
        level=logging.DEBUG if Config.DEBUG else logging.INFO,
        handlers=[rotating_handler, console_handler]
    )
