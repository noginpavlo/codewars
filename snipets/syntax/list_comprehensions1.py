"""
Task:
    You are given a list of integers.
    Create a new list that contains the square of each number, 
    but only if the number is divisible by 3.

Hint:
    Use a conditional inside the list comprehension.

Example:
    Input:
        nums = [1, 3, 4, 6, 8, 9, 12]
    Output:
        [9, 36, 81, 144]
"""

nums = [1, 3, 4, 6, 8, 9, 12]
 
def result_function(numbers):
    return [n ** 2 for n in numbers if n % 3 == 0]

result = result_function(nums)
print(result)
