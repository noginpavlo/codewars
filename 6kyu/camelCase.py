"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

string = "camelCase"

def solution(s):
    new_s = ""
    for d in s:
        if d.isupper():
            new_s += " " + d
        else:
            new_s += d
    return new_s

result = solution(string)
print(result)