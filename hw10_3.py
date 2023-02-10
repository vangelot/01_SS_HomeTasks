import string


class NameErrorLanguage(Exception):
    def __init__(self, wrong_name):
        print(wrong_name, ' includes wrong letters')


class NameErrorRespect(Exception):
    def __init__(self, wrong_name):
        print(wrong_name, ' should begin with Uppercase')


try:
    name = input("enter name: ")
    smash_name = set(name)
    if name[0] not in string.ascii_uppercase:
        raise NameErrorRespect(name)
    for letter in smash_name:
        if letter not in (string.ascii_letters + '-'):
            raise NameErrorLanguage(name)
    print("Nice name, ",name)
except NameErrorLanguage:
    print("ERROR !!!")
except NameErrorRespect:
    print("ERROR !!!")
except Exception:
    print("Name is empy \n ERROR !!!")

# print(string.ascii_letters+'-')
