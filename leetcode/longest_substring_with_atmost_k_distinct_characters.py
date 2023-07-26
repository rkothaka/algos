import collections


class Solution:
    # Leetcode solution
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return len(s)

        max_size = 0
        counter = collections.Counter()

        for right in range(n):
            counter[s[right]] += 1

            if len(counter) <= k:
                max_size += 1
            else:
                counter[s[right - max_size]] -= 1
                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]

        return max_size


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstringKDistinct("abaccc", 2))
