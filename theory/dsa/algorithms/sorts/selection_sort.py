"""
SELECTION SORT is a O(n**2) sorting algorithm.
Slow and I guess that it is rather instructive then proctical. ADJUST WHEN HAVE BETTER UNDERSTANDING

=> Takes unsorted_list
=> Finds the smallest element in such list
=> Saves it to a new list (eventually sorted)
=> Deleted the value from unsorted_list
=> Repeats till unsorted_list is empty
"""


def find_smallest(array: list[int]) -> int:
    """
    Finds the smallest element in array. O(n).
    Used in selection_sort function.
    """
    smallest_n = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest_n:
            smallest_n = array[i]
            smallest_index = i

    return smallest_index


def selection_sort(array: list[int]) -> list[int]:
    """
    Takes smallest element in array from find_smallest() and appends it to a sorted_list.
    selection_sort() function is O(n) complexity.
    But find_smallest() is O(n) too.
    Then the complexity of 2 functions in total that constitute algorithm:
    O(n * n) == O(n**2)
    """

    sorted_array: list[int] = []

    for _ in range(len(array)):
        smallest = find_smallest(array)
        sorted_array.append(array.pop(smallest))

    return sorted_array


my_list = [1, 2, 4, 5, 6, 73, 4, 5, 3, 5, 12, 34, 123, 4, 123, 4, 1, 3]

my_list_sorted = selection_sort(my_list)
print(my_list_sorted)
