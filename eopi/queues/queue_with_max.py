from eopi.stacks.stack_with_max import Stack


class QueueWithMax:
    def __init__(self) -> None:
        self._enqueue, self._dequeue = Stack(), Stack()

    def enqueue(self, x: 'element') -> None:
        self._enqueue.push(x)

    def dequeue(self) -> 'element':
        if self._dequeue.empty():
            while not self._enqueue.empty():
                self._dequeue.push(self._enqueue.pop())

        return self._dequeue.pop()

    def max(self) -> 'element':
        if not self._enqueue.empty():
            return self._enqueue.max() if self._dequeue.empty() else max(self._enqueue.max(), self._dequeue.max())
        return self._dequeue.max()
