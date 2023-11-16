from typing import List
import heapq


def kth_largest(arr: List[int], k: int) -> int:
    assert 0 < k <= len(arr)

    k_largest = []
    for num in arr:
        if len(k_largest) < k:
            heapq.heappush(k_largest, num)
        elif len(k_largest) == k and k_largest[0] < num:
            heapq.heapreplace(k_largest, num)

    return k_largest[0]


if __name__ == '__main__':
    arr = [5, 12, 8, 3, 19, 7, 1, 9, 14, 6]
    print(kth_largest(arr, 10))

