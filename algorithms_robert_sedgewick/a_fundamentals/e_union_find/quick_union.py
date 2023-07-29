from uf import UF


class QuickUnionUF(UF):

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        self.id[i] = j
        self.count -= 1

    def find(self, p) -> int:
        while p != self.id[p]:
            p = self.id[p]
        return p
