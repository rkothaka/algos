from typing import List
import heapq


# Merge k sorted arrays & output should not have duplicates.
def merge_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    iterators = [iter(x) for x in arrays]

    min_heap = []
    for idx, it in enumerate(iterators):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, idx))

    result = []
    while min_heap:
        smallest_entry, idx = heapq.heappop(min_heap)
        smallest_array_iter = iterators[idx]
        if not result or result[-1] != smallest_entry:
            result.append(smallest_entry)

        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, idx))

    return result


if __name__ == "__main__":
    import random
    arrays = []
    for _ in range(3):
        array = [random.randint(-3, 2) for _ in range(random.randint(5, 10))]
        array.sort()
        arrays.append(array)

    print(arrays)
    print(merge_sorted_arrays(arrays))


