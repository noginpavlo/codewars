class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name} is {self.age} years old!"

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        else:
            return False


p1 = Person("Josselin Beaumont", 42)
p2 = Person("Pablo Escobar", 33)

print(p2 > p1)
print(p1 > p2)
