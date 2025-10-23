my_list = list(range(1, 100))


def bs(ordered_list: list[int], s_number: int) -> int | None:
    start = 0
    end = len(ordered_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if ordered_list[mid] == s_number:
            return ordered_list.index(s_number)
        if ordered_list[mid] < s_number:
            start = mid + 1
        else:
            end = mid - 1

    return None


restult = bs(my_list, 10)
print(restult)
