class Digraph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self.adj = [set() for _ in range(V)]

    @property
    def V(self):
        return self._V

    @property
    def E(self):
        return self.E

    @E.setter
    def E(self, value):
        self._E = value

    def add_edge(self, v, w):
        if v > self.V or w > self.V:
            raise ValueError("Invalid edge. Vertex out of bounds")
        if w in self.adj[v]:
            raise ValueError("Edge already exists")

        self.adj[v].add(w)
        self.E += 1

    def adj(self, v):
        return self.adj[v]

    def reverse(self):
        R = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj(v):
                R.add_edge(w, v)
        return R
