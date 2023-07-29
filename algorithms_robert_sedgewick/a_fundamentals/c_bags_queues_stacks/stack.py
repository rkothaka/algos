class Stack:
    def __init__(self):
        self.data = []

    def empty(self) -> bool:
        return len(self.data) == 0

    def size(self) -> int:
        return len(self.data)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        assert not self.empty()
        item = self.data[-1]
        del self.data[-1]
        return item

    def peek(self):
        assert not self.empty()
        return self.data[-1]

    def __bool__(self):
        return not self.empty()

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.data[::-1]:
            yield item
