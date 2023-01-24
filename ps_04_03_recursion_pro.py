def is_polindrom(word):
    if (len(word) == 1) or (len(word) == 0):
        return True
    while len(word) > 1:
        if word[0] == word[-1]:
            return is_polindrom(word[1:-1])
        else:
            return False
print(is_polindrom('b'))