"""
Write a function to check if two strings are anagrams.
Two strings are anagrams if they contain the same characters with the same frequency,
but possibly in a different order.

Example:
are_anagrams("listen", "silent")  # should return True
are_anagrams("hello", "world")    # should return False
"""

string1 = "aaaadzdd"
string2 = "ddddaaaa"

def are_anagrams(a, b):
    return sorted(a) == sorted(b)

result = are_anagrams("listen", "silent")
print(result)