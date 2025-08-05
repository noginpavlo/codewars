"""
>>>A getter is a method that retrieves the value of an attribute.

>>>A setter is a method that sets or updates the value of an attribute, often with validation.
"""

"""
Create a Dog class that has name and agae attributes.
Let's make sure that age is valid.
"""


class Dog:
    """Dog that can be of age that is no larger then the longest-lived-dog's age."""

    def __init__(self, name: str, age: int) -> None:  # None return is standard for __init__ btw
        self.name: str = name
        self._age: int = age  # note that this variable is underscored meaning for internal use only

    @property  # this is needed for @age.setter even work btw
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("The age is not valid. The age must be > 0")
        if value > 29:
            raise ValueError(
                """The age you provided exedes the longes-lived
            dog age which is 29 y.o., lived by Bluey from Australia.
            Please provide the confirmation of dog's age."""
            )
        self._age = value

    def bark(self) -> str:
        return f"Woof, my name is {self.name}, I am {self.age} yers old."


dog1 = Dog("AngryDog", 12)
dog2 = Dog("LovelyDog", 22)

print(dog1.bark())
print(dog2.bark())

dog1.age = 3  # this calls @age.setter and sets age to dog1
dog2.age = 4  # this calls @age.setter and sets age to dog2

print("======================AFTER AGE RESET======================")

print(dog1.bark())
print(dog2.bark())
