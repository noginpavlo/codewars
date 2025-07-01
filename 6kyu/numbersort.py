from collections import Counter

"""
Given an array of numbers, your function should return an array of arrays,
where each subarray contains all the duplicates of a particular number.
Subarrays should be in the same order as the first occurence of the number.

They contain:

group([3, 2, 6, 2, 1, 3])

>>> [[3, 3], [2, 2], [6], [1]]

Assume the input is always going to be an array of numbers.
If the input is an empty array, an empty array should be returned.
"""


def group(array):
    sorted_array = Counter(array)
    print(sorted_array)
    result = []
    for key, value in sorted_array.items():
        result.append([key for _ in range(value)])
    return result


solution = group([3, 2, 6, 2, 1, 3])
print(solution)
