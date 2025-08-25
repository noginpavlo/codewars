"""
Here I implement basic iterator.
Practice for memory and understanding.
"""


class BasicIterator:
    """This is a basic iterator. Increments one at a time with __next__."""

    def __init__(self, start=0):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        current = self.start
        self.start += 1
        return current


my_iterator = BasicIterator(10)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
