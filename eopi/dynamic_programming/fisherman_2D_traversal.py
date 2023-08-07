import functools
from typing import List
import random


def max_fish_caught(grid: List[List[int]]) -> (int, str):
    @functools.lru_cache(None)
    def max_fish(x, y):
        if x == y == 0:
            return grid[x][y], ''

        if x == 0:
            fish_left, path_left = max_fish(x, y - 1)
            return grid[x][y] + fish_left, path_left + 'L'
        elif y == 0:
            fish_top, path_top = max_fish(x - 1, y)
            return grid[x][y] + fish_top, path_top + 'T'
        else:
            fish_top, path_top = max_fish(x - 1, y)
            fish_left, path_left = max_fish(x, y - 1)
            if fish_top > fish_left:
                return grid[x][y] + fish_top, path_top + 'T'
            else:
                return grid[x][y] + fish_left, path_left + 'L'

    final_fish_count, final_path = max_fish(len(grid) - 1, len(grid[0]) - 1)
    return final_fish_count, final_path[::-1]


if __name__ == '__main__':
    rows = 10
    cols = 8
    grid = [[0 if random.random() < 0.5 else random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    for row in grid:
        print(row)

    print(max_fish_caught(grid))
