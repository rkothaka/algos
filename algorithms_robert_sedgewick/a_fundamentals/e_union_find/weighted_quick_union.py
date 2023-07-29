from uf import UF


class WeightedQuickUnionUF(UF):
    def __init__(self, n):
        super().__init__(n)
        self.sz = [1] * n

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

        self.count -= 1

    def find(self, p) -> int:
        while p != self.id[p]:
            p = self.id[p]
        return p
