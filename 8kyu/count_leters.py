"""
Create a function that accepts a string and a single character,
and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", 'o')  =>  1
("Hello", 'l')  =>  2
("", 'z')       =>  0
"""

my_string = "aaaaaaaaacccttttcacacacacact"
my_letter = "t"

def letter_count(s, l):
    n = 0
    for i in s:
        if i == l:
            n += 1
    print(n)

letter_count(my_string, my_letter)