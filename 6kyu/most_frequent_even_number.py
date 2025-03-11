"""
Write a function that takes a list of integers and returns the most frequently occurring even number.

If multiple even numbers have the same frequency, return the largest one.
If there are no even numbers, return None.

Example:
print(most_frequent_even([2, 3, 2, 4, 4, 4, 6, 2]))  # Expected: 4
print(most_frequent_even([1, 3, 5, 7]))  # Expected: None
print(most_frequent_even([10, 20, 10, 20, 30, 20]))  # Expected: 20

"""

from collections import  Counter

variable = [2, 3, 2, 4, 4, 4, 6, 2]

def most_frequent_even(l):
    count = Counter([n for n in l if n % 2 == 0])
    if not count:
        return None

    max_frequency = count.most_common(1)[0][1]
    most_common = count.most_common()

    return max([n for n, f in most_common if f == max_frequency])

print(most_frequent_even(variable))