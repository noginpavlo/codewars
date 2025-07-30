"""
### **Practice Problem: Using `lambda` and `filter()`**
Write a Python function that filters out all the even numbers from a
given list using a `lambda` inside the `filter()` function.

Example Input:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Expected Output:
    [1, 3, 5, 7, 9]
"""

n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_evens(some_list):
    return list(filter(lambda x: x % 2 == 0, some_list))


result = get_evens(n_list)
print(result)
