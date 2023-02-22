from randoms import list_filling
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
        if ord(word1[i]) > ord(word2[i]):
            return True
        elif ord(word1[i]) < ord(word2[i]):
            return False
    if len(word1) > len(word2):
        return True
    elif len(word1) < len(word2):
        return False
    else:
        return None


def execute():
    new_list = list_filling("word", 20)
    print(new_list)
    print(quick_sort_words(new_list))


# execute()


