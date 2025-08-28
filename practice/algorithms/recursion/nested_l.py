"""
Example:

Input:
[1, [2, 3], [4, [5, 6]], 7]


Output:
28  # because 1+2+3+4+5+6+7 = 28
"""

my_list = [1, [2, 3], [4, [5, 6]], 7]


def flatten_and_sum(some_list: list):
    return sum(
        flatten_and_sum(element) if isinstance(element, list) else element for element in some_list
    )


result = flatten_and_sum(my_list)
print(result)
