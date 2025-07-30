"""
Write a function that returns the n-th Fibonacci number.
The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
The sequence looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Example:
    fibonacci(5)  # should return 5 (0, 1, 1, 2, 3, 5)
fibonacci(10) # should return 55
"""


def fibonacci(n):
    numbers_list = [0, 1]
    while len(numbers_list) <= n:
        numbers_list.append(numbers_list[-1] + numbers_list[-2])
    return numbers_list[-1]


result = fibonacci(5)
print(result)
