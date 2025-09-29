"""
->Binary search takes sorted list of elements as input. It needs to be sorted.
->It returns an index of the searched element or None.

=> The idea of the algorithm is to choose a value exactly in the middle of the array and
ask an conditional questtion about the searched value: is it bigger or smaller the the mid number?
If bigger then the searched value is on the left,
if smaller -- on the right.

Initial List:
Index:       0   1   2   3   4   5   6   7   8   9   10
           [ 1 | 3 | 5 | 7 | 9 |11 |13 |15 |17 |19 |21 ]
                          ↑
                       mid=5 (11)
                       13 > 11 → search right

----------------------------------------------------------------

Right Half:
Index:              6   7   8   9   10
                  [ 13 |15 |17 |19 |21 ]
                            ↑
                         mid=8 (17)
                         13 < 17 → search left

----------------------------------------------------------------

Left of Right Half:
Index:           6   7
              [ 13 |15 ]
                 ↑
            mid=6 (13)
      ✅ Found 13 at index 6!
"""

"""
BS Big O complexity is log2(n),
    where n is a length of an array.
"""


my_list = list(range(1, 101))


def binary_search(int_list: list[int], searched_int: int) -> int | None:
    start = 0
    end = len(int_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if int_list[mid] == searched_int:
            return mid
        if int_list[mid] < searched_int:
            start = mid + 1
        else:
            end = mid - 1

    return None


RESULT = binary_search(my_list, 9)
print(RESULT)


"""
Question 1:

Suppose you have a sorted list of 128 names, and you’re searching
through it using binary search. What’s the maximum number of
steps it would take?

BS complexity is O(log2(n)),
=> n_steps = log2(128) = 7

RESPONSE: it takes 7 steps to search through 128 names.

Question2:

Suppose you double the size of the list. What’s the maximum
number of steps now?

not it is:
n_steps = log2(256) = 8

RESPONSE: 8 steps
"""
