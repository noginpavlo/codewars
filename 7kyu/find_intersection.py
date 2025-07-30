"""
Write a function that takes two lists and returns a new
list containing only the elements that appear in both lists (without duplicates).

Example:
find_intersection([1, 2, 3, 4], [3, 4, 5, 6])  # Expected output: [3, 4]
find_intersection(["apple", "banana"], ["banana", "cherry"])  # Expected output: ["banana"]
find_intersection([1, 2, 3], [4, 5, 6])  # Expected output: []
"""


def find_intersection(l1, l2):
    return list(set(l1) & set(l2))


result = find_intersection([1, 2, 3, 4], [3, 4, 5, 6])
print(result)
