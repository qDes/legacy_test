import unittest

from finder import find_prime_simple, find_prime_thr_gen


class TestPrimeNumbers(unittest.TestCase):
    def test_5th(self):
        assert find_prime_simple(5) == 11
        assert find_prime_thr_gen(5) == 11
    def test_10k(self):
        assert find_prime_simple(10000) == 104729
        assert find_prime_thr_gen(10000) == 104729
    def test_none(self):
        assert find_prime_simple(0) is None
        assert find_prime_thr_gen(0) is None


if __name__ == '__main__':
    unittest.main()
