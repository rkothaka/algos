"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""


def gcdOfStrings(str1: str, str2: str) -> str:
    last = min(len(str1), len(str2))
    gcd = ""

    def is_divisor(prefix: str, text: str) -> bool:
        if len(text) % len(prefix) != 0:
            return False

        prefix_len = len(prefix)
        for i in range(0, len(text), prefix_len):
            if text[i: i + prefix_len] != prefix:
                return False

        return True

    for i in range(1, last+1):
        prefix = str1[:i]
        if is_divisor(prefix, str1) and is_divisor(prefix, str2):
            gcd = prefix

    return gcd


if __name__ == "__main__":
    str1, str2 = "LEET", "CODE"
    print(gcdOfStrings(str1, str2))
