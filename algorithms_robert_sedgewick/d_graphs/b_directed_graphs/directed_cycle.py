from d_graphs.b_directed_graphs.digraph import Digraph


class DirectedCycle:
    def __init__(self, G: Digraph):
        self.on_stack = [False] * G.V
        self.edge_to = [-1] * G.V
        self.marked = [False] * G.V
        self.cycle = None
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.on_stack[v] = True
        self.marked[v] = True
        for w in G.adj(v):
            if self.has_cycle():
                return
            elif not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)
            elif self.on_stack[w]:
                self.cycle = []
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(w)
        self.on_stack[v] = False

    def has_cycle(self):
        return self.cycle is not None

    @property
    def cycle(self):
        return self.cycle
