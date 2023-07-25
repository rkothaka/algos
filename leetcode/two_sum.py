from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen.get(target - num), i]
            seen[num] = i
