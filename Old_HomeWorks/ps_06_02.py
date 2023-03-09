import sys
from math import sqrt

def reducer(n):
    while n > 0:
        n = n - 1
        print(n)
        return reducer(n)

try:
    n = int(input("Input natural number: "))
    sqrt(n-1) #геніальне рішення перевірки на те що n >= 1
    #щоб запихнути в один try без додаткових перевірок
except:
    print("\n\033[38;2;255;160;122m WRONG INPUT!!! \033[0;0m")
    sys.exit()

# print('dsdf')

reducer(n)