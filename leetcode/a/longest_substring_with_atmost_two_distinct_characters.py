class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest = -1
        cache = {}
        start = 0

        for cur, char in enumerate(s):
            if len(cache) < 2:
                if char not in cache:
                    cache[char] = cur
            elif char in cache:
                if char != s[cur-1]:
                    cache[char] = cur
            else:
                prev_char = s[cur-1]
                for key in list(cache.keys()):
                    if key != prev_char:
                        cache.pop(key)

                longest = max(longest, cur - start)
                start = cache[prev_char]
                cache[char] = cur

        return max(longest, len(s) - start)
