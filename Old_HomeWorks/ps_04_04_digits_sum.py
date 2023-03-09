'''
ps_04_04 = 4th Homework, task #4, ps = Свалявчик П.

Напишіть функцію, яка приймає ціле число та повертає суму всіх його цифр.
Наприклад, 437. 4+3+7=14
'''

def sum_numbers(number):
    str_number = str(number)
    sum = 0
    while len(str_number) > 0:
        sum += int(str_number[0])
        str_number = str_number[1:]
    return sum
print(sum_numbers(1))
