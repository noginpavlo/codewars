class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"You are {self.age} years old, {self.name}"


person1 = Person("Pavlo", 29)
person2 = Person("Julia", 28)

print(person1)
print(person2)