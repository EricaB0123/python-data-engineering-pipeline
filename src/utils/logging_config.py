import logging
import os
from logging.handlers import RotatingFileHandler
from src.utils.settings import Config

# Ensure the logs directory exists
os.makedirs(Config.LOGS_DIR, exist_ok=True)

# File paths
MAIN_LOG_FILE = os.path.join(Config.LOGS_DIR, "pipeline.log")
ERROR_LOG_FILE = os.path.join(Config.LOGS_DIR, "errors.log")

# Shared log format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def configure_logging():
    """
    Configure global logging for the entire pipeline with:
    - rotating main logs
    - rotating error-only logs
    - console output
    """

    # -----------------------------
    # Main rotating log handler
    # -----------------------------
    main_handler = RotatingFileHandler(
        MAIN_LOG_FILE,
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=5,
        encoding="utf-8"
    )
    main_handler.setLevel(logging.INFO)

    # -----------------------------
    # Error-only rotating log handler
    # -----------------------------
    error_handler = RotatingFileHandler(
        ERROR_LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    error_handler.setLevel(logging.ERROR)

    # -----------------------------
    # Console handler
    # -----------------------------
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if Config.DEBUG else logging.INFO)

    # -----------------------------
    # Formatter
    # -----------------------------
    formatter = logging.Formatter(LOG_FORMAT)
    main_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # -----------------------------
    # Root logger configuration
    # -----------------------------
    logging.basicConfig(
        level=logging.DEBUG if Config.DEBUG else logging.INFO,
        handlers=[main_handler, error_handler, console_handler]
    )
