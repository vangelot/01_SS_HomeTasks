'''
ps_03_03 = 3rd Homework, task #3, ps = Свалявчик П.

Напишіть цикл for, який просить ввести ціле число 10 разів, а потім роздруковує
у консолі суму всіх введених чисел
'''

list_of_numbers = []
sum = 0
for i in range(10):
    list_of_numbers.append(int(input("Введіть " + str(i+1) + " число : ")))
    sum += list_of_numbers[i]
# print(list_of_numbers) # перевірка
print('Sum is ' + str(sum))
