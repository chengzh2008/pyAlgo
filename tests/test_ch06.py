"""Testing for ch06"""

import logging
import random
import unittest
from bisect import bisect, bisect_left
from copy import deepcopy

from src.ch06 import bisect_right_1, divide_and_conquer

LOG = logging.getLogger(__name__)

class Ch06TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_bisect(self):
        LOG.info("Testing bisect module")
        a = [0, 2, 3, 5, 6, 8, 8, 9]
        self.assertEqual(bisect(a, 5), 4)
        self.assertEqual(bisect(a, 4), 3)
        self.assertEqual(bisect_left(a, 4), 3)
        self.assertEqual(bisect_left(a, 3), 2)

        # test bisect_right_1
        self.assertEqual(bisect_right_1(a, 5), 4)
        self.assertEqual(bisect_right_1(a, 4), 3)

    def test_dsu_pattern(self):
        LOG.info("testing 'decorate, sort/search, undecorate' pattern")
        seq = "I aim to misbehave".split()
        dec = sorted((len(x), x) for x in seq)
        keys = [k for (k, v) in dec]
        vals = [v for (k, v) in dec]
        print dec, keys, vals
        self.assertEqual(vals[bisect_left(keys, 3)], 'aim')

if __name__ == '__main__':
    unittest.main()
