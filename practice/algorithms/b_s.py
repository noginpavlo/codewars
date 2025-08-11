"""
Practicing binary search again:
"""

my_list = list(range(12, 113))


def b_s(array: list[int], n: int) -> int | None:
    start = 0
    end = len(array)
    try:
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == n:
                return array.index(n - 1)
            if array[mid] < n:
                start = mid + 1
            elif array[mid] > n:
                end = mid - 1
    except IndexError:
        return None

    return None


result = b_s(my_list, 23)
print(result)
