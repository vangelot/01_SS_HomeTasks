def unique_in_order(iterable):
    i = 1
    res = []
    res.append(iterable[0])
    while i < len(iterable):
        if iterable[i] == res[-1]:
            i += 1
        else:
            res.append(iterable[i])
        if i < len(iterable)-1:
            while iterable[i] == iterable[i+1]:
                i += 1
                if i == len(iterable)-1:
                    break
    return res
print(unique_in_order('AAAABBBCCDAABBB'))