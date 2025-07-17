from collections import Counter

"""
Description:
Write a function merge_dicts(d1: dict, d2: dict) -> dict that merges two
dictionaries of integer keys and values. If a key exists in both dictionaries,
sum their values in the resulting dictionary; otherwise, include the key-value
pair as is. The result should include all keys from both inputs.

Example:

merge_dicts({1: 2, 2: 3}, {2: 4, 3: 5})

# Expected result: {1: 2, 2: 7, 3: 5}
"""

first_dict = {1: 2, 2: 3}
second_dict = {2: 4, 3: 5}


def merge_dicts(dict1: dict[int, int], dict2: dict[int, int]) -> dict[int, int]:
    counter1 = Counter(dict1)
    counter2 = Counter(dict2)
    return counter1 + counter2


print(merge_dicts(first_dict, second_dict))
