"""
Write a function that takes a string and returns the first non-repeating character.
If all characters repeat, return None.

Example:
first_unique_char("aabccdeff")  # Expected output: 'b'
first_unique_char("aabbcc")     # Expected output: None
first_unique_char("abcdef")     # Expected output: 'a'
"""
from collections import Counter


def first_unique_char(s):
    count = Counter(s)
    for char in count:
        if count[char] == 1:
            return char
    return None

print(first_unique_char("aabbcc"))