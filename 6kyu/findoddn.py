from collections import Counter

"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time
(which is odd).
"""


def find_odd(seq):
    return [n for n, count in Counter(seq).items() if count % 2 != 0][0]


result = find_odd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
print(result)

"""
Note that the solution you came up with iterates all numbers, when it is actually needs
just the first odd number. Then after all numbers are counted in a list you select the one.

This is actually much better:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

This way the iteration stops as soon as you hit the first odd number. You know from the 
problem description that there is only one odd number.
"""
