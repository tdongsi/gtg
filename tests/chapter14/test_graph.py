
from chapter14.graph import *

import unittest


class ExampleGraphs:

    @staticmethod
    def airport_graph():
        """ Example airport graph shown in Figure 14.14, page 659

        :return:
        """
        g = Graph(directed=False)

        bos = g.insert_vertex("BOS")
        jfk = g.insert_vertex("JFK")
        dfw = g.insert_vertex("DFW")
        lax = g.insert_vertex("LAX")
        ord = g.insert_vertex("ORD")
        mia = g.insert_vertex("MIA")
        sfo = g.insert_vertex("SFO")

        g.insert_edge(bos, jfk, 187)
        g.insert_edge(bos, sfo, 2704)
        g.insert_edge(bos, ord, 867)
        g.insert_edge(bos, mia, 1258)

        g.insert_edge(jfk, ord, 740)
        g.insert_edge(jfk, mia, 1090)

        g.insert_edge(mia, lax, 2342)
        g.insert_edge(mia, dfw, 1121)

        g.insert_edge(dfw, lax, 1235)
        g.insert_edge(dfw, sfo, 1464)
        g.insert_edge(dfw, ord, 802)

        g.insert_edge(ord, sfo, 1846)

        g.insert_edge(sfo, lax, 337)

        return g

    @staticmethod
    def alphabet_graph():
        """Example alphabet graph shown in Figure 14.9 (pg 641) and Figure 14.10 (pg 649)
        Returning the graph and optional starting vertex.
        """

        graph = Graph()

        a = graph.insert_vertex("a")
        b = graph.insert_vertex("b")
        c = graph.insert_vertex("c")
        d = graph.insert_vertex("d")
        e = graph.insert_vertex("e")
        f = graph.insert_vertex("f")
        g = graph.insert_vertex("g")
        h = graph.insert_vertex("h")
        i = graph.insert_vertex("i")
        j = graph.insert_vertex("j")
        k = graph.insert_vertex("k")
        l = graph.insert_vertex("l")
        m = graph.insert_vertex("m")
        n = graph.insert_vertex("n")
        o = graph.insert_vertex("o")
        p = graph.insert_vertex("p")

        graph.insert_edge(a, b)
        graph.insert_edge(a, e)
        graph.insert_edge(a, f)
        graph.insert_edge(b, f)
        graph.insert_edge(e, f)

        graph.insert_edge(b, c)
        graph.insert_edge(c, d)
        graph.insert_edge(c, g)
        graph.insert_edge(g, d)
        graph.insert_edge(d, h)

        graph.insert_edge(e, i)
        graph.insert_edge(f, i)
        graph.insert_edge(i, m)
        graph.insert_edge(i, n)
        graph.insert_edge(i, j)

        graph.insert_edge(g, j)
        graph.insert_edge(g, k)
        graph.insert_edge(g, l)
        graph.insert_edge(h, l)
        graph.insert_edge(j, k)

        graph.insert_edge(m, n)
        graph.insert_edge(k, n)
        graph.insert_edge(k, o)
        graph.insert_edge(l, p)

        return graph, a

    @staticmethod
    def simplet_network_flow():
        """Simple network flow. Based on Figure 7.6 from Algorithm Design book by Kleinberg, Tardos."""

        g = Graph(directed=True)

        source = g.insert_vertex("s")
        sink = g.insert_vertex("t")
        u = g.insert_vertex("u")
        v = g.insert_vertex("v")

        g.insert_edge(source, u, 100)
        g.insert_edge(source, v, 100)
        g.insert_edge(u, v, 1)
        g.insert_edge(u, sink, 100)
        g.insert_edge(v, sink, 100)

        return g, source, sink

    @staticmethod
    def demo_network_flow():
        """Demo network flow, as shown in Network Flow slides.
        http://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/07DemoFordFulkerson.pdf
        """
        g = Graph(directed=True)

        source = g.insert_vertex("s")
        sink = g.insert_vertex("t")
        a = g.insert_vertex("a")
        b = g.insert_vertex("b")
        c = g.insert_vertex("c")
        d = g.insert_vertex("d")

        g.insert_edge(source, a, 10)
        g.insert_edge(source, c, 10)
        g.insert_edge(a, c, 2)
        g.insert_edge(a, b, 4)
        g.insert_edge(a, d, 8)
        g.insert_edge(c, d, 9)
        g.insert_edge(d, b, 6)
        g.insert_edge(b, sink, 10)
        g.insert_edge(d, sink, 10)

        return g, source, sink

    @staticmethod
    def bipartite_matching_graph():
        """ Network flow for example bipartite matching problem.
        Based on Figure 7.9 from Algorithm Design book by Kleinberg, Tardos.
        """
        g = Graph(directed=True)

        source = g.insert_vertex("s")
        sink = g.insert_vertex("t")

        m1 = g.insert_vertex("M1")
        m2 = g.insert_vertex("M2")
        m3 = g.insert_vertex("M3")
        m4 = g.insert_vertex("M4")
        m5 = g.insert_vertex("M5")

        f1 = g.insert_vertex("F1")
        f2 = g.insert_vertex("F2")
        f3 = g.insert_vertex("F3")
        f4 = g.insert_vertex("F4")
        f5 = g.insert_vertex("F5")

        g.insert_edge(source, m1, 1)
        g.insert_edge(source, m2, 1)
        g.insert_edge(source, m3, 1)
        g.insert_edge(source, m4, 1)
        g.insert_edge(source, m5, 1)

        g.insert_edge(f1, sink, 1)
        g.insert_edge(f2, sink, 1)
        g.insert_edge(f3, sink, 1)
        g.insert_edge(f4, sink, 1)
        g.insert_edge(f5, sink, 1)

        g.insert_edge(m1, f1, 1)
        g.insert_edge(m1, f3, 1)

        g.insert_edge(m2, f1, 1)
        g.insert_edge(m2, f2, 1)
        g.insert_edge(m2, f3, 1)
        g.insert_edge(m2, f4, 1)

        g.insert_edge(m3, f4, 1)

        g.insert_edge(m4, f4, 1)

        g.insert_edge(m5, f4, 1)
        g.insert_edge(m5, f5, 1)

        return g, source, sink


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

        g, source, sink = ExampleGraphs.demo_network_flow()
        max_flow = edmonds_karp(g, source, sink)
        self.assertEqual(max_flow, 19)

        g, source, sink = ExampleGraphs.bipartite_matching_graph()
        max_flow = edmonds_karp(g, source, sink)
        self.assertEqual(max_flow, 4)
        pass
