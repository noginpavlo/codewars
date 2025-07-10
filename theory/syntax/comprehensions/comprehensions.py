"""
Task:
    Given a list of integers, return a new list where:
    Even numbers are divided by 2
    Odd numbers are multiplied by 3
    Use a list comprehension.

Input example:

    nums = [1, 2, 3, 4, 5]

Expected output:
    [3, 1, 9, 2, 15]
"""

input_list = [1, 2, 3, 4, 5]

def process_num(my_list):
    return [n * 3 if n % 2 != 0 else n // 2 for n in my_list]

result = process_num(input_list)
print(result)

