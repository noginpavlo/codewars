from abc import ABC, abstractmethod

"""
The goal is to refactor code and make it consistent with SOLID.
"""


class BaseOrder(ABC):

    @property
    @abstractmethod
    def total(self): ...

    @property
    @abstractmethod
    def items(self): ...


class Discount(ABC):

    @abstractmethod
    def calculate_discount(self, total: float) -> float: ...


class Order(BaseOrder):
    """Keeps order data"""

    def __init__(self, items: list, total: float):
        self._items = items
        self._total = total

    @property
    def items(self) -> list:
        return self._items

    @property
    def total(self) -> float:
        return self._total


class TenPercentDiscount(Discount):
    """Calculates discount price"""

    def calculate_discount(self, total: float) -> float:
        return total * 0.1


class OrderSaver:
    """Saves order"""

    def save_order(self, order: BaseOrder) -> None:
        print(f"Saving {order} to database...")


class InvoicePrinter:
    """Prints invoice"""

    def print_invoice(self, order: BaseOrder):
        print("Invoice:")
        for item in order.items:
            print(item)
        print(f"Total: {order.total}")
