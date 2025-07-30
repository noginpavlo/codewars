"""
Given an integer, determine whether it is a palindrome.
An integer is a palindrome if it reads the same forward and backward.

Example:
is_palindrome_number(121)  # should return True
is_palindrome_number(-121)  # should return False
is_palindrome_number(10)  # should return False
"""


def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(is_palindrome(121))
