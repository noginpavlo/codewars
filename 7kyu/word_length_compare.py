"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

string = "I have to go outside to breathe some air now"

def find_short(s):
    word_list = s.split(" ")
    first_w_length = len(word_list[0])
    for w in word_list[1:]:
        if len(w) < first_w_length:
            first_w_length = len(w)
    return first_w_length

result = find_short(string)
print(result)