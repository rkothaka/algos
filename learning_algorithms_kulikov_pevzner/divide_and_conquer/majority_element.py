from typing import List

# check whether a given sequence of numbers contains an element
# that appears more than half of the times


def majority_element(arr: List[int]):
    most_frequent = arr[0]
    count = 1

    for element in arr[1:]:
        if element == most_frequent:
            count += 1
        else:
            if count == 1:
                most_frequent = element
            else:
                count -= 1

    return most_frequent
