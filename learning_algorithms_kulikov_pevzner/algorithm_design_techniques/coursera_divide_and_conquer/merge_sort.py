from typing import List


def merge_sort(arr: List[int]):
    n = len(arr)
    aux_arr = [-1] * n

    def merge_sort_helper(left, right):
        if left >= right:
            return

        middle = left + (right - left) // 2
        merge_sort_helper(left, middle)
        merge_sort_helper(middle + 1, right)

        merge(left, middle, right)

    def merge(left: int, mid: int, right: int):
        aux_arr[left: right + 1] = arr[left: right + 1].copy()
        left_pt, right_pt = left, mid+1
        current = left

        while left_pt <= mid and right_pt <= right:
            if aux_arr[left_pt] <= aux_arr[right_pt]:
                arr[current] = aux_arr[left_pt]
                left_pt += 1
            else:
                arr[current] = aux_arr[right_pt]
                right_pt += 1
            current += 1

        while left_pt <= mid:
            arr[current] = aux_arr[left_pt]
            left_pt += 1
            current += 1
        while right_pt <= right:
            arr[current] = aux_arr[right_pt]
            right_pt += 1
            current += 1

    merge_sort_helper(0, len(arr) - 1)


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 20) for _ in range(10)]
    print(arr)
    merge_sort(arr)
    print(arr)
