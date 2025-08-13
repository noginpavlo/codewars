import logging

logger = logging.getLogger(__name__)

"""
This is a shor training example to catch bad code within exceptions topic.
"""


class Calculator:
    def divide(self, a: int, b: int):
        try:
            return a / b
        except ZeroDivisionError as e:
            logger.error("Attempt to divide by 0: %s", e)
        except TypeError as e:
            logger.error("Input parameters are not numbers: %s", e)

    def multiply(self, a, b):
        return a * b

    def sum_list(self, numbers: list[int]) -> list[int]:
        return [n for n in numbers if isinstance(n, int)]
