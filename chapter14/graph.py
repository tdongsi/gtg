

class Vertex:
    """Lightweight vertex structure for graph"""
    __slots__ = "_element"

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))


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
        """ Example airport graph shown in Figure 14.8, page 640

        :return:
        """
        g = Graph(directed=True)

        bos = Vertex("BOS")
        jfk = Vertex("JFK")
        dfw = Vertex("DFW")
        lax = Vertex("LAX")
        ord = Vertex("ORD")
        mia = Vertex("MIA")
        sfo = Vertex("SFO")

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

