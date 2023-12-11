from typing import List


def findMin(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[0] > nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return nums[left]


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(findMin(nums))
