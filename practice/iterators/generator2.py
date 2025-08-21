"""This is an implementation of itertools.count using generator."""


def count(start_n: int):
    while True:
        yield start_n
        start_n += 1
