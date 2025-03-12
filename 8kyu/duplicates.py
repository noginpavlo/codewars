"""
Write a function that takes a list and removes all duplicate elements,
keeping the first occurrence of each element in the order they appear.

Examples:
remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # Expected output: [1, 2, 3, 4, 5]
remove_duplicates(["apple", "banana", "apple", "cherry"])  # Expected output: ["apple", "banana", "cherry"]
remove_duplicates([1, 1, 1, 1])  # Expected output: [1]
"""

def remove_duplicates(l):
    unique_elements = set()
    return [x for x in l if not (x in unique_elements or unique_elements.add(x))]

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))