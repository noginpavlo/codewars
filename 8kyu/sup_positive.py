"""
Sum of Positive

Write a function that takes a list of numbers and returns the sum of all the positive ones.

Example:

Input: [1, -4, 7, 12]
Output: 20   # because 1 + 7 + 12 = 20
"""

my_input = [1, -4, 7, 12]


def sum_positive(numbers_list: list[int]):
    return sum(num for num in numbers_list if num >= 0)


result = sum_positive(my_input)
print(result)
