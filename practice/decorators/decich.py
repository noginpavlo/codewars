from functools import wraps
from time import time

"""
Write a decorator and be good
"""


def average_time_logger(n: int):

    def time_logger(func):
        """Decorator that measures function's execution time"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            record = []
            for _ in range(1, n + 1):
                now = time()
                func(*args, **kwargs)
                later = time()
                record.append(later - now)
                average_time = sum(record) / len(record)
            print(f"The average time based on {n} executions is {average_time} seconds.")
            return average_time

        return wrapper

    return time_logger


@average_time_logger(10)
def say_hellow():
    print("Hey hey")


say_hellow()
