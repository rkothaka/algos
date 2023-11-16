from typing import Optional
from collections import Counter


def longest_substring_with_k_distinct_characters(some_string: str, k: int) -> Optional[str]:
    if k < 0:
        raise ValueError("Invalid argument: k must be a positive integer")
    if k >= len(some_string):
        return some_string
    if k <= 1:
        return some_string[:k]

    my_counter = Counter()
    left = right = 0
    result = ""
    while right < len(some_string):
        my_counter[some_string[right]] += 1

        # if we have more than k distinct chars in current window,
        # then keep sliding left window until we have k distinct
        while len(my_counter) > k:
            c = some_string[left]
            my_counter[c] -= 1
            if my_counter[c] == 0:
                del my_counter[c]

            left += 1

        right += 1

        # check for new longest substring
        if right - left > len(result):
            result = some_string[left: right]

    return result


if __name__ == "__main__":
    assert longest_substring_with_k_distinct_characters("abcdefghij", 4) == "abcd"
    assert longest_substring_with_k_distinct_characters("zyababccdddeae", 4) == "ababccddd"
    assert longest_substring_with_k_distinct_characters("zyababccd", 4) == "yababcc"
