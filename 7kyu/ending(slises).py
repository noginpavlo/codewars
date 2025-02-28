"""
Complete the solution so that it returns true
 f the first argument(string) passed in ends with the 2nd argument (also a string).
Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""

txt = "abc"
end = "bc"

def solution(text, ending):
    return ending == text[-len(ending):]

result = solution(txt, end)
print(result)