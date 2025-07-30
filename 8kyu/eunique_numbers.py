"""
Write a function that takes a list of numbers and returns a new list containing only the unique elements
(removing duplicates but keeping order).

Examples:
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Expected: [1, 2, 3, 4, 5]
print(unique_elements([7, 7, 7, 7]))  # Expected: [7]
print(unique_elements([]))  # Expected: []
"""


def unique_elements(l):
    return list(set(l))


print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
