import time
import logging
logger = logging.getLogger(__name__)
def retry(attempts=2, delay=2):
    def decorator(function):
        def wrapper(*args, **kwargs):
            attempt = 1
            current_delay = delay
            last_error = None
            while attempt <= attempts:
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    logger.info((f"function failed, trying again: {e}"))
                    time.sleep(current_delay)
                    current_delay *= 2
                    attempt += 1
            raise last_error
        return wrapper
    return decorator
            