"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    sorted_intervals = sorted(intervals, key=lambda x: x[-1])
    k = float('-inf')
    result: int = 0
    for x, y in sorted_intervals:
        if x >= k:
            k = y
        else:
            result += 1

    return result
