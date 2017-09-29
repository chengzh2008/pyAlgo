"""Testing for ch02"""

import logging
import unittest

from src.ch02 import Bunch, MTree, Node, Tree

LOG = logging.getLogger(__name__)

class Ch02TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_node(self):
        LOG.debug("Testing Node implementation")
        node = Node("a", Node("b", Node("c", Node("d"))))

        value = "c"
        realvalue = node.next.next.value
        self.assertEqual(realvalue, value, msg='{0}, {1}'.format(realvalue, value))

    def test_adjacency_set_graph(self):
        a, b, c, d, e, f, g, h = range(8)
        N = [
            {b, c, d, e, f}, #a
            {c, e},
            {d},
            {e},
            {f},
            {c, g, h},
            {f, h},
            {f, g}
        ]
        self.assertEqual(b in N[a], True, msg="{0}, {1}".format("is b in N[a]", b in N[a]))

    def test_adjacency_dict_graph(self):
        a, b, c, d, e, f, g, h = range(8)
        N = [
            {b:2, c:1, d:3, e:9, f:4},    # a
            {c:4, e:3},                   # b
            {d:8},                        # c
            {e:7},                        # d
            {f:5},                        # e
            {c:2, g:2, h:2},              # f
            {f:1, h:6},                   # g
            {f:9, g:8}                    # h
        ]
        self.assertEqual(N[a][b], 2, msg="{0}, {1}".format("weight of edge a b", N[a][b]))

    def test_weight_matrix_graph(self):
        a, b, c, d, e, f, g, h = range(8)
        inf = float('inf')

        #       a    b    c    d    e    f    g    h

        W = [
            [  0,   2,   1,   3,   9,   4, inf, inf], # a
            [inf,   0,   4, inf,   3, inf, inf, inf], # b
            [inf, inf,   0,   8, inf, inf, inf, inf], # c
            [inf, inf, inf,   0,   7, inf, inf, inf], # d
            [inf, inf, inf, inf,   0,   5, inf, inf], # e
            [inf, inf,   2, inf, inf,   0,   2,   2], # f
            [inf, inf, inf, inf, inf,   1,   0,   6], # g
            [inf, inf, inf, inf, inf,   9,   8,   0]
        ] # h
        self.assertEqual(W[a][b] < inf, True, msg="{0}, {1}".format("weight of edge a b less than inf", W[a][b]))
        self.assertEqual(W[c][e] < inf, False, msg="{0}, {1}".format("weight of edge a b less than inf", W[c][e]))
        degree_node_a = sum(1 for w in W[a] if w < inf and w != 0)
        self.assertEqual(degree_node_a, 5, msg="{0}, {1}".format("degree of node a", degree_node_a))

    def test_tree_list_of_lists(self):
        T = [["a", "b"], ["c"], ["d", ["e", "f"]]]
        self.assertEqual(T[0][1], "b", msg="{0}, {1}".format("right child of the left child is", T[0][1]))

    def test_binary_tree(self):
        T = Tree(None, Tree("c", "d"))
        self.assertEqual(T.left, None)
        self.assertEqual(T.right.left, "c")

    def test_multi_way_tree(self):
        T = MTree(MTree("a", MTree("b", MTree("c", MTree("d")))))
        self.assertEqual(T.kids.next.next.kids, "c")
        self.assertEqual(T.kids.next.next.val, "c")

    def test_bunch_pattern(self):
        b = Bunch(name="abc", address="1st street")
        self.assertEqual(b.name, "abc")
        self.assertEqual(b.address, "1st street")
        self.assertEqual("name" in b, True)
        self.assertEqual("address" in b, True)

if __name__ == '__main__':
    unittest.main()
