"""
Let's create basic generator now.
"""

from collections.abc import Generator


def basic_gen(iteration_count: int = 0) -> Generator[int, None, None]:
    # Generator[what yields, what .send(type), what returns]

    while True:
        yield iteration_count
        iteration_count += 1


gen = basic_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
