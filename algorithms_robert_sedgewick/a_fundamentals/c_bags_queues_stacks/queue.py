from node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def empty(self) -> bool:
        return not self.first

    def __bool__(self) -> bool:
        return not self.empty()

    def size(self) -> int:
        return self.n

    def __len__(self) -> int:
        return self.size()

    def enqueue(self, item):
        oldLast = self.last
        self.last = Node(item)
        if self.empty():
            self.first = self.last
        else:
            oldLast.next = self.last
        self.n += 1

    def deque(self):
        if self.empty():
            raise IndexError("Queue is empty. Cannot deque from an empty stack.")

        node = self.first
        self.first = self.first.next
        self.n -= 1
        if self.empty():
            self.last = None
        return node

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.next
