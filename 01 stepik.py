import first
#Есть list объектов objects: посчитать к-во неповторяемых элементов
objects = [1, 2 ,3, 3, 1, 1]
ans = 0
res = []
while len(objects) > 0: # доступная переменная objects
    res.append(objects[0])
    a = objects[0]
    while a in objects:
        objects.remove(a)
print(len(res))
