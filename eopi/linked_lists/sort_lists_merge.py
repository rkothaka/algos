from typing import Optional
from list_node import ListNode


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next

        tail = tail.next

    tail.next = L1 or L2

    return dummy_head.next
