class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name} is {self.age} years old!"

    def __gt__(self, other):
        if isinstance(other, Person):
            return f"I am older then you, {other.name}!"
        else:
            return f"It seems that you are older then me, {other.name}!"

p1 = Person("Josselin Beaumont", 42)
p2 = Person("Pablo Escobar", 33)

print(p2 > p1)
