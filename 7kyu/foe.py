"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []
"""

users_input = ["Ryan", "Kieran", "Jason", "Yous", "1234"]


def friend_or_foe(l):
    return [i for i in l if len(i) == 4]


result = friend_or_foe(users_input)
print(result)
