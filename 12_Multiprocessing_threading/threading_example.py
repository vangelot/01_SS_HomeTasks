import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def worker1():
    print('Рабочий 1 попытается захватить lock1')
    with lock1:
        print('Рабочий 1 захватил lock1')
        print('Рабочий 1 попытается захватить lock2')
        with lock2:
            print('Рабочий 1 захватил lock2')
    print('Рабочий 1 освободил lock2')
    print('Рабочий 1 освободил lock1')

def worker2():
    print('Рабочий 2 попытается захватить lock2')
    with lock2:
        print('Рабочий 2 захватил lock2')
        print('Рабочий 2 попытается захватить lock1')
        with lock1:
            print('Рабочий 2 захватил lock1')
    print('Рабочий 2 освободил lock1')
    print('Рабочий 2 освободил lock2')

# Создание объектов потоков
thread1 = threading.Thread(target=worker1)
thread2 = threading.Thread(target=worker2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
