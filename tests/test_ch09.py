"""Testing for ch09"""

import logging
import random
import unittest
from bisect import bisect
from collections import defaultdict
from copy import deepcopy
from functools import wraps
from heapq import heapify, heappop, heappush
from itertools import combinations, count

from util.data import W_G_dict_dict

LOG = logging.getLogger(__name__)

def relax(G, u, v, D, P):
    """relax the distance"""
    inf = float('inf')
    pre_d_v = D.get(v, inf)
    cur_d_v = D.get(u, inf) + G[u][v]
    if cur_d_v < pre_d_v:
        D[v], P[v] = cur_d_v, u
        #LOG.info("changed: (u:v) -> {0}:{1}".format(u, v))
        #LOG.info("distance pre:cur {0}:{1} ***".format(pre_d_v, cur_d_v))
        return True
    #LOG.info("un-changed: (u:v) -> {0}:{1}".format(u, v))
    #LOG.info("distance pre:cur {0}:{1}".format(pre_d_v, cur_d_v))
    return False

def bellman_ford(G, s): # G: a weighted graph with n nodes and m edges
    """
    relax like crzay: relax at most n-1 rounds
    relaxation leads to bellman ford algorithm for shorted path of weighted graph
    it is a single-source shorted path algorithm allowing arbitrary directed or undirected graphs.
    if the graph contains negative cycle, it will report that and give up.
    """
    D, P = {s: 0}, {} # D: distance to node, P: parent of s
    for rnd in G: # the maxiume rounds of relaxation is n - 1 (maxiume numer of edges in the shorted path)
        LOG.info("Rounds: # {0}".format(rnd))
        changed = False # flag if a change happened
        for u in G:
            for v in G[u]:
                changed = relax(G, u, v, D, P)
        if not changed:
            break # early termination
    else:
        raise ValueError('negative cycle')
    return D, P

def dijkstra(G, s):
    """
    finding the hidden DAG, relax starting always with the lowest estimate distance node
    using the priority queue based on estimated distance
    assumption: no negative cycle
    """
    D, P, Q, S = {s: 0}, {}, [(0, s)], set() # Estimates, Path, queue, seen set, initialize distance to s is 0,
    while Q:
        _, u = heappop(Q) # start with the lowest estimate node
        if u in S:
            continue
        S.add(u)
        for v in G[u]: # go through all its neighbors
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))
    return D, P

def johnson(G):
    """all pairs shorted path
    allow negative cycles. this is the algorithm that combines bellman_ford and dijkstra together with the clever idea (teloscoping sums)
    """
    G = deepcopy(G)
    LOG.info("before: {0}".format(G))
    s  = object() # create a sentinel value as a special node
    LOG.info("s: {0}".format(s))
    G[s] = {v:0 for v in G} # create a new node s and add edge from s to all other nodes with weight 0
    LOG.info("after: {0}".format(G))
    h, _ = bellman_ford(G, s) # run bellman_ford from s to get distances from s to all other nodes
    LOG.info("after bellman h: {0}".format(h))

    del G[s]  # no long needed
    LOG.info("after deleted s: {0}".format(G))
    for u in G:
        for v in G[u]:
            G[u][v] += h[u] - h[v] # adjust all weights to make sure nonnegative edges
    LOG.info("after adjust weight: {0}".format(G))
    D, P = {}, {}
    for u in G:
        D[u], P[u] = dijkstra(G, u) # for every u, run dijkstra algorithm to get distance and path
        for v in G:
            D[u][v] += h[v] - h[u] # readjust distance back
    LOG.info(D)
    return D, P # which are two-dimentional



####################################################
class Ch09TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_bellman_ford(self):
        """test bellman ford algirhtm for shorted path of weighted general graph"""
        a,b,c,d,e,f,g,h = range(8)
        G = W_G_dict_dict
        G_negative = deepcopy(G)
        G_negative[g][h] = -9
        #self.assertEqual(bellman_ford(G, a), [])
        #self.assertEqual(bellman_ford(G_negative, a), [])

    def test_dijkstra(self):
        """test bellman ford algirhtm for shorted path of weighted general graph"""
        a,b,c,d,e,f,g,h = range(8)
        G = W_G_dict_dict
        #self.assertEqual(dijkstra(G, a), [])

    def test_johnson(self):
        """test bellman ford algirhtm for shorted path of weighted general graph"""
        a,b,c,d,e,f,g,h = range(8)
        G = W_G_dict_dict
        self.assertEqual(johnson(G), [])


if __name__ == '__main__':
    unittest.main()
