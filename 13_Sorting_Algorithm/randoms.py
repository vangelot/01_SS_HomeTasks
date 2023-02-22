import random
import time
from random_words import RandomWords


def sort_speed(_list, sort_func, iteration_number=1):
    start = time.time()
    for i in range(iteration_number):
        sort_func(_list)
    return (time.time()-start) / iteration_number


def quick_sort(_list):
    if len(_list) > 1:
        pivot = random.choice(_list)
        less = [x for x in _list if x < pivot]
        greater = [x for x in _list if x > pivot]
        equal = [x for x in _list if x == pivot]
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return _list


def list_filling(_type="int", quantity=1):
    _list = []
    if quantity < 1 or type(quantity) != int:
        print("!!! Wrong quantity !!!")
        return _list
    if _type == "int":
        for index in range(quantity):
            _list.append(random.randint(0, 1000))
    elif _type == "float":
        for index in range(quantity):
            _list.append(random.uniform(0.1, 100))
    elif _type == "word":
        w = RandomWords()
        for index in range(quantity):
            _list.append(w.random_word())
    else:
        print("!!! Wrong type !!!")
    return _list


def home_task():

    # creating lists
    int_list = list_filling("int", 5000)
    float_list = list_filling("float", 5000)
    str_list = list_filling("word", 5000)

    # mistakes
    print(list_filling("xxx", 5000))
    print(list_filling("int", 0))

    # function output example
    new_list = list_filling("word", 10)
    print(new_list)
    print(quick_sort(new_list))

    print("Average time is: ", sort_speed(str_list, quick_sort, 20), 'seconds')


# home_task()

