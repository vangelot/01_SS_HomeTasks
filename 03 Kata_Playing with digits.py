def dig_pow(n, p):
    # your code
    n_string = str(n)
    polinom = 0
    for i in range(len(n_string)):
        polinom += int(n_string[i])**(p+i)
    # print(polinom)
    if (polinom % n) == 0:
        return polinom // n
    return -1
print(dig_pow(695,2))