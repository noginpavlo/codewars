"""
Task:
    Given a list of strings, return a new list that contains:
        - The uppercase version of each string only if the string has more than 3 characters
        - Otherwise, return the string unchanged
    Use a list comprehension.

Example:
    Input:
        words = ["hi", "hello", "yo", "python", "ok"]
    Output:
        ['hi', 'HELLO', 'yo', 'PYTHON', 'ok']
"""

words = ["hi", "hello", "yo", "python", "ok"]
 
def word_changer(words):
    return [word.upper() if len(word) > 3 else word for word in words]

result = word_changer(words)
print(result)
