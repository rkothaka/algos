from typing import List


def can_reach_end(A: List[int]) -> bool:
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, i + A[i])
        i += 1
    return furthest_reach_so_far >= last_index
