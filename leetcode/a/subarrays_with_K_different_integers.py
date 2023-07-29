from collections import deque
import heapq
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        result = 0
        counter = {}

        left = 0
        for right in range(len(nums)):
            if nums[right] in counter:
                counter[nums[right]].append(right)
            else:
                counter[nums[right]] = deque([right])

            while len(counter) > k:
                counter[nums[left]].popleft()
                if not counter[nums[left]]:
                    del counter[nums[left]]

                left += 1

            if len(counter) == k:
                min_right = min(q[-1] for q in counter.values())
                min_right = min_right + 1 if right - k >= min_right else right
                result += (min_right - left - k + 2)

        return result


solution = Solution()
print(solution.subarraysWithKDistinct([2,2,1,2,2,2,1,1], 2))
