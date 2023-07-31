from collections import deque
from d_graphs.b_directed_graphs.digraph import Digraph


class DepthFirstOrder:
    def __init__(self, G: Digraph):
        self.pre = deque()
        self.post = deque()

        self.marked = [False] * G.V

        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G: Digraph, v: int):
        self.pre.append(v)
        self.marked[v] = True
        for w in G.adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

        self.post.append(v)

    def preorder(self):
        return self.pre

    def postorder(self):
        return self.post

    def reverse_postorder(self):
        return reversed(self.post)
