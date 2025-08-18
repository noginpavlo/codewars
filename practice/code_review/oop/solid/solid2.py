from abc import ABC, abstractmethod


# ----------------------------
# Transaction storage / manager
# ----------------------------
class BaseTransactions(ABC):
    @property
    @abstractmethod
    def transactions_items(self) -> list: ...


class Transactions(BaseTransactions):
    """Manages all transactions."""

    def __init__(self):
        self._transactions = []

    @property
    def transactions_items(self):
        return self._transactions

    def add_transaction(self, method: str, amount: float):
        self._transactions.append({"method": method, "amount": amount})

    def refund_last(self):
        if self._transactions:
            refunded = self._transactions.pop()
            print(f"Refunded transaction: {refunded}")


# ----------------------------
# Payment strategy interface
# ----------------------------
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float, transactions: Transactions):
        pass


# ----------------------------
# Concrete payment strategies
# ----------------------------
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float, transactions: Transactions):
        print(f"Processing credit card {self.card_number} for ${amount}")
        transactions.add_transaction("credit_card", amount)


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float, transactions: Transactions):
        print(f"Processing PayPal {self.email} for ${amount}")
        transactions.add_transaction("paypal", amount)


# ----------------------------
# Cart
# ----------------------------
class Cart:
    """Handles items in cart."""

    def __init__(self):
        self.items = []

    def add_to_cart(self, item: str, price: float):
        self.items.append({"item": item, "price": price})

    def total(self) -> float:
        return sum(item["price"] for item in self.items)


# ----------------------------
# Checkout
# ----------------------------
class Checkout:
    """Handles checkout using any payment strategy."""

    def __init__(self, payment_strategy: PaymentStrategy, transactions: Transactions):
        self.payment_strategy = payment_strategy
        self.transactions = transactions

    def process_payment(self, cart: Cart):
        amount = cart.total()
        self.payment_strategy.pay(amount, self.transactions)
        print("Checkout complete!")


# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    cart = Cart()
    cart.add_to_cart("Laptop", 1200)
    cart.add_to_cart("Mouse", 50)

    transactions = Transactions()

    cc_payment = CreditCardPayment("1234-5678-9012-3456")
    checkout = Checkout(cc_payment, transactions)
    checkout.process_payment(cart)

    paypal_payment = PayPalPayment("user@example.com")
    checkout_pp = Checkout(paypal_payment, transactions)
    checkout_pp.process_payment(cart)

    # Refund last transaction
    transactions.refund_last()
