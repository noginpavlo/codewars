from collections import Counter

"""
Write a function that returns the most frequent element in a list. If there are multiple elements with the same highest frequency, return any one of them.
"""

my_list = [1, 3, 2, 1, 4, 1]  # expected 1


def most_frequent(int_list: list[int]) -> int:
    counter = Counter(int_list)
    return max(counter, key=lambda x: counter[x])


print(most_frequent(my_list))
