class MaxPQ:
    def __init__(self, size):
        # index 0 is unused
        self.pq = [None] * (size + 1)
        self.n = 0

    def __bool__(self):
        return self.n == 0

    def empty(self):
        return not self

    def size(self):
        return self.n

    def insert(self, item):
        self.n += 1
        self.pq[self.n] = item
        self.swim(self.n)

    def del_max(self):
        item = self.pq[1]
        self.exchange(1, self.n)
        self.n -= 1
        self.sink(1)
        return item

    def exchange(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def swim(self, k):
        while k > 1 and self.less(k//2, k):
            self.exchange(k//2, k)
            k //= 2

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j, j+1):
                j += 1
            if not self.less(k, j):
                break
            self.exchange(k, j)
            k = j
