"""
Task:
    You are given a list of integers.
    Use map() with a lambda function to return a new list where each number is doubled.

Example:
    Input:
        numbers = [1, 2, 3, 4, 5]
    Output:
        [2, 4, 6, 8, 10]
"""


numbers = [1, 2, 3, 4, 5]

def double(nums):
    return list(map(lambda x : x*2, nums))

result = double(numbers)
print(result)

