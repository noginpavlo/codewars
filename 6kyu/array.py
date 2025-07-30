"""
Implement a function that computes the difference between two lists.
The function should remove all occurrences of elements from the first list (a)
that are present in the second list (b).
The order of elements in the first list should be preserved in the result.

Example:
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
"""


def array_diff(l1, l2):
    return [item for item in l1 if item not in l2]


result = array_diff([1, 2, 2, 2, 2, 1, 3, 4, 5], [1])
print(result)
