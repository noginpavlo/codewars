"""
BUBBLE SORT ALGORITHM

!!!This is mainly educational algorithm and you should use QUICK SORT or INSERT SORT for interviews.

This algorithm sorting an array of elements.

The algorytmd does this:
>>> 1. Compare the last two elements.
>>> 2. If the first is greater than the second, swap them.
>>> 3. Move to the next pair, repeat.
>>> 4. After the first iteration, the largest element is at the end.
>>> 5. Repeat the process for the remaining elements.
"""

"""
You are given a list of students' scores on a test. Use Bubble Sort to sort
the scores in descending order (highest score first),
and then print out the top 3 scores.
"""


student_scores = [88, 95, 70, 100, 65, 77, 92]


def bubble_sort(some_list: list[int]) -> list[int]:
    len_l = len(some_list)
    for i in range(len_l):
        for j in range(len_l - i - 1):
            if some_list[j] < some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
    return some_list


sorted_scores = bubble_sort(student_scores)
print(sorted_scores)
print(sorted_scores[0])
print(sorted_scores[1])
print(sorted_scores[2])
