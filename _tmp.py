while True:
    try:
        a = int(float(input('enter smth: ')))
        break
    except Exception as ex:
        print('wrong')
        print(str(ex))

print(int(10.5))
print(int(True))

b = int(10.5)
print(b)