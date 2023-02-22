import random


def quick_sort_words(_list):
    if len(_list) > 1:
        pivot = random.choice(_list)
        less = [x for x in _list if word1_bigger_word2(x, pivot) is False]
        greater = [x for x in _list if word1_bigger_word2(x, pivot) is True]
        equal = [x for x in _list if word1_bigger_word2(x, pivot) is None]
        return quick_sort_words(less) + equal + quick_sort_words(greater)
    else:
        return _list


def word1_bigger_word2(word1, word2):
    '''
    a > b : return True
    a < b : return False
    a = b : return None
    '''
    min_len = len(word1)
    if len(word2) < min_len:
        min_len = len(word2)
    for i in range(min_len):
        if get_key(cyr_dict, word1[i]) > get_key(cyr_dict, word2[i]):
            return True
        elif get_key(cyr_dict, word1[i]) < get_key(cyr_dict, word2[i]):
            return False
    if len(word1) > len(word2):
        return True
    elif len(word1) < len(word2):
        return False
    else:
        return None


def get_key(_dict, _value):
    for key, val in _dict.items():
        if val == _value:
            return key


def make_cyrillic_dict():
    list_of_cyrillic_symbols = ["а", "б", "в", "г", "д", "е", 'ё', "ж", "з", "и", "й", "к", "л",
                                "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч",
                                "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    cyrillic_dict = {}
    for i in range(len(list_of_cyrillic_symbols)):
        cyrillic_dict.update({i: list_of_cyrillic_symbols[i]})
    for i in range(33, 33 + len(list_of_cyrillic_symbols)):
        cyrillic_dict.update({i: list_of_cyrillic_symbols[i - 33].upper()})
    return cyrillic_dict


cyr_dict = make_cyrillic_dict()
print(cyr_dict)

words = ['Каша', "Рыба", "мясо", "олень", "Алёшка", "алежка", "молочко", "Париж", "Курица",
         "гомогей", "пионер", "путинЛох", "Стабилизаторчик", "Стабилизатор", "стоянка", "Ася",
         "Люба", "зая", "алена", "алеша", "Василий", "овсянка", "григорий", "витаминка", "ГавГав",
         "алешшш", "аорта", "словарь", "слесарь", "абрикос", "Стаб"]


print(quick_sort_words(words))



