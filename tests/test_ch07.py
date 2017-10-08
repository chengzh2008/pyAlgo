"""Testing for ch06"""

import logging
import random
import unittest
from heapq import heapify, heappop, heappush
from itertools import count

LOG = logging.getLogger(__name__)

####################################################
def huffman_trees(seq, frq):
    """huffman encoding, seq, frq are lists"""
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    LOG.info("trees: {0}".format(trees))
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a, b]))
    return trees[0][-1]

def huffman_codes(tree, prefix=""):
    """tree is a list of list representing trees"""
    if len(tree) == 1:
        yield (tree, prefix)
        return
    for bit, child in zip("01", tree):
        for pair in huffman_codes(child, prefix + bit):
            yield pair

def huffman_decode(binary, current_tree, root_tree):
    """TODO: """
    pass

####################################################
"""Naive implementation of Kruskall algorithm"""
def naive_find(C, u):
    while C[u] != u: # search the representative
        u = C[u]
    return u

def naive_union(C, u, v):
    u = naive_find(C, u)
    v = naive_find(C, v) # make v as the representative
    C[u] = v

def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u:u for u in G}
    for _, u, v in sorted(E):
        if naive_find(C, u) != naive_find(C, v):
            T.add(u, v)
            naive_union(C, u, v)
    return T
####################################################
"""Improved Kruskall algorithm
the running time is Theta(mlgn):
"""
def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u]) # path compression, a little bit mind bending
    return C[u]

def union(C, R, u, v):
    u = find(C, u)
    v = find(C, v)
    if R[u] > R[v]: # union  by rank
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1

def kruska(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u:u for u in G}, {u:0 for u in G}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add(u, v)
            union(C, R, u, v)
    return T

#######################################################
"""Prim's algorithm"""
def prim(G, s):
    """here to do list is a priority queue based on weight"""
    P, Q = {}, [(0, None, s)] # here 0 is the waight, None here is the predecessor of s
    while Q:
        _, p, u = heappop(Q)
        if u in P:
            continue
        P[u] = p
        for v, w in G[u].items():
            heappush(Q, (w, u, v)) # hereu is predecessor of v
    return P






class Ch07TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_make_changes(self):
        """greedy thinking"""
        denom = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
        owed = 5632
        payed = []
        result = [5000, 500, 100, 25, 5, 1, 1]
        for d in denom:
            while owed >= d:
                owed -= d
                payed.append(d)
        self.assertEqual(sum(payed), 5632)
        self.assertEqual(payed, result)

    def test_huffman_trees(self):
        seq = "abcdefghi"
        frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
        result_trees = [['i', [['a', 'b'], 'e']], [['f', 'g'], [['c', 'd'], 'h']]]
        self.assertEqual(huffman_trees(seq, frq), result_trees)
        result_char_map = dict(huffman_codes(result_trees))
        self.assertEqual(result_char_map['a'], '0100')
        self.assertEqual(result_char_map['b'], '0101')



if __name__ == '__main__':
    unittest.main()
