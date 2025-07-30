"""
Write a function that removes duplicate elements
from a given list while keeping the order of elements unchanged.

Example:
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]))
# Output: [1, 2, 3, 4, 5, 6, 7]

print(remove_duplicates(["apple", "banana", "apple", "cherry", "banana"]))
# Output: ["apple", "banana", "cherry"]
"""


def remove(l):
    new_l = []
    for item in l:
        if item not in new_l:
            new_l.append(item)
    return new_l


print(remove(["apple", "banana", "apple", "cherry", "banana"]))
