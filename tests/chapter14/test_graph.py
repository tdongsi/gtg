
from chapter14.graph import *

import unittest


class TestGraph(unittest.TestCase):

    def test_dijkstra_algorithm(self):
        g = ExampleGraphs.airport_graph()

        starting_vertex = None
        for v in g.vertices():
            if v.element() == "JFK":
                starting_vertex = v

        cloud = shortest_path_lengths(g, starting_vertex)

        for k, v in cloud.items():
            print("%s: %s"% (k,v))