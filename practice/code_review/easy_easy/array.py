"""
We have array with digits and some of them are nulls. Move nulls to the end.
"""

my_array = [1, 3, 4, 5, 6, 7, 89, 0, 0, 0, 8, 7, 32, 441, 3]


def null_mover(array: list[int]) -> list[int]:
    changed_l = [n for n in array if n != 0]
    null_list = [n for n in array if n == 0]
    changed_l.extend(null_list)
    return changed_l


result = null_mover(my_array)
print(result)
