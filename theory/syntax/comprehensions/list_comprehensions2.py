"""
Task:
    You are given a list of strings.
    Convert each string to title case (first letter uppercase, the rest lowercase),
    but do this by using a custom function inside a list comprehension.

Hint:
    Define a helper function that takes a string and returns it in title case.

Example:
    Input:
        words = ["heLLo", "WorLD", "PYTHON", "coDing"]
    Output:
        ['Hello', 'World', 'Python', 'Coding']
"""

words = ["heLLo", "WorLD", "PYTHON", "coDing"]


def custom_function(word):
    return word.capitalize()


def result_function(wrds):
    return [custom_function(word) for word in wrds]


result = result_function(words)
print(result)
