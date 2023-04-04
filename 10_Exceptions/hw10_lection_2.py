def element_catch(list, index):
    try:
        return list[index]
    except IndexError:
        print("!!! no such INDEX !!!")
        return -1

print(element_catch([1, 2], 2),'\n')
print(element_catch([1, 2, 3], 2))
