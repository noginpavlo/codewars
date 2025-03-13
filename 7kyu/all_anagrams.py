"""
You are given a list of strings. Write a function to group the strings that are anagrams of each other

Example:
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# Expected output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""

def group_anagrams(l):
    for i in l:
        print(f"{i}, {i[::-1]}")
    return [item for item in l if item == item[::-1]]

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))