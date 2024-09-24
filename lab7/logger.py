"""
Module logger: Defines logger decorator function.
"""
import logging
from enum import Enum

class LogMode(Enum):
    """Enumeration for logging modes."""
    FILE = "file"
    CONSOLE = "console"

def logged(exception: Exception, mode: LogMode):
    """Decorator logged for logging functions."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(__name__)

            if mode == LogMode.FILE:
                logging.basicConfig(filename='lab7.log', level=logging.INFO)
            else:
                logging.basicConfig(level=logging.INFO)

            try:
                result = func(*args, **kwargs)
                logger.info(
                    "Logged: Function '%s' executed successfully with result: %s",
                    func.__name__, result
                )
                return result
            except exception as e:
                logger.error(
                    "Logged: Exception in function '%s' — %s: %s",
                    func.__name__, exception.__name__, str(e)
                )
                return e
        return wrapper
    return decorator
