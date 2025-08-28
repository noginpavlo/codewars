"""
This is a basic recurcion example that implements both basic and recurcive cases.
"""


def basic_recurcion(n):
    if n < 1:
        return 0
    print(n)
    return basic_recurcion(n - 1)


basic_recurcion(10)


"""
This example shows function that implements recurcive case,
but does not implement basic case.
As a result recurcion goes forever until max recurcive depthe is reached.
"""


def infinite_recursion(n):
    print(n)
    return infinite_recursion(n - 1)


infinite_recursion(10)
