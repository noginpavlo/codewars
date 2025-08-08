from abc import ABC, abstractmethod

"""
This is a pattern practice from Open/Closed Principle SOLID, Clean Code book.
"""


class Pet(ABC):
    """Interface for pets. Defines what they can do, name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def say(self):
        pass

    @abstractmethod
    def do_tricks(self):
        pass

    @abstractmethod
    def meets_condition(self) -> bool:
        pass


class Cat(Pet):
    """This is a cat. It can meaw and sleep."""

    def say(self):
        print("Meaw!")

    def do_tricks(self):
        print("Sleeps on a couch...")

    def meets_condition(self):
        if self.age < 2:
            return True
        return False


class Dog(Pet):
    """This is a dog. It can bark and spin around."""

    def say(self):
        print("Bark!")

    def do_tricks(self):
        print("Spins around")

    def meets_condition(self):
        if self.name[0] == "D":
            return True
        return False


class FeedPet:
    """Feeds a pet if the condition is met"""

    def feed(self, pets: list[Pet]):
        for pet in pets:
            if pet.meets_condition():
                print(f"Feed {pet.name}")
            else:
                print(f"Pet {pet.name} does not meet feeding conditions")


my_pets = [
    Cat("Tom", 3),
    Dog("Duke", 2),
    Cat("Ginger", 1),
    Dog("Rex", 5),
]

feeder = FeedPet()
feeder.feed(my_pets)
