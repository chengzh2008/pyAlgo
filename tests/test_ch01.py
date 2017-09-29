# -*- coding: utf-8 -*-

import logging
import unittest

from src import ch01 as CH01

LOG = logging.getLogger(__name__)

class Ch01TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_exp1(self):
        count = 10**4
        LOG.debug("Testing %r", count)
        realcount = len(CH01.exp1(count))
        self.assertEqual(realcount, count, msg='{0}, {1}'.format(realcount, count))

    def test_exp2(self):
        count = 10**4
        LOG.debug("Testing %r", count)
        realcount = len(CH01.exp2(count))
        self.assertEqual(realcount, count, msg='{0}, {1}'.format(realcount, count))

if __name__ == '__main__':
    unittest.main()
