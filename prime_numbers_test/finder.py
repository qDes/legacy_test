import time

from math import ceil


def find_prime_simple(AIM):
    if AIM < 1:
        return None
    prime_numbers = [2]
    counter = 2
    num = 3
    while counter <= AIM:
        isprime = True
        target = ceil(num/2)+1
        for i in range(3, target, 2):
            if num % i == 0:
                isprime = False
                break
        if isprime:
            prime_numbers.append(num)
            counter += 1
        num += 2
    return prime_numbers[-1]


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    # The running integer that's checked for primeness
    q = 2
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def find_prime_thr_gen(AIM):
    if AIM < 1:
        return None
    prime_gen = gen_primes()
    for _ in range(AIM):
        prime_num = next(prime_gen)
    return prime_num


def test_func(func, aims):
    for aim in aims:
        start = time.time()
        prime = func(aim)
        exec_time = time.time() - start
        print(f"find {aim} prime numbers in {exec_time}")
        print()


def test_perfomance():
    aims_1 = [100, 1000, 10000]
    aims_2 = [1000000]
    test_func(find_prime_thr_gen, aims_1+aims_2)
    test_func(find_prime_simple, aims_1)


def main():
    pass


if __name__ == "__main__":
    main()
