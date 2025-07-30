"""
Task:
    You are given a 2D list (a list of lists) of integers.
    Flatten the 2D list into a 1D list,
    but only include numbers that are even.

Hint:
    Use two `for` clauses in the list comprehension,
    and a condition to filter only even numbers.

Example:
    Input:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    Output:
        [2, 4, 6, 8]
"""

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def nested(matrix):
    return [num for row in my_matrix for num in row if num % 2 == 0]


result = nested(my_matrix)
print(result)
