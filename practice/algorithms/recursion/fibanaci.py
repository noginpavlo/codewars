"""
Basic solution of fibanaci problem.
Calculate fibanaci sequence using recursion:
Function must take number of addition iterations n, first and second number a and b.

Example:
fib(n=5, a=10, b=20)

Output:
30
50
80
130
210

"""


def fib(n: int, a: int, b: int) -> int:
    if n == 1:
        return a
    if n == 2:
        return b
    return fib(n - 1, b, a + b)


result = fib(7, 10, 20)
print(result)
