from typing import Optional
from list_node import ListNode


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    it = L
    while it:
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = not next_distinct
        it.next = next_distinct
        it = next_distinct
    return L
