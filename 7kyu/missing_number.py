"""
You are given an array of n-1 integers, which are the numbers from 1 to n.
One number is missing. Write a function to find that missing number.

Example:
find_missing([1, 2, 4, 6, 3, 7, 8])  # should return 5
find_missing([1, 2, 3])  # should return 4
"""

variable = [1, 2, 4, 6, 3, 7, 8]


def find_missing(l):
    return sum([n for n in range(1, len(l) + 2)]) - sum(l)


result = find_missing(variable)
print(result)
