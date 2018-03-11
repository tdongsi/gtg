
from chapter14.graph import *

import unittest


class TestGraph(unittest.TestCase):

    def test_dijkstra_algorithm(self):
        g = ExampleGraphs.airport_graph()

        vertex_map = {v.element() : v for v in g.vertices()}
        starting_vertex = vertex_map["JFK"]

        cloud = shortest_path_lengths(g, starting_vertex)

        for k, v in cloud.items():
            print("%s: %s"% (k,v))

        sp_tree = shortest_path_tree(g, starting_vertex, cloud)
        path = construct_path(vertex_map["JFK"], vertex_map["LAX"], sp_tree)

        for ap in path:
            print(str(ap))