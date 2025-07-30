class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"You are {self.age} years old, {self.name}"

    def __repr__(self):
        """Official string representation: For developers/ debugging"""
        return "This is the structure of the Person object: ('self.name', self.age)"


person1 = Person("Pavlo", 29)
person2 = Person("Julia", 28)

print(str(person1))
print(str(person2))

print(repr(person1))
print(repr(person2))
