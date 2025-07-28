"""
The problem is to write a function `is_palindrome(s)` that returns True if the input
string `s` is a palindrome (reads the same forwards and backwards), and False otherwise.

Ignore case and non-alphanumeric characters.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True
"""


def is_palindrome(string: str) -> bool:
    filtered = ''.join(char.lower() for char in string if char.isalnum())
    return filtered == filtered[::-1]


result = is_palindrome("A man, a plan, a canal: Panama")
print(result)
