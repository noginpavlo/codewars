"""
Let's *unpack some stuff.
"""

packed_list = [
    [1, 2, 3],
    [3, 3, 6],
    [1, 4, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 324, 3],
    [1, 5, 3],
    [1, 2, 3],
    [2, 2, 3],
    [345, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]


def raw_pretty_printer(array: list[list]) -> str:
    for n_1, n_2, n_3 in array:
        print(f"This are: first element - {n_1}, second element - {n_2}, third element - {n_3}")

    return "hello world"


raw_pretty_printer(packed_list)
