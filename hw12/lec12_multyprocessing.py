import os
import time
from multiprocessing import Pool


def f(x):
    return x*x


def f_gen(x):
    yield x*x


if __name__ == '__main__':
    cpu = os.cpu_count()
    print(f"Your PC has {cpu} cores.")
    with Pool(cpu) as p:
        started_at = time.time()
        print(p.map(f, range(1, 100000)))
        print(f'Time: {time.time() - started_at}')

