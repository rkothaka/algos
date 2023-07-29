from uf import UF


class QuickFindUF(UF):

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)

        if pID == qID:
            return

        self.id = [qID if x == pID else x for x in self.id]
        self.count -= 1

    def find(self, p) -> int:
        return self.id[p]