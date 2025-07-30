"""
### **Practice Problem 1: Using `lambda` and `map()`**
Write a Python function to multiply each number in the list `[5, 10, 15, 20]`
by 2 using a `lambda` inside the `map()` function.
"""

my_list = [5, 10, 15, 20]


def multiplier(some_list):
    return list(map(lambda x: x * 2, some_list))


result = multiplier(my_list)
print(result)
