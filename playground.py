def infinite_recursion(n):
    if n < 1:
        return
    print(n)
    return infinite_recursion(n - 1)


infinite_recursion(3)
