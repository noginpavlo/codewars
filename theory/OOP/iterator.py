"""
Here I will play with iterators a little bit by creating iterator classes
and iteratin over them.
"""


class Iterable:  # here I want to create an iterable

    def __init__(self, my_range):
        self.my_range = range(my_range)

    def __iter__(self):
        return iter(self.my_range)  # this return an iterator anyway


my_iterable = Iterable(6)

"""
Let's make this stuff clear. The iter() return and iterator anyway. So the
value of my_iterable is an iterator.
Nevertheless, hasattr() says my_iterable has __iter__, but does not have
__next__. This is because it checks if
Iterable class have __next__, checks if it is defined in class declaration and
NOT whether it returns an object
that has __next__. iter(self.my_range) returns an iterator that has __next__.
hasattr does not see it as it checks the Iterable declaration and not the value
of my_iterable.
"""

print(f"Does my_iterable have __iter__?: {hasattr(my_iterable, '__iter__')}")
print(f"Does my_iterable have __next__?: {hasattr(my_iterable, '__next__')}")

for i in my_iterable:
    print(f"This comes from Iterable class: {i}")


# now I want to define an iterator class
class Iterator:
    def __init__(self, number):
        self.range_number = range(number)
        self.limit = 5
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration


my_iterator = Iterator(12)

"""
Now the declaration of the class has __iter__ and __next__, these method kind
of make sense.
So now I can safly set that Iterator class is an actual iterator.
"""

print(f"Does my_iterator have __iter__?: {hasattr(my_iterator, '__iter__')}")
print(f"Does my_iterator have __next__?: {hasattr(my_iterator, '__next__')}")

for n in my_iterator:
    print(n)


# What I want to create not is generator function
def letter_parser(string):
    for letter in string:
        yield letter


gen = letter_parser("here some test to be parsed")

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
