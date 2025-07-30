"""
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
"""

array = [
    "Keep",
    "Remove",
    "Keep",
    "Remove",
    "Keep",
    "Keep",
    "Remove",
    "Keep",
    "Remove",
    "Keep",
]


def remove(a):
    print(a)
    for i in a:
        if i == "Remove":
            a.remove(i)
    print(a)
    return


remove(array)
