"""
The goal is to implement binary search
"""

my_list = list(range(1, 101))


def bs(array: list[int], n: int) -> int | None:
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = array[mid]

        if guess == n:
            return array.index(n)
        if guess > n:
            end = mid - 1
        elif guess < n:
            start = mid + 1

    return None


result = bs(my_list, 103)
print(result)
