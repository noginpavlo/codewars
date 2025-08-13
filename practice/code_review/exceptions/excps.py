import logging

"""
NOTE: there is nothing good in this code except of proper responsibility separation.
Exceptions occur in the parts of the code that are responcibl for data input. 

DO NOT TAKE THIS CODE AS A GOOD PRACTICE EXAMPLE
"""

logger = logging.getLogger(__name__)


class DataAnalyzer:
    _MAX_ITEMS = 5

    def __init__(self, data: list[int]):
        self.data = data

    def average(self) -> float:
        return sum(self.data) / len(self.data)

    def top_items(self) -> list[int]:
        return sorted(self.data, reverse=True)[: self._MAX_ITEMS]

    def filter_positive(self) -> list[int]:
        return [x for x in self.data if x > 0]

    def transform(self) -> list[int]:
        return [x**2 for x in self.data]


def caller(action_id: int, data: list[int]) -> list[int] | float | bool:
    """
    Identifies id of an action and performs calculations.
    IDs:
        1 => average
        2 => top_items
        3 => filter_positive
        4 => transform
    """

    analyzer = DataAnalyzer(data)

    if action_id == 1:
        try:
            return analyzer.average()
        except ZeroDivisionError as e:
            logger.error("Data contains 0 values preventing division: %s", e)
        except TypeError as e:
            logger.error("Data contains non-integer values %s", e)

    elif action_id == 2:
        try:
            return analyzer.top_items()
        except TypeError as e:
            logger.error("Data contains non-integer values %s", e)

    elif action_id == 3:
        try:
            return analyzer.filter_positive()
        except TypeError as e:
            logger.error("Data contains non-integer values %s", e)

    else:
        try:
            return analyzer.transform()
        except TypeError as e:
            logger.error("Data contains non-integer values %s", e)

    return False
