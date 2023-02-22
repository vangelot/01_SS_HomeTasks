from multiprocessing import Pool
import os
import time
import threading

results = []


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += 1
    results.append(result)


def count_cores():
    return os.cpu_count()


def sequence_root(x):
    return x**0.5


def by_multiprocessing():
    print(count_cores())
    with Pool(processes=3) as pool:
        started_at = time.time()
        for i in range(10):
            pool.map(sequence_root, range(1, 1000000))
        print(f"Time used: {(time.time()-started_at)/10}")
        # 1 core = 0.27 sec
        # 3 core = 0.11 sec
        # 16 core = 0.087 sec


def by_nothing():
    started_at = time.time()
    for i in range(10):
        for j in range(1, 1000000):
            sequence_root(j)
    print(f"Time used: {(time.time() - started_at)/10}")
    # Time = 0.17 sec


def by_threading():
    global results
    task1 = threading.Thread(
        target=handler,
        kwargs={"started": 2 ** 15}
    )
    task2 = threading.Thread(
        target=handler,
        kwargs={"started": 2 ** 15, "finished": 2**27}
    )
    started_at = time.time()
    task1.start()
    task2.start()

    task1.join()
    task2.join()
    print("Result 1:")
    print(f"Time: {time.time() - started_at}")
    print("Value: ", sum(results))

    results = []
    started_at = time.time()
    handler(finished=2 ** 27)
    print("Result 2:")
    print(f"Time: {time.time() - started_at}")
    print("Value: ", sum(results))
    pass


if __name__ == '__main__':
    # by_multiprocessing()
    by_nothing()
    # by_threading()
    # handler(1, 10)
    pass

# print(time.time())

