"""Testing for ch04"""

import logging
import random
import unittest
from copy import deepcopy

from src.ch04 import cover, ins_sort_iter, ins_sort_rec, print_board

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
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), ins_sort_rec(seq1, len(seq1) - 1))

    def test_iter_ins_sort(self):
        seq = [random.randrange(1000) for i in range(100)]
        seq1 = deepcopy(seq)
        self.assertEqual(sorted(seq), ins_sort_iter(seq1))

if __name__ == '__main__':
    unittest.main()
