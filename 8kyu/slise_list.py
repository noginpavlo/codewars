"""
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
"""

my_list = [1,2,3,4,5,6,7,8,9,10]

def remove_every_other(l):
    l = l[::2] #slise every second element.
    print(l)
    return l

remove_every_other(my_list)