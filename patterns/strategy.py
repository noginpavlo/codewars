"""
The Strategy pattern lets you swap algorithms or behaviors without changing the context class.
It’s useful because it decouples the “what” from the “how”, so your code is more flexible,
reusable, and easier to extend.

=> It directly supports SOLID principles:

=> Open/Closed: You can add new strategies without modifying existing code.

=> Single Responsibility: The context only orchestrates; strategies handle specific behavior.

=> Dependency Inversion: Context depends on an abstract strategy interface,
not concrete implementations.

In short, it’s great whenever you want interchangeable behaviors, cleaner code,
and adherence to solid design principles.
"""

from abc import ABC, abstractmethod


# strategy interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: int): ...


# concrete strategy
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount: int):
        print(f"They paid ${amount} with Credit Card.")


# concrete strategy
class PayPalPayment(PaymentStrategy):

    def pay(self, amount: int):
        print(f"They paid ${amount} with PayPal.")


# context
class Order:

    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


payment = Order(CreditCardPayment())
payment.process_payment(10)
