"""
Task:
    You are given a list of strings.
    Sort the list in descending order based on the number of vowels in each string.
    Use sorted() with a lambda function.

Hint:
    You may use a helper inside the lambda to count vowels: 'aeiou'

Example:
    Input:
        words = ["banana", "apple", "kiwi", "grape", "orange"]
    Output:
        ['banana', 'orange', 'apple', 'grape', 'kiwi']
"""

words = ["banana", "apple", "kiwi", "grape", "orange"]


def vowel_count(w_list):
    return sorted(
        w_list, key=lambda x: sum(1 for char in x if char in "aeiou"), reverse=True
    )


result = vowel_count(words)
print(result)
