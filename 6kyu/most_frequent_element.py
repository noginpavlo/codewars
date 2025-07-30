from collections import Counter


one_list = [1, 3, 2, 3, 4, 1, 3, 2, 1, 1]


def most_frequent(l):
    count = Counter(l)
    return count.most_common(1)[0][0]


print(most_frequent(one_list))  # Expected: 1
