import logging
from src.utils.logging_config import configure_logging

# Configure logging once when this module is imported
configure_logging()

def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger instance with the given name.
    Logging configuration is handled globally in logging_config.py.
    """
    return logging.getLogger(name)

