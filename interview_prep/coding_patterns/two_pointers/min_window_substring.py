"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
"""


from collections import Counter


def minimum_window(s: str, t: str) -> str:
    char_count_s = Counter(s)
    char_count_t = Counter(t)

    if not char_count_t or char_count_t - char_count_s:
        return ""

    left, right = 0, 0
    smallest_substring = None
    char_count_substring = Counter(s[0])

    if not char_count_t - char_count_substring:
        smallest_substring = s[0]
        return smallest_substring

    while right + 1 < len(s):
        while right + 1 < len(s) and char_count_t - char_count_substring:
            right += 1
            char_count_substring[s[right]] += 1
        while left <= right and not char_count_t - char_count_substring:
            char_count_substring[s[left]] -= 1
            left += 1

            if not smallest_substring or len(smallest_substring) > right - left + 2:
                smallest_substring = s[left - 1: right + 1]

    return smallest_substring


if __name__ == "__main__":
        print(minimum_window("cabwefgewcwaefgcf", "cae"))
