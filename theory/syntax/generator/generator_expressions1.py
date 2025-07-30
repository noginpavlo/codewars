"""
Task:
    You are given a list of strings.
    Find the length of the longest word that starts with a vowel.

Hint:
    Use a generator expression inside the max() function.

Example:
    Input:
        words = ["apple", "banana", "orange", "umbrella", "grape", "egg"]
    Output:
        8  # "umbrella"
"""

words = ["apple", "banana", "orange", "umbrella", "grape", "egg"]


def longest(wrds):
    return max(len(word) for word in wrds if word[0] in ["a", "e", "o", "u", "y"])


result = longest(words)
print(result)
