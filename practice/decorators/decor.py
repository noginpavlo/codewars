from datetime import datetime
from functools import wraps

"""
write a basic decorator
"""


def time_measure(func):
    """
    Measures time of function execution
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.now()
        result = func(*args, **kwargs)
        later = datetime.now()
        print(f"It took {later - now} to execute a function")
        return result

    return wrapper


@time_measure
def some_function():
    calculate_smth = 234 * 324**20
    print(f"Let's calculate something. Something is equal to {calculate_smth}")
    return calculate_smth


some_function()
