"""
Problem 2: Palindrome Check
Write a function that checks if a given string is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example:
is_palindrome("A man a plan a canal Panama")  # should return True
is_palindrome("racecar")  # should return True
is_palindrome("hello")  # should return False
"""

variable = "A man a plan a canal Panama"


def is_palindrome(s):
    s_purified = s.replace(" ", "").lower()
    return s_purified == s_purified[::-1]


result = is_palindrome(variable)
print(result)
