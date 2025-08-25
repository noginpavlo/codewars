"""
Create and iterator and make 3 copies of it with itertools.tee
"""

from itertools import tee


def simple_gen(start=0, end=10):
    yield from range(start, end + 1)


gen = simple_gen(1, 3)
gen1, gen2, gen3 = tee(gen, 3)  # makes 3 copies of gen to reuse a gen many times(avoids exhaustion)

print("Exhaust gen1:")
print(next(gen1))
print(next(gen1))
print(next(gen1))

print("Exhaust gen2:")
print(next(gen2))
print(next(gen2))
print(next(gen2))

print("Exhaust gen3:")
print(next(gen3))
print(next(gen3))
print(next(gen3))
