import time
from functools import wraps

"""
Write a basic decorator that measures time.
"""


def measure_hello_speed(func):
    @wraps(func)
    def wrapper():
        now = time.time()
        func()
        after = time.time()
        time_delta = after - now
        print(f"Time it takes to execute the func is: {time_delta:.7f}")
        return time_delta

    return wrapper


@measure_hello_speed
def hello():
    print("hello to all guys!")


hello()
