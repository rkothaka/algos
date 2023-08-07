from typing import List


def get_max_trapped_water(heights: List[int]) -> int:
    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))

        if heights[i] > heights[j]:
            j -= 1
        else:
            i += 1

    return max_water
