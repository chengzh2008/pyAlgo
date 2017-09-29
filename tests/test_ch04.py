"""Testing for ch04"""

import logging
import unittest

from src.ch04 import cover, print_board

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

if __name__ == '__main__':
    unittest.main()
