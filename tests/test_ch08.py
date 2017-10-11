"""Testing for ch06"""

import logging
import random
import unittest
from functools import wraps
from heapq import heapify, heappop, heappush
from itertools import combinations, count

LOG = logging.getLogger(__name__)

####################################################
def naive_lis(seq):
    """naive implementation of longest increase subsequence
    basicall it get all possible subsequence combinations, then test if one of them is sorted
    """
    for length in range(len(seq), 0, -1): # from n, n-1, ..., 1
        for sub in combinations(seq, length): # subsequence of given length
            sub_list = list(sub)
            if sub_list == sorted(sub): # check if sorted
                return sub_list

####################################################
def memo(fn):
    """convert fn to a memoization one
    run in the iPython
    fib = memo(fib)
    fib(100) returns 573147844013817084101L quickly
    """
    cache = {}
    @wraps(fn)
    def wrap(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrap
####################################################
@memo
def fib(i):
    """naive_recursive version"""
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)

####################################################
@memo
def C(n, k):
    """pascal triangle"""
    if k == 0:
        return 1
    if n == 0:
        return 0
    return C(n-1, k-1) + C(n-1, k)



####################################################
class Ch08TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_naive_lis(self):
        """test naive longest increase subsequence"""
        input_list = [3, 1, 0, 2, 4]
        output_list = [1, 2, 4]
        self.assertEqual(naive_lis(input_list), output_list)

    def test_fib(self):
        """test fib"""
        self.assertEqual(fib(100), 573147844013817084101L)

    def test_pascal_triangle(self):
        """test parscal triangle"""
        self.assertEqual(C(100, 50), 100891344545564193334812497256)


if __name__ == '__main__':
    unittest.main()
