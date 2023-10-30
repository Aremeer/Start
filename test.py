def duplicate_encode(word):
    word = word.lower()
    new = ""
        if word.count(char) > 1:
            new += ")"
        else:
            new += "("
    return new

word = 'hahaha'
print(duplicate_encode(word))


