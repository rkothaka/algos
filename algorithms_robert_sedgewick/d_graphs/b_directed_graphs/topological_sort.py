from d_graphs.b_directed_graphs.digraph import Digraph
from d_graphs.b_directed_graphs.directed_cycle import DirectedCycle
from d_graphs.b_directed_graphs.depth_first_order import DepthFirstOrder


class Topological:
    def __init__(self, G: Digraph):
        self.cycle_finder = DirectedCycle(G)
        self.order = None
        if not self.cycle_finder.has_cycle():
            dfs = DepthFirstOrder(G)
            self.order = dfs.reverse_postorder()

    @property
    def order(self):
        return self.order

    @order.setter
    def order(self, val):
        self.order = val

    def has_order(self):
        return self.order is not None
