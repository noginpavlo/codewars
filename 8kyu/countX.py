"""

Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

ss = "xo"

def xo(s):
    xs = 0
    os = 0
    for i in s:
        if i.lower() == "x":
            xs += 1
        elif i.lower() == "o":
            os += 1
    return True if xs == os else False

result = xo(ss)
print(result)