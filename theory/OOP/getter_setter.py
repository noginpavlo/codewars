"""
>>>A getter is a method that retrieves the value of a private or protected
attribute.

>>>A setter is a method that sets or updates the value of a private or
protected attribute, often with validation.
"""

"""
Create a Dog class that has name and agae attributes.
Let's make sure that age is valid.
"""


class Dog:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self._age: int = age

    @property  # this is needed for @age.setter even work btw.
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("The age is not valid. The age must be > 0")
        elif value > 29:
            raise ValueError(
                """The age you provided exedes the longes-lived
            dog age which is 29 y.o., lived by Bluey from Australia.
            Please provide the confirmation of dog's age."""
            )
        else:
            self._age = value

    def bark(self):
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
