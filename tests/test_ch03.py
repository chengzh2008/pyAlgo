"""Testing for ch03"""

import logging
import random
import unittest
from copy import deepcopy

from src.ch03 import is_prime, merge_sort, rec_cost_sum, rec_sum

LOG = logging.getLogger(__name__)

class Ch03TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_is_prime(self):
        LOG.info("Testing is_prime")
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)

    def test_sum_and_cost(self):
        LOG.info("Testing operation and cost")
        seq = range(1, 101)
        self.assertEqual(rec_sum(seq), 5050)
        self.assertEqual(rec_cost_sum(seq), 101)

    def test_merge_sort(self):
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), merge_sort(seq1))

if __name__ == '__main__':
    unittest.main()
