from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    length = len(nums)
    result = [0] * length
    left, right = 0, length - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[right - left] = nums[left] * nums[left]
            left += 1
        else:
            result[right - left] = nums[right] * nums[right]
            right -= 1

    return result
