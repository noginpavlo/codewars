"""
Task:
    You are given a list of integers.
    Use filter() with a lambda function to return a list containing only the numbers greater than 10.

Example:
    Input:
        numbers = [5, 12, 8, 20, 3, 15]
    Output:
        [12, 20, 15]
"""

numbers = [5, 12, 8, 20, 3, 15]

def greater(num_l):
    return list(filter(lambda x : x > 10, num_l))

result = greater(numbers)
print(result)

