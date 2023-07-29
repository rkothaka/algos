class Counter:
    def __init__(self, name):
        self._name = name
        self._count = 0

    @property
    def name(self):
        return self._name

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    def increment(self):
        self.count += 1

    def tally(self):
        return self.count

    def __repr__(self):
        return f"Counter(name='{self.name}', count={self.count})"

    def __str__(self):
        return f"Counter: ({self.name}, {self.count})"
