from typing import List
import random


def sort(nums: List[int]) -> None:
    idx = 0
    while idx < len(nums):
        if nums[idx] - 1 == idx:
            idx += 1
        else:
            nums[idx], nums[nums[idx] - 1] = nums[nums[idx] - 1], nums[idx]


if __name__ == "__main__":
    nums = list(range(10))
    random.shuffle(nums)
    print(nums)
    sort(nums)
    print(nums)
