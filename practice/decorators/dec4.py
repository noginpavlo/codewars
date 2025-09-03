"""
Write a decorator that measures time.
"""

import time
from functools import wraps


def measure_time(func):
    """Decorator that measures time of function execution."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        now = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"Execution time: {after - now:.8f}")

    return wrapper


@measure_time
def counter_function(iterable: list):
    for n in iterable:
        print(n)


some_list = [1, 3, 4, 5, 6, 7, 78, 23, 234, 5423, 222]

counter_function(some_list)
