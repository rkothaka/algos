from typing import List


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot_val = A[pivot_index]
    # maintaining
    # bottom group: A[:smaller]
    # middle group: A[smaller: equal]
    # unclassified: A[equal: larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot_val:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot_val:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[equal], A[larger]
