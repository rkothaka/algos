from typing import List


def num_inversions(arr: List[int]) -> int:
    aux_arr = [0] * len(arr)

    def sub_problem(left, right):
        if left == right:
            return 0

        mid = left + (right - left) // 2
        num_inversions_left = sub_problem(left, mid)
        num_inversions_right = sub_problem(mid + 1, right)
        num_split_inversions = merge(left, mid, right)

        return num_inversions_left + num_inversions_right + num_split_inversions

    def merge(left: int, mid: int, right: int):
        count_inversions = 0
        aux_arr[left: right + 1] = arr[left: right + 1].copy()
        left_pt, right_pt = left, mid + 1
        current = left

        while left_pt <= mid and right_pt <= right:
            if aux_arr[left_pt] <= aux_arr[right_pt]:
                arr[current] = aux_arr[left_pt]
                left_pt += 1
            else:
                arr[current] = aux_arr[right_pt]
                right_pt += 1
                count_inversions += (mid - left + 1)
            current += 1

        while left_pt <= mid:
            arr[current] = aux_arr[left_pt]
            left_pt += 1
            current += 1
        while right_pt <= right:
            arr[current] = aux_arr[right_pt]
            right_pt += 1
            current += 1

        return count_inversions

    return sub_problem(0, len(arr) - 1)


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(arr)
    print(arr, num_inversions(arr))

    arr = [6, 5, 4, 3, 2, 1]
    print(arr)
    print(arr, num_inversions(arr))

    arr = [5, 1, 2, 3]
    print(arr)
    print(arr, num_inversions(arr))

    arr = [2, 1, 4, 3, -1]
    print(arr)
    print(arr, num_inversions(arr))

