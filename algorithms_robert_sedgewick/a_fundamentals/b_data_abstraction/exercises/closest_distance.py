import math
from random import random
from typing import List


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D(x='{self.x}', y={self.y})"

    def __str__(self):
        return f"Point2D: ({self.x}, {self.y})"


def distance(p1: Point2D, p2: Point2D) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def closest_distance(n: int) -> float:
    """
    :param n: creates n random points in unit square
    :return: distance separating the closest pair of points
    """
    if n < 2:
        raise ValueError("At least two points are required to find the closest pair.")
    points = [Point2D(random(), random()) for _ in range(n)]

    def closest_among_three(points_arr):
        assert len(points_arr) == 3
        d1 = distance(points_arr[0], points_arr[1])
        d2 = distance(points_arr[0], points_arr[2])
        d3 = distance(points_arr[1], points_arr[2])

        return min(d1, d2, d3)

    def closest_recursive(points_sorted_x: List[Point2D], points_sorted_y: List[Point2D]) -> float:
        num = len(points_sorted_x)

        # Base Cases
        if num == 2:
            return distance(points_sorted_x[0], points_sorted_x[1])
        elif num == 3:
            return closest_among_three(points_sorted_x)
        else:
            # Divide
            print(len(points_sorted_x), len(points_sorted_y))
            mid_point = points_sorted_x[num // 2]

            left_half_x = points_sorted_x[:num // 2]
            right_half_x = points_sorted_x[num // 2:]

            left_half_y = [p for p in points_sorted_y if p.x < mid_point.x]
            right_half_y = [p for p in points_sorted_y if p.x >= mid_point.x]

            d1 = closest_recursive(left_half_x, left_half_y)
            d2 = closest_recursive(right_half_x, right_half_y)
            d = min(d1, d2)

            # Combine
            strip = [p for p in points_sorted_y if abs(p.x - mid_point.x) < d]
            strip_len = len(strip)

            for i in range(strip_len):
                for j in range(i + 1, min(i + 7, strip_len)):
                    dist = distance(strip[i], strip[j])
                    if dist < d:
                        d = dist

            return d

    points_sorted_x = sorted(points, key=lambda p: p.x)
    points_sorted_y = sorted(points, key=lambda p: p.y)

    min_dist = closest_recursive(points_sorted_x, points_sorted_y)
    return min_dist


print(closest_distance(10))
