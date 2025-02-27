"""
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.

"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"

"""

string = "tasdfasdfdgc"

def get_middle(s):
    s_len = len(s)
    if s_len % 2 == 0:
        middle_chars = s[int((s_len / 2) - 1)] + s[int(s_len / 2)]
    else:
        middle_chars = s[int(s_len / 2)]
    middle_chars = str(middle_chars)
    print(middle_chars)

    return middle_chars

get_middle(string)