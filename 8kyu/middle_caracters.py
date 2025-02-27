"""
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.

"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"

"""

string = "tasasdfasdfasdfxfdgc"

def get_middle(s):
    index, odd = divmod(len(s), 2)
    result = s[index] if odd == 1 else s[index - 1:index + 1]
    print(result)
    return result

get_middle(string)