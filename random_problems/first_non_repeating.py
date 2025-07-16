from collections import Counter

"""
Description:
Write a function first_unique_char(s: str) -> int that takes a non-empty
string s and returns the index of the first non-repeating character.
If every character repeats, return -1.

first_non_repeating("leetcode")   # Returns 0 (since 'l' is unique)
first_non_repeating("loveleetcode")  # Returns 2 (first unique is 'v')
first_non_repeating("aabb")      # Returns -1 (no unique characters)
"""

my_string = "some string that is not neccesserily a good string to try but it is long"


def first_non_repeating(string: str) -> int:
    counter = Counter(string)
    for elm in string:
        if counter[elm] == 1:
            return string.index(elm)
    return -1


print(first_non_repeating(my_string))
