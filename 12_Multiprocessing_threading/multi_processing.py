from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# з рекурсією не працює
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x*factorial(x-1)


def factor(x):
    if x == 0:
        return 0
    res = 1
    for i in range(1, x+1):
        res = res * i
    return res


def sequence_root(x):
    return x**0.5


def thread_execution(n):
    started_at = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(factor, i) for i in range(n)]
    res_thread = [future.result() for future in futures]
    # print(res_thread)
    time_thread = time.time() - started_at
    return time_thread


def process_execution(n):
    started_at = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(factor, i) for i in range(n)]
    res_process = [future.result() for future in futures]
    # print(res_process)
    time_thread = time.time() - started_at
    return time_thread


if __name__ == '__main__':
    examples1 = 100
    examples2 = 3000

    a = thread_execution(examples1)
    b = process_execution(examples1)
    print(f"for examples {examples1} result is:")
    if a > b:
        print(f"ProcessPoolExecutor faster x{a / b} times")
    else:
        print(f"ThreadPoolExecutor faster x{b / a} times\n")

    a = thread_execution(examples2)
    b = process_execution(examples2)
    print(f"for examples {examples2} result is:")
    if a > b:
        print(f"ProcessPoolExecutor faster x{a / b} times")
    else:
        print(f"ThreadPoolExecutor faster x{b / a} times")



