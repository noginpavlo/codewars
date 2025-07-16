from collections import Counter

"""
Write a function unique_elements(lst) that takes a list lst of integers and
returns a new list containing only the elements that appear exactly once in the
original list. The returned list should preserve the original order.

Example:

unique_elements([1, 2, 2, 3, 4, 1, 5])
# Expected output: [3, 4, 5]
"""

mixed_list = [1, 2, 2, 3, 4, 1, 5]


def u_elements(lst: list[int]) -> list[int]:
    counter = Counter(lst)
    return [elm for elm in lst if counter[elm] == 1]


print(u_elements(mixed_list))
