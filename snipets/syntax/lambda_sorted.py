"""
Task:
    You are given a list of tuples where each tuple contains a name and an age.
    Sort the list in ascending order based on the age using sorted() with a lambda function.

Example:
    Input:
        people = [("Alice", 30), ("Bob", 25), ("Eve", 35)]
    Output:
        [('Bob', 25), ('Alice', 30), ('Eve', 35)]
"""

people = [("Alice", 30), ("Bob", 25), ("Eve", 35)]
 
def age_sorting(ppl_list):
    return list(sorted(ppl_list, key=lambda x : x[1]))


result = age_sorting(people)
print(result)

