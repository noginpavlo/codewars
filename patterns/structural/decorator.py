"""
decorator.py
============================

Decorator Design Pattern
-------------------------
Definition:
The Decorator pattern dynamically adds responsibilities to an object
without modifying its structure. It wraps objects to extend behavior at runtime.

Structure:
1. COMPONENT (interface/ABC)
2. CONCRETE COMPONENT (core object)
3. Decorator (base class) — wraps Component
4. CONCRETE DECORATORS — extend behavior
"""

from abc import ABC, abstractmethod


# ─────────────────────────────────────────────
# 1. Component Interface
# ─────────────────────────────────────────────
class Coffee(ABC):
    """Interface for coffee."""

    @abstractmethod
    def cost(self) -> float: ...

    @abstractmethod
    def description(self) -> str: ...


# ─────────────────────────────────────────────
# 2. Concrete Component
# ─────────────────────────────────────────────
class SimpleCoffee(Coffee):
    """ConcreteComponent: provides core behavior."""

    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Simple Coffee"


# ─────────────────────────────────────────────
# 3. Base Decorator
# => This decorator exists as a layer between basic substance (Coffee) and the decorators logic.
# => Decorators add Sugar, Milk and Cream regarles of what basic substance is. It can be Tee.
# => So creating basic decorator decouples the logic of adding something from the substance.
# ─────────────────────────────────────────────
class CoffeeDecorator(Coffee):
    """Base Decorator: wraps a Coffee object."""

    def __init__(self, coffee: Coffee):
        self._coffee = coffee  # composition

    def cost(self) -> float:
        return self._coffee.cost()  # delegate

    def description(self) -> str:
        return self._coffee.description()  # delegate


# ─────────────────────────────────────────────
# 4. Concrete Decorators
# ─────────────────────────────────────────────
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 0.5

    def description(self) -> str:
        return super().description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 0.2

    def description(self) -> str:
        return super().description() + ", Sugar"


class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 0.7

    def description(self) -> str:
        return super().description() + ", Whipped Cream"


# ─────────────────────────────────────────────
# 5. Client Code
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Create base coffee
    my_coffee = SimpleCoffee()
    print(f"{my_coffee.description()} = ${my_coffee.cost():.2f}")

    # Wrap with Milk
    my_coffee_with_milk = MilkDecorator(my_coffee)
    print(f"{my_coffee_with_milk.description()} = ${my_coffee_with_milk.cost():.2f}")

    # Wrap with Sugar
    my_coffee_with_sugar = SugarDecorator(my_coffee)
    print(f"{my_coffee_with_sugar.description()} = ${my_coffee_with_sugar.cost():.2f}")

    # Wrap with Whipped Cream
    my_coffee_with_cream = WhippedCreamDecorator(my_coffee)
    print(f"{my_coffee_with_cream.description()} = ${my_coffee_with_cream.cost():.2f}")
