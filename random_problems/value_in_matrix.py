from typing import List, Tuple, Generator

"""
Problem: Find all occurrences of a target value in a 2D matrix
Given a 2D list (matrix) of integers, write a function that returns a list of
all coordinates (row_index, column_index) where the target value appears.

If the target does not appear, return an empty list.

Example matrix:
matrix = [
    [7, 2, 3, 7],
    [4, 7, 6, 1],
    [7, 8, 9, 7]
]

Example input/output:
Input: target = 7
Output: [(0, 0), (0, 3), (1, 1), (2, 0), (2, 3)]
Input: target = 5
Output: []

Your task:
Write a function find_all_occurrences(matrix, target) that:
Uses a generator (or nested loops if you prefer) to iterate over the matrix
Collects all coordinates where target appears
Returns the list of those coordinates
Test it on the example matrix and targets above.
"""


def go_through_matrix(
    matrix: List[List[int]],
) -> Generator[Tuple[Tuple[int, int], int], None, None]:
    for r_position, row in enumerate(matrix):
        for v_position, value in enumerate(row):
            yield (r_position, v_position), value


def find_all_occurrences(matrix: List[List[int]], target: int) -> List[Tuple[int, int]]:
    return [
        coordinates
        for coordinates, value in go_through_matrix(matrix)
        if value == target
    ]


my_matrix = [
    [7, 2, 3, 7],
    [4, 7, 6, 1],
    [7, 8, 9, 7],
]

my_target = 7
result = find_all_occurrences(my_matrix, my_target)
print(result)
