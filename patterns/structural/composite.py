"""
composite.py
============================

Composite Design Pattern
-------------------------
Definition:
The Composite pattern allows you to treat individual objects and compositions of objects
uniformly. It is used to represent part–whole hierarchies (e.g., trees).

Consists of:
1. Component (interface/abstract base class) – declares the common operations.
2. Leaf (concrete class) – represents simple (atomic) objects in the structure.
3. Composite (concrete class) – represents complex objects that can hold children.
4. Client– works with objects through the common interface, without caring
   whether it deals with a leaf or a composite.

When to use:
- When you need to represent objects in a tree structure (e.g., file systems, UIs, organizations).
- When you want to treat individual and composite objects the same way.
- When your code benefits from recursive behavior(e.g., applying an operation to a whole structure).

Advantages:
- Simplifies client code — uniform treatment of leaf and composite.
- Makes adding new component types easy.
- Supports recursive structures naturally.

Example below: a company hierarchy where Managers can manage Employees.
"""

from abc import ABC, abstractmethod


# ─────────────────────────────────────────────
# 1. Component Interface
# ─────────────────────────────────────────────
class Employee(ABC):
    """Component: declares the common interface for all employees."""

    @abstractmethod
    def show_details(self, indent: int = 0):
        """Display employee details."""


# ─────────────────────────────────────────────
# 2. Leaf: Represents individual (non-managing) employees
# ─────────────────────────────────────────────
class Developer(Employee):
    """Leaf: represents a simple employee with no subordinates."""

    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def show_details(self, indent: int = 0):
        print(" " * indent + f"- {self.position}: {self.name}")


class Designer(Employee):
    """Another Leaf type."""

    def __init__(self, name: str):
        self.name = name

    def show_details(self, indent: int = 0):
        print(" " * indent + f"- Designer: {self.name}")


# ─────────────────────────────────────────────
# 3. Composite: Represents managers or departments that contain employees
# ─────────────────────────────────────────────
class Manager(Employee):
    """Composite: can hold children employees (either leaf or composite)."""

    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        self._subordinates: list[Employee] = []

    def add(self, employee: Employee):
        """Add a subordinate employee."""
        self._subordinates.append(employee)

    def remove(self, employee: Employee):
        """Remove a subordinate employee."""
        self._subordinates.remove(employee)

    def show_details(self, indent: int = 0):
        print(" " * indent + f"{self.position}: {self.name}")
        for e in self._subordinates:
            e.show_details(indent + 4)


# ─────────────────────────────────────────────
# 4. Client code: works with the structure through the Component interface
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Create leaf employees
    dev1 = Developer("Alice", "Backend Developer")
    dev2 = Developer("Bob", "Frontend Developer")
    designer = Designer("Charlie")

    # Create a composite manager
    lead = Manager("Diana", "Tech Lead")
    lead.add(dev1)
    lead.add(dev2)

    # Create another composite manager
    ceo = Manager("Eve", "CEO")
    ceo.add(lead)
    ceo.add(designer)

    # Client treats all objects the same
    print("Company Structure:\n")
    ceo.show_details()
