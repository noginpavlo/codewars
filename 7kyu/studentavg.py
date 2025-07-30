"""
There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!

Note:
    Your points are not included in the array of your class's points. Do not forget them when calculating the average score!
"""

class_points = [1, 2, 3, 4, 5, 6, 7]
your_points = 1


def better_then_average(cls, you):
    return True if (sum(cls) / len(cls)) < you else False


result = better_then_average(class_points, your_points)
print(result)
