class IndexMinPQ:
    def __init__(self, size):
        self.keys = [None] * (size + 1)
        self.pq = [0] * (size + 1)
        self.qp = [-1] * (size + 1)
        self.n = 0

    def __bool__(self):
        return self.n == 0

    def empty(self):
        return not self

    def contains(self, i):
        return self.qp[i] != -1

    def insert(self, i, key):
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swim(self.n)

    def min_key(self):
        return self.keys[self.pq[1]]

    def del_min(self):
        min_idx = self.pq[1]
        self.exchange(1, self.n)
        self.n -= 1
        self.keys[min_idx] = None
        self.qp[min_idx] = -1
        self.sink(1)
        return min_idx

    def change_key(self, i, new_key):
        if not self.contains(i):
            raise ValueError(f"Index {i} is not in the priority queue.")
        self.keys[i] = new_key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def delete(self, i):
        if not self.contains(i):
            raise ValueError(f"Index {i} is not in the priority queue.")
        idx = self.qp[i]
        self.exchange(idx, self.n)
        self.n -= 1
        self.qp[i] = -1
        self.keys[i] = None
        self.swim(idx)
        self.sink(idx)

    def exchange(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]], self.qp[self.pq[j]] = i, j

    def less(self, i, j):
        return self.keys[self.pq[i]] < self.keys[self.pq[j]]

    def swim(self, k):
        while k > 1 and self.less(k, k//2):
            self.exchange(k, k//2)
            k //= 2

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j + 1, j):
                j += 1
            if not self.less(j, k):
                break
            self.exchange(k, j)
            k = j

    def __repr__(self):
        return f"IndexMinPQ({self.keys}, {self.pq}, {self.qp})"

    def __str__(self):
        pq_str = ", ".join(str(self.pq[i]) for i in range(1, self.n+1))
        keys_str = ", ".join(str(self.keys[self.pq[i]]) for i in range(1, self.n+1))
        return f"IndexMinPQ: pq=[{pq_str}], keys=[{keys_str}]"


if __name__ == "__main__":
    my_pq = IndexMinPQ(10)

    import random
    for i in range(1, 11):
        my_pq.insert(i, random.randrange(10, 100))

    print(repr(my_pq))
    my_pq.delete(7)
    my_pq.delete(3)
    print(repr(my_pq))
