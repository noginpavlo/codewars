some_array = [234, 2, 3, 4, 534, 12, 235, 23, 43, 23]


def quicksort(unsorted_array: list[int]):
    if len(unsorted_array) < 2:
        return unsorted_array
    pivot = unsorted_array[0]
    less = [i for i in unsorted_array if i < pivot]
    greater = [j for j in unsorted_array if j > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


result = quicksort(some_array)
print(result)
