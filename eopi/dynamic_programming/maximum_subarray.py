import collections
from typing import List


MaxValueLoc = collections.namedtuple('MaxValueLoc', ('value', 'location'))


def find_maximum_subarray(A: List[int]) -> MaxValueLoc:  # O(n log n)

    def find_max_crossing_subarray(start: 'idx', mid: 'idx', end: 'idx'):
        left_sum = float("-inf")
        sum = 0
        max_left = mid

        for i in range(mid, start - 1, -1):
            sum += A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = float("-inf")
        sum = 0
        max_right = mid + 1

        for i in range(mid + 1, end + 1):
            sum += A[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i

        return MaxValueLoc(left_sum + right_sum, (max_left, max_right))

    def fms_recursive(start: 'idx', end: 'idx'):
        if start == end:
            return MaxValueLoc(A[start], (start, end))

        mid = start + (end - start) // 2
        L = fms_recursive(start, mid)
        R = fms_recursive(mid + 1, end)
        C = find_max_crossing_subarray(start, mid, end)

        if L.value >= R.value and L.value >= C.value:
            return L
        elif R.value >= L.value and R.value >= C.value:
            return R
        else:
            return C

    return fms_recursive(0, len(A) - 1)


def find_maximum_subarray_dp(A: List[int]) -> MaxValueLoc:
    max_seen = max_end = MaxValueLoc(0, (0, 0))

    for idx, a in enumerate(A):
        max_end = MaxValueLoc(a, (idx, idx)) if a > max_end.value + a \
            else MaxValueLoc(max_end.value + a, (max_end.location[0], idx))
        max_seen = max_seen if max_seen.value > max_end.value else max_end

    return max_seen


if __name__ == "__main__":
    import random
    random_arr = [[random.randint(-10, 10) for _ in range(random.randint(5, 10))] for _ in range(5)]

    for arr in random_arr:
        print(arr)
        result1 = find_maximum_subarray(arr)
        result2 = find_maximum_subarray_dp(arr)
        print(result2)
        assert result1 == result2
