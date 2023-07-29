from typing import List


def index_of(a: List[int], key: int) -> int:
    """
    :param a: Sorted list of ints
    :param key: key to search if exists
    :return: -1 if key doesn't exist in 'a', else return its index in 'a'
    """
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid

    return -1


# Exercises
# 1.1.28 Remove duplicates
def remove_duplicates(a: List[int]) -> int:
    """

    :param a: Sorted List of ints
    :return: valid elements idx. Elements after the idx can be discarded
    """
    prev = 0
    for item in a:
        if item == a[prev]:
            continue
        else:
            prev += 1
            a[prev] = item

    return prev


# 1.1.29 rank() and count()
def rank(a: List[int], key: int) -> int:
    """
    :param a: Sorted list of ints
    :param key: int
    :return: number of elements that are smaller than key
    """
    lo, hi = 0, len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if key <= a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


def count(a: List[int], key: int) -> int:
    """
    :param a: Sorted list
    :param key: int
    :return: number of elements in "a" equal to key
    """
    lo, hi = 0, len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if key >= a[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    lt = rank(a, key)
    gt = lo

    return gt - lt
