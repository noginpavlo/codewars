from collections.abc import Generator

"""
Print the nested list.
Use yield from for that.
"""

nested = [[1, 2], [3, 4, 5], [6]]


def flatten_list(nested_l: list[list[int]]) -> Generator:
    for sublist in nested_l:
        yield from sublist


for number in flatten_list(nested):
    print(number)
