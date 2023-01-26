def average(numbers):
    # повертає середнє арифметичне елементів списку
    sum = 0
    for i in numbers:
        sum += i
    return sum/len(numbers)

print(average([1, 8, 5, 4, 12]))
