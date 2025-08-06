"""
The basic boilerplate that we have when defining attributes is __init__.

Something like this:
--------------------------------
def __init__(self, x, y, … ):   |
self.x = x                      |
self.y = y                      |
--------------------------------

To make is shorter we can use dataclass form PEP-557.

The thing is that it is used just to avoid the huge boilerplate when a lot of attributes
are defined in __init__.
"""

from dataclasses import dataclass, field
from datetime import date


# pylint says that there are too many instance attributes, and this id why we use @dataclass
@dataclass
class Book:
    title: str
    author: str
    published: date
    pages: int
    price: float
    isbn: str | None = None
    tags: list[str] = field(default_factory=list)
    in_stock: bool = True

    def is_expensive(self) -> bool:
        return self.price > 50

    def age(self) -> int:
        return date.today().year - self.published.year


if __name__ == "__main__":
    b = Book("Clean Code", "Robert C. Martin", date(2008, 8, 1), 464, 58.99)
    print(b)
    print("Expensive:", b.is_expensive())
    print("Age:", b.age())
