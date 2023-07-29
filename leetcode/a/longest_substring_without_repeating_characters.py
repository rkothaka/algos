class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = -1
        start = 0
        cache = {}
        for cur, char in enumerate(s):
            if char in cache and cache[char] >= start:
                longest = max(longest, cur - start)
                start = cache[char] + 1
            cache[char] = cur

        return max(longest, len(s) - start)
