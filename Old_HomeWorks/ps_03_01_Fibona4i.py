'''
ps_03_01 = 3rd Homework, task #1, ps = Свалявчик П.

За допомогою нескінченного циклу згенеруйте ряд чисел Фібоначчі.
Ряд починається з чисел 1, 1, 2, 3, 5, 8, 13, а кожен наступний елемент -
це сума двох попередніх
'''

last = 1
previous = 1
print(last)
print(previous)

while True:
    last, previous = previous + last, last
    print(last)