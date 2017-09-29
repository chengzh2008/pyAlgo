
class Node:
    """Node implementation"""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Tree:
    """Binary Tree implementation"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

class MTree:
    """MultiWayTree implementation"""

    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next

class Bunch(dict):
    """Bunch pattern"""

    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self
