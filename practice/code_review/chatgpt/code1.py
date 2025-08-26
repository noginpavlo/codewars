def add_item_to_list(item, my_list: list[int] | None = None) -> list[int]:
    my_list = [] if my_list is None else list(my_list)
    my_list.append(item)
    return my_list


def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


PARTICULAR_NUMBERS = [10, 20, 30]
print(calculate_average(PARTICULAR_NUMBERS))
print(add_item_to_list(5))
print(add_item_to_list(7))
