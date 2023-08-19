from typing import List
import random


def quick_sort(arr: List[int]):

    def partition(left, right) -> int:
        pivot_idx = random.randint(left, right)
        pivot_val = arr[pivot_idx]
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

        lt = left
        for idx in range(left, right):
            if arr[idx] < pivot_val:
                arr[lt], arr[idx] = arr[idx], arr[lt]
                lt += 1

        arr[lt], arr[right] = arr[right], arr[lt]

        return lt

    def quick_sort_helper(left, right):
        if left >= right:
            return

        pivot = partition(left, right)
        quick_sort_helper(left, pivot - 1)
        quick_sort_helper(pivot + 1, right)

    quick_sort_helper(0, len(arr) - 1)


if __name__ == "__main__":
    for _ in range(5):
        arr = [random.randint(1, 20) for _ in range(random.randint(1, 15))]
        print(arr)
        quick_sort(arr)
        print(arr, "\n")
