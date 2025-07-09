"""
Let us have a list L.

l = [1,2,3]

Now, if we cycle it and will take consequent pairs, we'll get

(1,2), (2, 3), (3, 1), (1, 2) ...
and so on.

Your task is to create a generator gen(n, iterable) which will iterate over
n-tuples of cycled iterable.
"""

my_list = [1, 2, 3]


def gen(n, iterable: list[int]):
    index = 0
    iterations_done = 0
    while iterations_done < n:
        yield (iterable[index], iterable[index + 1])
        index = (index + 1) % (len(iterable) - 1)
        iterations_done += 1


my_result = []
generator = gen(10, my_list)

my_result.append(next(generator))
my_result.append(next(generator))
my_result.append(next(generator))
my_result.append(next(generator))
my_result.append(next(generator))
my_result.append(next(generator))
my_result.append(next(generator))

print(my_result)
