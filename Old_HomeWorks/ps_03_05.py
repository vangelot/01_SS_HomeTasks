'''
ps_03_05 = 3rd Homework, task #5, ps = Свалявчик П.

Напишіть код який просить ввести дві будь-які змінні, а потім міняє їх місцями.
'''

a = input("Введіть 1 змінну (a) : ")
b = input("Введіть 2 змінну (b) : ")
a, b = b, a
print("a = "+str(a)+"\nb =",b) #

x = lambda y: y*3
print(x(2))