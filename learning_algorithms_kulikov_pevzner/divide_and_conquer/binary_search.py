from typing import List


def bsearch(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if target < arr[mid]:
            right = mid - 1
        elif target == arr[mid]:
            return mid
        else:
            left = mid + 1

    return -1
