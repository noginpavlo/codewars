import copy

"""
=============================================================================
copy() (Shallow Copy)
Creates a new object, but does not create copies of nested objects inside it.

Instead, it copies references to nested objects.

So, if the original object contains other mutable objects
(like lists or dicts), changes to those nested objects will affect both copies.

=============================================================================
deepcopy() (Deep Copy)
Creates a new object and recursively copies all nested objects too.

This means the new object is completely independent of the original.

Changes made to nested objects in the copy won't affect the original at all.
"""


class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, brand, prise, engine):
        self.brand = brand
        self.prise = prise
        self.engine = engine


engine1 = Engine(100)
car1 = Car("Lada", "100$", engine1)

print("Car1 BEFORE COPYING")
print(
    f"Car1 brand is {car1.brand}. It costs {
        car1.prise}. It's engine is {car1.engine.power} horsepowers (In engine1 declared 100)."
)

print("COPY (Shalow Copy)")
copied_car = copy.copy(car1)
copied_car.engine.power = 999
print(
    f"Copied car's brand is {copied_car.brand}. It costs {
        copied_car.prise}. It's engine is {copied_car.engine.power} horsepowers."
)

print("DEEPCOPY")
deepcopied_car = copy.deepcopy(car1)
deepcopied_car.engine.power = 123
print(
    f"Deepcopied car's brand is {deepcopied_car.brand}. It costs {
        deepcopied_car.prise}. It's engine is {deepcopied_car.engine.power} horsepowers."
)

print("Car1 AFTER COPYING")
print(
    f"Car1 brand is {car1.brand}. It costs {
        car1.prise}. It's engine is {car1.engine.power} horsepowers ."
)
print("copied_car.engine.power = 999 changed the original object of class Car")
