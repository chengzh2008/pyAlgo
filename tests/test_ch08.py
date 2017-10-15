"""Testing for ch06"""

import logging
import random
import unittest
from bisect import bisect
from collections import defaultdict
from functools import wraps
from heapq import heapify, heappop, heappush
from itertools import combinations, count

from src.ch05 import dfs_topsort
from util.helper import memo

LOG = logging.getLogger(__name__)

def naive_lis(seq):
    """naive implementation of longest increase subsequence
    basicall it get all possible subsequence combinations, then test if one of them is sorted
    """
    for length in range(len(seq), 0, -1): # from n, n-1, ..., 1
        for sub in combinations(seq, length): # subsequence of given length
            sub_list = list(sub)
            if sub_list == sorted(sub): # check if sorted
                return sub_list

def rec_lis(seq):
    """recursive implementation of longest increase subsequence"""
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res
    return max(L(i) for i in range(len(seq)))

def iter_lis(seq):
    """interative implementation of longest increase subsequence
    bigO is quadratic
    """
    n = len(seq)
    L = [1]*n
    for i in range(n):
        for pre in range(i):
            if seq[pre] <= seq[i]:
                L[i] = max(L[i], 1 + L[pre])
    return max(L[i] for i in range(n))

def bisect_iter_lis(seq):
    """improve the iterative longest increase subsequence
    improve the inner loop by using the bisection
    """
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
        LOG.info("idx: {0}".format(idx))
        LOG.info(end)
    return len(end)

####################################################
@memo
def fib(i):
    """naive_recursive version"""
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)

####################################################
@memo
def C(n, k):
    """pascal triangle"""
    if k == 0:
        return 1
    if n == 0:
        return 0
    return C(n-1, k-1) + C(n-1, k)

def iter_pascal_triangle(n, k):
    C = defaultdict(int)
    for row in range(n + 1):
        C[row, 0] = 1
        for col in range(1, k + 1):
            C[row, col] = C[row-1, col-1] + C[row-1, col]
    LOG.info(C)
    return C[n, k]
####################################################
def rec_dag_shortpath(W, s, t):
    """recursive shorpath for DAG
    W: weight dict
    s: starting node
    t: target node
    """
    @memo
    def d(u):
        if u == t: # base case
            return 0
        # think forward, let recursive handle the rest of the problem
        return min(W[u][v] + d(v) for v in W[u])
    return d(s)

def iter_dag_shortpath(W, s, t):
    """iterative shortpath for DAG
    relaxation
    upside-down of the recursive algorithm"""
    d = {u: float('inf') for u in W} # initialize all distance to be infinity
    d[s] = 0 # set distance for starting node to be 0
    for u in dfs_topsort(W): #iterative needs a topsorted DAG to start
        if u == t:
            break
        for v in W[u]: # relaxation of every node
            d[v] = min(d[v], W[u][v] + d[u])
    return d[t]

####################################################
def rec_lcs(seq1, seq2):
    """memoized recursive solution for longest common subsequence"""
    @memo
    def L(i, j):
        if min(i, j) < 0: # one prefix is empty
            return 0
        if seq1[i] == seq2[j]: # match: recursively call subproblem
            return 1 + L(i-1, j-1)
        return max(L(i-1, j), L(i, j-1)) # not match: chose the max one of the subproblem
    return L(len(seq1)-1, len(seq2)-1)

def iter_lcs(seq1, seq2):
    """iterative solution for the longest common subsequence"""
    n, m = len(seq1), len(seq2)
    pre, cur = [0]* (n+1), [0]*(n+1)
    for j in range(1, m+1):
        pre, cur = cur, pre
        for i in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                cur[i] = pre[i-1] + 1
            else:
                cur[i] = max(pre[i], cur[i-1])
    return cur[n]

####################################################
def rec_unbounded_knapsack(w, v, c): # weights, values, and capacity
    """recursive solution for unbounded knapsack problem"""
    @memo
    def m(r): # remaining capacity
        if r == 0:
            return 0
        val = m(r-1) # ignore the last cap/unit
        for i, wi in enumerate(w): # try every object with this remaining capacity r
            if wi > r: # too heavy, ignore it
                continue
            val = max(val, v[i] + m(r-wi)) # choose the max one over all
        return val
    return m(c)

def iter_unbounded_knapsack(w, v, c):
    """iterative solution for unbounded knapsack problem"""
    m = [0] # 0 capacity stored first
    for r in range(1, r+1):
        val = m[r-1]
        for i, wi in enumerate(w):
            if wi > r:
                continue
            val = max(val, v[i] + m[r-w(i)])
        m.append(val)
    return m[c]

def rec_bounded_knapsack(w, v, c):
    """recursive solution to bounded(0-1) knapsack problem"""
    @memo
    def m(k, r): # k: first k elements; r: remaining capacity
        if k == 0 or r == 0:
            return 0
        i = k-1 # object i under consideration
        drop = m(i, r) # not considering the kth element
        if w[i] > r:
            return drop
        return max(drop, v[i] + m(i, r-w[i]))

def iter_bounded_knapsack(w, v, c):
    """iterative solution to bounded(0-1) knapsack problem"""
    n = len(w)
    m = [[0]*(c+1) for i in range(1, n+1)] # empty max-value matrix
    p = [[False]*(c+1) for i in range(1, n+1)] # empty keep-drop matrix
    for k in range(1, n+1):
        i = k-1 # elem under consideration
        for r in range(1, r+1):
            m[k][r] = drop = m[k-1][r] # not consider i
            if w[i] > r:
                continue
            keep = v[i] + m[k-1][r-w[i]]
            m[k][r] = max(drop, keep)
            p[k][r] = keep > drop
    return m, p

def retrive_set_from_iter_bounded_knapsack(w, m, p):
    """retrieve the set from result of iter_bounded_knapsack"""
    k, r, items = len(w), c, set()
    while k > 0 and r > 0:
        i = k-1
        if p[k][r]:
            items.add(i)
            r -= w[i]
        k -= 1
    return items



####################################################
class Ch08TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_naive_lis(self):
        """test naive longest increase subsequence"""
        input_list = [3, 1, 0, 2, 4]
        output_list = [1, 2, 4]
        self.assertEqual(naive_lis(input_list), output_list)

    def test_rec_lis(self):
        """test recursive longest increase subsequence"""
        input_list = [3, 1, 0, 2, 4]
        output_list = [1, 2, 4]
        self.assertEqual(rec_lis(input_list), len(output_list))

    def test_iter_lis(self):
        """test iterative longest increase subsequence"""
        input_list = [3, 1, 0, 2, 4]
        output_list = [1, 2, 4]
        self.assertEqual(iter_lis(input_list), len(output_list))

    def test_bisect_iter_lis(self):
        """test iterative longest increase subsequence"""
        input_list = [3, 1, 0, 2, 4]
        output_list = [1, 2, 4]
        self.assertEqual(bisect_iter_lis(input_list), len(output_list))

    def test_fib(self):
        """test fib"""
        self.assertEqual(fib(100), 573147844013817084101L)

    def test_pascal_triangle(self):
        """test parscal triangle"""
        self.assertEqual(C(100, 50), 100891344545564193334812497256)
        self.assertEqual(iter_pascal_triangle(100, 50), 100891344545564193334812497256)

    def test_shortpath(self):
        """test recursive and iterative"""
        W = {
            'a': {
                'b': 2,
                'f': 9
            },
            'b': {
                'd': 2,
                'c': 1,
                'f': 6
            },
            'c': {
                'd': 7
            },
            'd': {
                'e': 2,
                'f': 3
            },
            'e': {
                'f': 4
            },
            'f': {}
        }
        start = 'a'
        target = 'f'
        self.assertEqual(iter_dag_shortpath(W, start, target), rec_dag_shortpath(W, start, target))

    def test_rec_lcs(self):
        """test recursive and iterative lcs"""
        a = "abcdefghi"
        b = "cefxyz"
        common = "cef"
        self.assertEqual(rec_lcs(a, b), len(common))
        self.assertEqual(iter_lcs(a, b), len(common))

if __name__ == '__main__':
    unittest.main()
