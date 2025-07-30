"""
Write a function that takes a sentence as input and returns the longest word in the sentence.
If there are multiple words with the same length, return the first one.

Example:
find_longest_word("The quick brown fox jumped over the lazy dog")  # should return "jumped"
find_longest_word("I love programming")  # should return "programming"
"""

string = "The quick brown fox jumped over the lazy dog"


def find_longest(s):
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word


print(find_longest(string))
