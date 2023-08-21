from typing import List, Optional


def max_pairwise_product(arr: List[int]) -> Optional[int]:
    if len(arr) < 2:
        return None

    first, second = (arr[0], arr[1]) if arr[0] >= arr[1] else (arr[1], arr[0])

    for num in arr[2:]:
        if num > second:
            if num > first:
                second = first
                first = num
            else:
                second = num

    return first * second


if __name__ == "__main__":
    import random
    arr = [random.randint(1, 20) for i in range(7)]
    print(arr, max_pairwise_product(arr))
