class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        else:
            return NotImplemented


p1 = Person("Josselin Beaumont", 48)
p2 = Person("Pavlo Nohin", 29)

print(p1 + p2)