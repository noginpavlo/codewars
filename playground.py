def if_simple(n: int) -> bool:
    return not any(n % i == 0 for i in range(2, n))


result = if_simple(11)
print(result)
