"""
Task:
    You are given a list of strings that represent numerical values.
    Use map() with a lambda function to convert each string into its integer equivalent.

Example:
    Input:
        strings = ["1", "2", "3", "4", "5"]
    Output:
        [1, 2, 3, 4, 5]
"""

strings = ["1", "2", "3", "4", "5"]

def convert(str_l):
    return list(map(lambda x: int(x), str_l))


result = convert(strings)
print(result)

