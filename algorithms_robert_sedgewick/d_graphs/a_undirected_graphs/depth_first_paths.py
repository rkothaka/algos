from typing import Optional, Iterator

from d_graphs.a_undirected_graphs.graph import Graph


class DepthFirstPaths:
    def __init__(self, G: Graph, s: int):
        self.marked = [False] * G.V
        self.edge_to = [-1] * G.V
        self.s = s
        self.dfs(G, s)

    def dfs(self, G: Graph, v: int) -> None:
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)

    def has_path_to(self, v: int):
        return self.marked[v]

    def path_to(self, v: int) -> Optional[Iterator[int]]:
        if not self.has_path_to(v):
            return None

        path = [v]
        while v != self.s:
            v = self.edge_to[v]
            path.append(v)

        return iter(path)
