
b = [set() for i in range(5)]
print(b)

q = {0, 1, 2}
print(q)
q.add(2)
print(q)

seen = [1] * 45
print(seen)

def func():
    print('hello')
    a = 6
    print(a)
    return 1

q = func()
print('q=',q)

_list = [1, 2, 3]

print(len(_list))

print(str(_list)+'asdf')

p = (1, None)
if p[0]:
    print('DA')