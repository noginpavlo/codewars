"""
The makeLooper() function (or make_looper in your language) takes a string
(of non-zero length) as an argument. It returns a function. The function it
returns will return successive characters of the string on successive
invocations. It will start back at the beginning of the string once it reaches
the end.

For example:

abc = make_looper('abc')
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call
Different loopers should not affect each other, so be wary of unmanaged global
state.
"""


class Looper:
    def __init__(self, string: str):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        character = self.string[self.index]
        self.index = (self.index + 1) % len(self.string)
        return character

    def __call__(self):
        return next(self)


def make_looper(string: str):
    return Looper(string)


add = make_looper("Coding is hard, but WOW is harder.")
print(add())
print(add())
print(add())
print(add())
