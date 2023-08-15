from itertools import accumulate


def above_average_subarrays(nums):
    sums = list(accumulate(nums))  # O(n)
    n = len(nums)

    def get_sum(start, end):  # O(1)
        assert 0 <= start <= end < n
        if start == 0:
            return sums[end]
        return sums[end] - sums[start-1]

    def num_count(start, end):  # O(1)
        assert 0 <= start <= end < n
        return end - start + 1

    def get_average(start, end):  # O(1)
        assert 0 <= start <= end < n
        return get_sum(start, end) / num_count(start, end)

    def get_remaining_average(start, end):  # O(1)
        assert 0 <= start <= end < n
        total_sum = sums[n-1]
        remaining_sum = total_sum - get_sum(start, end)
        remaining_count = n - num_count(start, end)

        return 0 if remaining_count == 0 else remaining_sum / remaining_count

    result = []
    for i in range(len(nums)):  # O(n^2)
        for j in range(i, len(nums)):
            if get_average(i, j) > get_remaining_average(i, j):
                result.append([i+1, j+1])

    return result


if __name__ == "__main__":
    A = [3, 4, 2]
    print(above_average_subarrays(A))

