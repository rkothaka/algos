from typing import List


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    else:
        if A[0] == 10:
            A[0] = 1
            A.append(0)
    return A

