from threading import Thread
from functools import wraps


def start_backgroun_job(func):
    """
    Start background job on a different thread.
    """

    @wraps(func)
    def decorator(*args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator
