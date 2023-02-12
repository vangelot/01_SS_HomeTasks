
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("!!! Impossible to divide by 0 !!!")
        return 0
    except Exception:
        print('some other mistake')
        return 0

print(division(1, 2), '\n')
print(division(1, 0), '\n')
print(division("a", 2))
