
from chapter14.graph import *

import unittest


class TestGraph(unittest.TestCase):

    def test_dijkstra_algorithm(self):
        g = ExampleGraphs.airport_graph()

        # This map is created for readability
        vertex_map = {v.element(): v for v in g.vertices()}
        starting_vertex = vertex_map["JFK"]

        cloud = shortest_path_lengths(g, starting_vertex)

        for k, v in cloud.items():
            print("%s: %s"% (k,v))

        sp_tree = shortest_path_tree(g, starting_vertex, cloud)
        path = construct_path(vertex_map["JFK"], vertex_map["LAX"], sp_tree)
        print([str(ap) for ap in path])

    def test_dfs(self):
        g, s = ExampleGraphs.alphabet_graph()

        discovered = {s: None}
        DFS(g, s, discovered)

        discovered_iter = DFS_iter(g, s)

        for v in g.vertices():
            print("%s: %s vs %s", v, discovered[v], discovered_iter[v])

    def test_bfs(self):
        g, s = ExampleGraphs.alphabet_graph()

        discovered = {s: None}
        BFS(g, s, discovered)

        discovered_iter = BFS_iter(g, s)

        self.assertDictEqual(discovered, discovered_iter)
        for v in g.vertices():
            print("%s: %s vs %s", v, discovered[v], discovered_iter[v])
        pass

    def test_edmond_karp(self):
        g, source, sink = ExampleGraphs.simplet_network_flow()

        max_flow = edmonds_karp(g, source, sink)
        self.assertEqual(max_flow, 200)
        pass
