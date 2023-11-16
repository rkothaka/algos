def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # drops the lowest set bit of x
    return result

