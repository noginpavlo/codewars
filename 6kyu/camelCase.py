"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

string = "camelCase"

def solution(s):
    return "".join(" " + l if l.isupper() else l for l in s)

result = solution(string)
print(result)
