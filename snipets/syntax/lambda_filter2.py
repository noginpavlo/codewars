"""
Task:
    You are given a list of strings.
    Use filter() with a lambda function to return a new list containing only the strings that have more than 3 characters and start with a vowel (a, e, i, o, u).

Example:
    Input:
        words = ["apple", "banana", "pear", "kiwi", "ki", "orange"]
    Output:
        ['apple', 'orange']
"""

words = ["apple", "banana", "pear", "kiwi", "ki", "orange"]

def say(words_l):
    return list(filter(lambda word : word[0] in ["a", "e", "i", "o", "u"] and len(word) > 3, words_l))

result = say(words)
print(result)

