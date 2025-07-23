from abc import ABC, abstractmethod
"""
O — Open/Closed Principle (OCP)
=============================================================================

is about:
=> Software entities (classes, modules, functions, etc.)
should be open for extension, but closed for modification.

It means basically that you sould use inheritance when introducind new code
other then changing old functions. Works? Don't touch => extend.

Build code in the way so that if you add somehting you don't have to change existing code!!!
"""


# let's create a BAD example code firs
class SickAnimal:
    def make_sound(self, animal_type):
        if animal_type == "dog":
            print("Wof, wof")
        elif animal_type == "cat":
            print("Meow")
        else:
            print("I am a vibe coder")

"""
In this Animal class code if you want to add different animal type you would have to 
add one more elif block, meaning you need to CHANGE THE CODE which is BAD!!! AND YOU WILL DIE
"""

# now let's create more robust and scalable version of this code
class Animal(ABC):
    """
    Note that this in an interface as I don't want it to be called directly.
    I want the type of animal to be specifies by creating each class for each animal type.
    """
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Wof, wof")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class VibeCoder(Animal):
    def make_sound(self):
        print("It didn't work!!! Make it work, PLEEEEEEASE")


"""
Thie way if I want to intorduce one more animal type I don't have to add any changes in original code.
I just create NEW class based on an interface and that's it. Not having to untangle old code to make chagnes.
"""

