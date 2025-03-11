from collections import Counter

def most_frequent_word(s):
    list_s = s.split(" ")
    count = Counter(list_s)
    return count.most_common(1)[0][0]

print(most_frequent_word("apple banana apple orange banana apple"))  # Expected: "apple"
print(most_frequent_word("dog cat cat dog elephant dog"))  # Expected: "dog"