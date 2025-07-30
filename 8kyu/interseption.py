"""
Given two arrays, write a function to find their intersection (the elements that appear in both arrays).

Example:
intersection([1, 2, 2, 1], [2, 2])  # should return [2, 2]
intersection([4, 9, 5], [9, 4, 9, 8, 4])  # should return [4, 9]
"""

first_list = [1, 2, 2, 1]
second_list = [2, 2]


def intersection(l1, l2):
    return [number for number in l2 if number in l1]


print(intersection(first_list, second_list))
