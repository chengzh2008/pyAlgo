"""Testing for ch05"""

import logging
import random
import unittest
from copy import deepcopy

from src.ch05 import (components, dfs_topsort, iter_dfs, rec_dfs, stack1,
                      traverse)

LOG = logging.getLogger(__name__)

class Ch05TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_components(self):
        LOG.info("Testing finding connected components from a graph")
        G = {
            'a': {'b', 'c', 'd'},
            'b': {'a', 'd'},
            'c': {'a', 'd'},
            'd': {'a', 'b', 'c'},
            'e': {'f', 'g'},
            'f': {'e', 'g'},
            'g': {'e', 'f'},
            'h': {'i'},
            'i': {'h'}
        }
        real_cc1 = {'a', 'b', 'c', 'd'}
        real_cc2 = {'e', 'f', 'g'}
        real_cc3 = {'h', 'i'}
        real_cc_list = [real_cc1, real_cc2, real_cc3]

        cal_cc_list_transform = []
        cal_cc_list = components(G)
        for cc in cal_cc_list:
            s = set()
            s.update(cc)
            cal_cc_list_transform.append(s)
        self.assertEqual(cal_cc_list_transform, real_cc_list,
                         msg="calcualted components: {0} is not {1}".format(cal_cc_list_transform, real_cc_list))

    def test_iter_dfs(self):
        """test iterative dfs"""
        a, b, c, d, e, f, g, h = range(8)
        G = [
            {b:2, c:1, d:3, e:9, f:4},    # a
            {c:4, e:3},                   # b
            {d:8},                        # c
            {e:7},                        # d
            {f:5},                        # e
            {c:2, g:2, h:2},              # f
            {f:1, h:6},                   # g
            {f:9, g:8}                    # h
        ]
        l = [0, 5, 7, 6, 2, 3, 4, 1]
        self.assertEqual(list(iter_dfs(G, 0)), l)

    # TODO: why fails
    def test_general_traverse(self):
        """test general traverse"""
        a, b, c, d, e, f, g, h = range(8)
        G = [
            {b:2, c:1, d:3, e:9, f:4},    # a
            {c:4, e:3},                   # b
            {d:8},                        # c
            {e:7},                        # d
            {f:5},                        # e
            {c:2, g:2, h:2},              # f
            {f:1, h:6},                   # g
            {f:9, g:8}                    # h
        ]
        l = [0, 5, 7, 6, 2, 3, 4, 1]
        self.assertEqual(list(traverse(G, 0, stack1)), l)

    def test_dfs_topsort(self):
        G = {
            'a': {'b', 'f'},
            'b': {'c', 'd', 'f'},
            'c': {'d'},
            'd': {'e', 'f'},
            'e': {'f'},
            'f': {}
        }
        real_sort = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertEqual(real_sort, dfs_topsort(G))

if __name__ == '__main__':
    unittest.main()
