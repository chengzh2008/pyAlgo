"""Testing for ch04"""

import logging
import random
import unittest
from copy import deepcopy

from src.ch04 import (celebrity, counting_sort, cover, ins_sort_iter,
                      ins_sort_rec, max_permutation, naive_max_permutation,
                      naive_top_sort, print_board, sel_sort_iter, sel_sort_rec,
                      top_sort)

LOG = logging.getLogger(__name__)

class Ch04TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_board_cover(self):
        LOG.info("Testing cover for a board without a corner")
        board = [[0] * 8 for i in range(8)] # 8 x 8 board
        board[7][7] = -1 # lower right is the missing piece
        cover(board)
        print_board(board)
        self.assertEqual(board[0][0], 3)
        self.assertEqual(board[7][0], 15)

    def test_rec_ins_sort(self):
        LOG.info("Testing recursive insertion sort")
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), ins_sort_rec(seq1, len(seq1) - 1))

    def test_iter_ins_sort(self):
        LOG.info("Testing iterative insertion sort")
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), ins_sort_iter(seq1))

    def test_rec_sel_sort(self):
        LOG.info("Testing recursive selection sort")
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), sel_sort_rec(seq1, len(seq1) - 1))

    def test_iter_sel_sort(self):
        LOG.info("Testing iterative selection sort")
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), sel_sort_iter(seq1))

    def test_naive_max_perm(self):
        M = [2, 2, 0, 5, 3, 5, 7, 4]
        max_perm = {0, 2, 5}
        real_result = naive_max_permutation(M)
        self.assertEqual(real_result, max_perm, msg="{0} is not {1}".format(real_result, max_perm))

    def test_max_perm(self):
        M = [2, 2, 0, 5, 3, 5, 7, 4]
        max_perm = {0, 2, 5}
        real_result = max_permutation(M)
        self.assertEqual(real_result, max_perm, msg="{0} is not {1}".format(real_result, max_perm))

    def test_counting_sort(self):
        LOG.info("Testing counting sort")
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), counting_sort(seq1))

    def test_celebrity(self):
        """
        n = 100
        G = [[random.randrange(2) for i in range(n)] for i in range(n)]
        c = random.randrange(100) # choose a celebrity
        for i in range(n): # make sure c does not know anyone else
            G[i][c] = True # and anyone does know c
            G[c][i] = False
        found = celebrity(G)
        self.assertEqual(c, found, msg="real celebrity {0}: the one found is {1} ".format(c, found))
        """

    def test_naive_top_sort(self):
        G = {
            'a': {'b', 'f'},
            'b': {'c', 'd', 'f'},
            'c': {'d'},
            'd': {'e', 'f'},
            'e': {'f'},
            'f': {}
        }
        real_sort = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertEqual(real_sort, top_sort(G))
        self.assertEqual(naive_top_sort(G), top_sort(G))


if __name__ == '__main__':
    unittest.main()
