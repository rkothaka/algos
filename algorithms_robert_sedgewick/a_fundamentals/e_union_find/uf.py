from abc import ABC, abstractmethod


class UF(ABC):
    def __init__(self, n):
        self._count = n
        self.id = list(range(1, n+1))

    @abstractmethod
    def union(self, p, q):
        pass

    @abstractmethod
    def find(self, p) -> int:
        pass

    def connected(self, p, q) -> bool:
        return self.find(p) == self.find(q)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, new_count):
        if not isinstance(new_count, int) or new_count < 0:
            raise ValueError("Count must be a non-negative integer.")
        self._count = new_count
