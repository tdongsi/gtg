

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
        if outgoing:
            return self._outgoing[v].values()
        else:
            return self._incoming[v].values()

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
