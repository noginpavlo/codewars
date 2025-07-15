my_list = [1, 23, 4, 5, -6, 7, -8, 9, -12]


def some_function(some_list: list[int]) -> list[int]:
    return [x for x in some_list if x % 2 == 0]


print(some_function(my_list))
