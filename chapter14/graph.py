
from copy import deepcopy

class Vertex:
    """Lightweight vertex structure for graph"""
    __slots__ = "_element"

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return "[Vertex: %s]" % self._element


class Edge:
    """Lightweight edge structure for graph"""
    __slots__ = "_src", "_des", "_element"

    def __init__(self, u, v, x):
        self._src = u  # source
        self._des = v  # destination
        self._element = x

    def endpoints(self):
        return self._src, self._des

    def opposite(self, u):
        if u is self._src:
            return self._des
        elif u is self._des:
            return self._src
        else:
            raise ValueError("Unknown vertex")

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._src, self._des))

    def __str__(self):
        return "%s >- %s -> %s" % (self._src, self._element, self._des)


class Graph:
    """Simple graph using an adjancency map"""

    def __init__(self, directed=False):
        self._outgoing = {}
        # Only create the second map for directed graph
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._outgoing is not self._incoming

    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._outgoing)

    def vertices(self):
        """Return the iteration of all vertices"""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges"""
        total = sum([len(self._outgoing[v]) for v in self.vertices()])
        return total if self.is_directed() else total//2

    def edges(self):
        """Return the iteration of all edges"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        # TRICKY: self._outgoing[u][v] will raise KeyError instead of None if (u,v) not found
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        if outgoing:
            return len(self._outgoing[v])
        else:
            return len(self._incoming[v])

    def incident_edges(self, v, outgoing=True):
        """Return an *iteration* of incident edges"""
        adj = self._outgoing if outgoing else self._incoming
        for e in adj[v].values():
            yield e

    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e


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


def DFS(g:Graph, u:Vertex, discovered):
    """ DFS traversal of the undiscovered portion of Graph g starting at Vertex u.
    Example: start DFS traversal with DFS(g, u, {u: None}).

    :param g: given Graph
    :param u: starting Vertex
    :param discovered: Mapping each vertex to the edge used to discover it.
    :return:
    """
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)


def construct_path(u:Vertex, v:Vertex, discovered):
    """ Construct a path from u to v.

    :param u: source Vertex
    :param v: destination Vertex
    :param discovered: discovery edges constructed from DFS
    :return: list of vertices from u to v
    """
    path = []

    if v in discovered:
        path.append(v)

        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent

        path.reverse()

    return path


def BFS(g:Graph, s:Vertex, discovered):
    """ BFS traversal of the undiscovered portion of Graph g starting at vertex s.

    :param g: give Graph
    :param s: starting Vertex
    :param discovered: Mapping each vertex to the edge used to discover it.
    :return:
    """
    level = [s]

    while len(level) > 0:
        next_level = []
        for v in level:
            for e in g.incident_edges(v):
                u = e.opposite(v)
                if u not in discovered:
                    discovered[u] = e
                    next_level.append(u)

        level = next_level


def is_bipartite(g:Graph, s:Vertex):
    """ Check if a graph is bipartite.

    :param g: give Graph
    :param s: starting Vertex
    :return: True if bipartite.
    """
    # Perform a BFS traversal and keep track of color
    level = [s]
    coloring = {s: 0}  # keep track of colors for each node

    while len(level) > 0:
        next_level = []
        for v in level:
            for e in g.incident_edges(v):
                u = e.opposite(v)
                if u not in coloring:
                    coloring[u] = 1 - coloring[v]
                    next_level.append(u)
                else:
                    if coloring[u] == coloring[v]:
                        return False

        level = next_level

    return True


def floyd_warshall(g:Graph) -> Graph:
    """ Return a new graph that is the transite closure of g.

    :param g: input graph
    :return: the transitive closure of g.
    """
    closure = deepcopy(g)
    verts = list(closure.vertices())
    n = len(verts)

    for k in range(n):
        for i in range(n):
            # verify that edge(i, k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge(k, j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        if closure.get_edge(verts[i], verts[j]) is None:
                            # if (i, j) not yet included, add it to the closure
                            closure.insert_edge(verts[i], verts[j])

    return closure


def topological_sort(g: Graph) -> list:
    """ Return a list of vertices of DAG in topological order

    :param g: a directed acyclic graph (DAG)
    :return: list of topological sort
    """
    topo = []
    ready = []
    incount = {}

    for u in g.vertices():
        incount[u] = g.degree(u, False)
        if incount[u] == 0:
            # u is free of constraints
            ready.append(u)

    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)

        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)

    return topo


class AdaptableUnsortedPriorityQueue():
    """ Mocking AdaptableHeapPriorityQueue.
    loc => key in internal map
    key, val => value in internal map
    """

    def __init__(self):
        self._map = {}

    def add(self, key, value):
        """Add a key-value pair."""
        self._map[value] = (key, value)
        return value

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry"""
        self._map[loc] = (newkey, newval)

    def is_empty(self):
        return (len(self._map) == 0)

    def remove_min(self):

        min_key = float('inf')
        min_loc = None
        min_return = None

        for loc, val in self._map.items():
            if val[0] < min_key:
                min_key = val[0]
                min_loc = loc
                min_return = val

        del self._map[min_loc]
        return min_return


def shortest_path_lengths(g:Graph, s:Vertex):
    """ Compute shortest-path distances from src to reachable vertices of g.
    Dijkstra's Algorithm for finding shortest paths.

    :param g: directed or undirected Graph. e.element() must return non-negative weight
    :param s: Starting vertex
    :return: dictionary mapping each reachable vertex to its distance from s.
    """

    d = {}      # d[v] is upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableUnsortedPriorityQueue()   # vertex v will have key d[v]
    pqlocator = {}      # map from vertex to its pq locator

    for v in g.vertices():
        if v is s:
            d[v] = 0
        else:
            d[v] = float('inf')

        pqlocator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key

        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pqlocator[v], d[v], v)

    return cloud

