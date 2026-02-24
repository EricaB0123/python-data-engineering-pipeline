import logging
import os
from logging.handlers import TimedRotatingFileHandler
from src.utils.settings import Config

# Ensure logs directory exists
os.makedirs(Config.LOGS_DIR, exist_ok=True)

# File paths
MAIN_LOG_FILE = os.path.join(Config.LOGS_DIR, "pipeline.log")
ERROR_LOG_FILE = os.path.join(Config.LOGS_DIR, "errors.log")

# Shared log format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def configure_logging():
    """
    Configure global logging for the entire pipeline with:
    - daily rotation at midnight
    - separate error-only logs
    - console output
    """

    # -----------------------------
    # Main daily rotating log
    # -----------------------------
    main_handler = TimedRotatingFileHandler(
        MAIN_LOG_FILE,
        when="midnight",      # rotate at midnight
        interval=1,           # every 1 day
        backupCount=7,        # keep 7 days of logs
        encoding="utf-8"
    )
    main_handler.setLevel(logging.INFO)

    # -----------------------------
    # Error-only daily rotating log
    # -----------------------------
    error_handler = TimedRotatingFileHandler(
        ERROR_LOG_FILE,
        when="midnight",
        interval=1,
        backupCount=14,       # keep 14 days of error logs
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
