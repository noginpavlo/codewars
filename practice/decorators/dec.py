from datetime import datetime
from functools import wraps

"""
writ a basice decorator
"""


def mesure_time_dec(func):
    """
    Measures execution time of a function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.now()
        func(*args, **kwargs)
        later = datetime.now()
        print(f"It took {later - now} to execute a function")
        return f"It took {later - now} to execute a function"

    return wrapper


@mesure_time_dec
def random_func():
    print("123")
    expression = 1 * 3
    return expression


random_func()
