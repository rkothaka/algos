from typing import Iterable
from d_graphs.b_directed_graphs.digraph import Digraph


class DirectedDFS:
    def __init__(self, G: Digraph, sources: Iterable[int]):
        self.marked = [False] * G.V
        for s in sources:
            self.dfs(G, s)

    def dfs(self, G: Digraph, v: int):
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def marked(self, v):
        return self.marked[v]
