"""
Write a function that takes a list of numbers and returns the second largest number in the list.

If there's no second largest number (list has one unique element), return None.

Examples:
print(second_largest([10, 20, 4, 45, 99]))  # Expected: 45
print(second_largest([5, 5, 5]))  # Expected: None
print(second_largest([1]))  # Expected: None
"""


variable = [10, 20, 4, 45, 99]

def second_largest(l):
    if len(set(l)) <= 1:
        return None
    l.remove(max(l))
    return max(l)

print(second_largest(variable))