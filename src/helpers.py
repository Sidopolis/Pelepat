# Logging improvements

import logging

def setup_logger(name):
    """Create a configured logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
