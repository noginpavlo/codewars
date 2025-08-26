from collections.abc import Iterable, Callable


def filter_emulator(function: Callable, some_iterable: Iterable):
    for item in some_iterable:
        if function(item):
            yield item


my_list = [1,2,3,4,5,6]
result = filter_emulator(lambda x: x % 2 == 0, my_list)

print(list(result))
