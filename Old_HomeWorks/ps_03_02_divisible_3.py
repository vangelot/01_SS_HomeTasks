'''
ps_03_03 = 3rd Homework, task #2, ps = Свалявчик П.

Створіть список, що містить числа від 0 до 100 та за допомогою List Comprehension
отримайте з нього список чисел, що кратні 3.
'''

list_of_numbers = []

for i in range(101):
    # створення списку
    list_of_numbers.append(i)
# print(list_of_numbers) # - перевірка коректності створення списку

list_divisible_3 = [i for i in list_of_numbers if i % 3 == 0]

print(list_divisible_3)