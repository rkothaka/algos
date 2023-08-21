# Input: Positive integer
# Output: the maximum k such that n can be represented as the sum a1 + a2 + ... + ak of k distinct integers.
import math
from collections import deque


# Input 6 -> 3 (1, 2, 3)
# Input 8 -> 3 (1, 2, 5)
# Input 2 -> 1 (2)

def max_number_of_prizes(I: int) -> int:
    assert I >= 1

    return math.floor((math.sqrt(8*I + 1) - 1) / 2)


if __name__ == "__main__":
    print(max_number_of_prizes(2))

