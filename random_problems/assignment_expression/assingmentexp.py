"""
You are given an implicit list of integers from 1 to 30.
You need to generate a list of square roots of numbers whose squares are greater than 500,
but without calculating the square more than once per number.
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 30]


def root(n_list: list[int]) -> list[int]:
    return [num for n in n_list if (num := n * n) > 500]


result = root(my_list)
print(result)
