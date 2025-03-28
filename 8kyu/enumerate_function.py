def capitals(word):
    return [index for index, letter in enumerate(word) if letter.isupper()]

result = capitals("something LIKE That")
print(result)