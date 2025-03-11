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
    largest = max(l)
    new_l = []
    for i in l:
        if i != largest:
            new_l.append(i)
    if not new_l:
        return None
    return max(new_l)

print(second_largest(variable))