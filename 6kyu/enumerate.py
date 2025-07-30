"""
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""

from collections import Counter


def duplicate_encode(s):
    s = s.lower()
    count_items = dict(Counter(s))
    print(count_items)
    result_string = "Here is a string: "
    for letter in s:
        if count_items[letter] == 1:
            result_string += "("
        else:
            result_string += ")"
    return result_string


result = duplicate_encode("recede")
print(result)
