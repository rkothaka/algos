from collections import deque
from typing import Optional, Iterator

from d_graphs.a_undirected_graphs.graph import Graph


class BreadthFirstPaths:
    def __init__(self, G: Graph, s: int):
        self.marked = [False] * G.V
        self.edge_to = [-1] * G.V
        self.s = s
        self.bfs(G, s)

    def bfs(self, G: Graph, s):
        queue = deque()
        self.marked[s] = True
        queue.append(s)

        while queue:
            v = queue.popleft()
            for w in G.adj(v):
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    queue.append(w)

    def has_path_to(self, v: int) -> bool:
        return self.marked[v]

    def path_to(self, v: int) -> Optional[Iterator[int]]:
        if not self.has_path_to(v):
            return None

        path = [v]
        while v != self.s:
            v = self.edge_to[v]
            path.append(v)

        return iter(path)
