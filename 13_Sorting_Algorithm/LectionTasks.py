from randoms import list_filling, sort_speed, quick_sort
import random

dict_sample = {
    1: "Йогурт",
    2: "Кефир",
    3: "Майонез",
    4: "Борщ",
    5: "Сметана",
    6: "Молоко",
    7: "Рагу",
    8: "Картофель",
    9: "Гречка",
    10: "Рис",
}


def bubble_sort(_list):
    arg = _list[:]
    for i in range(len(_list)-1, 0, -1):
        for index in range(0, i):
            if arg[index] > arg[index + 1]:
                arg[index], arg[index + 1] = arg[index + 1], arg[index]
    return arg


def word_replacement(_list):
    if len(_list) < 10:
        return _list
    else:
        replaced_indexes = []
        for key in dict_sample.keys():
            index = random.randint(0, len(_list)-1)
            while index in replaced_indexes:
                index = random.randint(0, len(_list)-1)
            _list[index] = dict_sample[key]
            replaced_indexes.append(index)
        return _list


word_list = list_filling('word', 250)
print(word_list)

print("Average time for Quick: ", sort_speed(word_list, quick_sort, 100))
print("Average time for Bubble: ", sort_speed(word_list, bubble_sort, 100))

print(word_list)
print(word_replacement(word_list))

# Проведіть сортування попередніми алгоритмами:

print(quick_sort(word_list))
print(bubble_sort(word_list))
print(word_list)    # бачимо що з таким підходом вихідний ліст не змінився !!!

print("Average time for changed list by Quick: ", sort_speed(word_list, quick_sort, 100))
print("Average time for changed list by Bubble: ", sort_speed(word_list, bubble_sort, 100))


