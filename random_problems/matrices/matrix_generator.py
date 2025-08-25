"""
Find a desired value in matrix. Use generator to avoide complications with braking
nested loops.
"""

from collections.abc import Generator

MATRIX = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]

TARGET = 5


def iterate_over(nested_array: list[list[int]]) -> Generator[tuple, None, None]:
    for i, raw in enumerate(nested_array):
        for j, cell in enumerate(raw):
            yield (i, j), cell


def find_element(array: list[list[int]], target: int) -> tuple | str:
    gen = iterate_over(array)
    try:
        coords = next(
            (coords for coords, cell in gen if cell == target),
            f"Target {target} not in the matrix",
        )
        return coords
    finally:
        gen.close()  # free recourses that gen holds


target_coords = find_element(MATRIX, TARGET)
print(target_coords)
