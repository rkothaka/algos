from __future__ import annotations

from typing import TypeVar, Generic


T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T = None, next_node: Node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node({self.data!r})"

    def print_list(self):
        current_node = self
        while current_node:
            end_char = " | " if current_node.next_node else "\n"
            print(current_node.data, end=end_char)
            current_node = current_node.next_node


def find_mid(head: Node):
    dummy_node = Node(None, head)
    slow = fast = dummy_node

    while fast.next_node and fast.next_node.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node

    if fast.next_node:
        return slow.next_node
    return slow


if __name__ == "__main__":
    dummy_head = Node(-1, None)
    node = dummy_head
    for val in range(5):
        node.next_node = Node(val, None)
        node = node.next_node

    node = dummy_head.next_node
    node.print_list()
    print(find_mid(dummy_head.next_node))
