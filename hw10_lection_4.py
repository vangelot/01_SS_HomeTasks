def square():
    a = input("Input side 1: ")
    b = input("Input side 2: ")
    try:
        a, b = float(a), float(b)
        if a<0 or b<0:
            raise Exception("side couldn't be < 0")
        return a*b
    except Exception as ex:
        print(ex, " wrong input")
        return 0
    pass

print(square())

