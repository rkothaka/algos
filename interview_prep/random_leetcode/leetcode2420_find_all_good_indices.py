"""
You are given a 0-indexed integer array nums of size n and a positive integer k.

We call an index i in the range k <= i < n - k good if the following conditions are satisfied:

The k elements that are just before the index i are in non-increasing order.
The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.
"""

from typing import List
from collections import deque


def goodIndices(nums: List[int], k: int) -> List[int]:
    deq = deque()
    n = len(nums)
    res = [[-1 for _ in range(2)] for _ in range(n)]

    for i in range(n):
        while deq and deq[0] < i - k:
            deq.popleft()

        if deq:
            res[i][0] = deq[0]
        else:
            res[i][0] = i

        if deq and nums[deq[-1]] < nums[i]:
            deq.clear()
        deq.append(i)

    deq.clear()

    for i in range(n - 1, -1, -1):
        while deq and deq[0] > i + k:
            deq.popleft()

        if deq:
            res[i][1] = deq[0]
        else:
            res[i][1] = i

        if deq and nums[deq[-1]] < nums[i]:
            deq.clear()

        deq.append(i)

    ans = []
    for i in range(n):
        if i - res[i][0] >= k and res[i][1] - i >= k:
            ans.append(i)

    return ans
