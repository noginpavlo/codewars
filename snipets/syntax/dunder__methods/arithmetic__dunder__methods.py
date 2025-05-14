class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __add__(self, other):
        if isinstance(other, Person):
            new_age = self.age + other.age
            new_name = f"{self.name} and {other.name}"
            return Person(new_name, new_age)
        else:
            return NotImplemented


    def __str__(self):
        return f"{self.name} are {self.age} years old in total!"

p1 = Person("Josselin Beaumont", 48)
p2 = Person("Pavlo Nohin", 29)

print(p1 + p2)