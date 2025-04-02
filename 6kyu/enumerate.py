"""
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
"""

from collections import Counter

def duplicate_encode(s):
    count_items = dict(Counter(s))
    print(count_items)
    result_string = ""
    for count in count_items.values():
        if count > 1:
            result_string.join("more thebn oone ")
        else:
            result_string.join("!!!!")
    return result_string

result = duplicate_encode("aabcdd")
print(result)