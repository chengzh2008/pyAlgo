import logging
import unittest

from src.ch02 import Node

LOG = logging.getLogger("Ch02TestSuite")

class Ch02TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_node(self):
        LOG.debug("Testing Node implementation")
        node = Node("a", Node("b", Node("c", Node("d"))))

        value = "c"
        realvalue = node.next.next.value
        self.assertEqual(realvalue, value, msg='{0}, {1}'.format(realvalue, value))

    def test_adjacency_set_graph(self):
        a,b,c,d,e,f,g,h = range(8)
        N = [
            {b,c,d,e,f}, #a
            {c,e},
            {d},
            {e},
            {f},
            {c,g,h},
            {f,h},
            {f,g}
        ]
        self.assertEqual(b in N[a], True, msg="{0}, {1}".format("is b in N[a]", b in N[a]))

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("Ch02TestSuite").setLevel(logging.DEBUG)
    unittest.main()
