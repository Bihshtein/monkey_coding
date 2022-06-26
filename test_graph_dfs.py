import unittest
from graph import Graph


class Tests(unittest.TestCase):
    def test_1(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)

        self.assertEqual([2, 0, 1, 3], g.dfs(2))
        self.assertEqual([2, 0, 3, 1], g.bfs(2))
