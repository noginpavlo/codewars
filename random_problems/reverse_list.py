"""
Write a function that reverses a given list.
"""

my_list = [1, 2, 3]


def reverse_list(forward_list: list[int]):
    return forward_list[::-1]


print(reverse_list(my_list))
