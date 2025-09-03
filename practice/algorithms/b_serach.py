"""
Implement binary search.
"""

my_array = list(range(1, 101))


def bs(array: list[int], n: int) -> int | None:

    start = 0
    end = len(array)

    if n > end:
        return None

    while start <= end:
        mid = (start + end) // 2
        guess = array[mid]

        if guess == n:
            return array.index(guess)
        if guess < n:
            start = mid + 1
        else:
            end = mid - 1

    return None


print(bs(my_array, 1000))
