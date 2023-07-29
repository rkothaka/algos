from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def empty(self) -> bool:
        return self.size == 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.empty():
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.empty():
            raise IndexError("Stack is empty. Cannot peek from an empty stack.")
        return self.top.data

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.top
        while current:
            yield current.data
            current = current.next

    def __bool__(self):
        return not self.empty()
