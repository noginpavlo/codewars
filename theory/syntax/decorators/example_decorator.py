import time
from functools import wraps


def measure_time(func):
    """
    Wrapper that measures the execution time of greet() function.
    """

    @wraps(func)  # This does not allow wraper to overwrite greet() metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed in {end - start:.6f} seconds")
        return result

    return wrapper


@measure_time
def greet():
    """Prints the last words that you'll hear before blackout."""
    print("Hello, Josselin Beaumont!")


greet()
