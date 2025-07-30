"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:
1	0001
2	0010
3	0011
4	0100
5	0101
6	0110
7	0111
8	1000
9	1001
10	1010
"""

my_list = [1, 1, 1, 1]


def converter(l):
    return (l[0] * 2**3) + (l[1] * 2**2) + (l[2] * 2**1) + (l[3] * 2**0)


result = converter(my_list)
print(result)
