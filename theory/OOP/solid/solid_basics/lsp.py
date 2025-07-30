"""
L — Liskov Substitution Principle (LSP)
==================================================================================

is about:

Objects of a superclass should be replaceable with objects
of its subclasses without altering the correctness of the program.

In simpler terms:

If 'S' is a subclass of 'T', then objects of type 'T' can be replaced
with objects of type 'S' — without breaking the program.
"""

"""
So basically a subclass has to be ableto do everything that a parent class does
"""

"""
Context:
All birds can fly. It is false in real life.
But let's say it is what our program assumes.
Let's take a pinguin which is a bird. Pinguin cannot fly (in reality).
If Pinguin is a subclass of Bird parent class, it violates LSP.
"""


# let's create a VIOLARTION of the LSP
class DeadBird:
    def fly(self):
        print("I am flying")


class Pinguin(DeadBird):
    def fly(self):
        print(
            """
                I cannot fly, because I am a pinguin, which is a bird technically,
                but I can't.
                """
        )


"""Barbara Liskov doesn't care if you are pinguin, you have to fly because she say so.
If not, she KILLS YOU"""


# now to satisfy Barbara we need to create a Bird class and 2 more classes
# (that can and cannot fly)
class Bird:
    pass  # this class can contain anything that is also achievable in child classes


class FlyingBird(Bird):
    def fly(self):
        print("I am flying")


class Penguin(Bird):
    def walk(self):
        print("Yes I am walking but at least Barbara didn't kill me")
