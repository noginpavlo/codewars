"""
Implement binary search only by memory.
"""

my_list = list(range(1, 101))


def binary_search(array: list[int], n: int) -> int | None:
    start = 0
    end = len(array)

    while start <= end:
        mid = (start + end) // 2
        guess = array[mid]
        if n == guess:
            return n
        if guess > n:
            end = mid - 1
        elif guess < n:
            start = mid + 1

    return None


result = binary_search(my_list, 1)
print(result)
