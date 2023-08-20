from list_node import ListNode
from typing import Optional


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(start, finish):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next,
                                                           temp)

    return dummy_head.next
