import math


def compute_GCD(x, y):
    while y:
        x, y = y, x % y
    return abs(x)
