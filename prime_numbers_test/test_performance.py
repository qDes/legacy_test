import time

from finder import find_prime_simple, find_prime_thr_gen


def test_time_func(func, aims):
    for aim in aims:
        start = time.time()
        prime = func(aim)
        exec_time = time.time() - start
        print(f"find {aim} prime numbers in {exec_time}")
        print()


def test_performance():
    aims_1 = [100, 1000, 10000]
    aims_2 = [1000000]
    test_time_func(find_prime_thr_gen, aims_1+aims_2)
    test_time_func(find_prime_simple, aims_1)


if __name__ == "__main__":
    test_performance()
