"""Testing for ch06"""

import logging
import random
import unittest
from bisect import bisect, bisect_left
from copy import deepcopy

LOG = logging.getLogger(__name__)

class Node:
    """AA Tree unit """
    lft = None
    rgt = None
    lvl = 1
    def __init__(self, key, val):
        self.key = key
        self.val = val

def skew(node):
    """right rotate"""
    if None in [node, node.left]:
        return node
    if node.lft.lvl != node.lvl:
        return node
    lft = node.lft
    node.lft = lft.rgt
    lft.rgt = node
    return lft

def split(node):
    """basic left rotate of node"""
    if None in [node, node.rgt, node.rgt.rgt]:
        return node
    if node.rgt.rgt.lvl != node.lvl:
        return node
    rgt = node.rgt
    node.rgt = rgt.lft
    rgt.lft = node
    rgt.lvl += 1
    return rgt

def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = inssert(node.rgt, key, val)
    # balance the node after operation
    node = skew(node)
    node = split(node)
    return node

def search(node, key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    elif key < node.key:
        return search(node.lft, key)
    else:
        return search(node.rgt, key)

class Tree:
    """Tree wrapper"""
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try:
            search(self.root, key)
        except KeyError:
            return False
        return True



class Ch06TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_tree(self):
        tree = Tree()
        tree['a'] = 42
        self.assertEqual(tree['a'], 42)
        self.assertEqual('b' in tree, False)







if __name__ == '__main__':
    unittest.main()
