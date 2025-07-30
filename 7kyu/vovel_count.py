def get_count(sentence):
    return len([letter for letter in sentence if letter in ["a", "e", "i", "o", "u"]])


count = get_count("count vovels in this sentence")
print(count)
