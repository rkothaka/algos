from typing import List, Optional
from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['x', 'y'])


def find_robots(grid: List[List[str]], boundary_constrains: List[int]) -> Optional[List[Coordinate]]:
    """
    :param grid: grid containing: 'X' - Blocker, 'O' - Robot, and 'E' - Empty cell
    :param boundary_constrains: a valid robot should be able to move [t, r, b, l]
    :return: valid robots
    """

    rows, cols = len(grid), len(grid[0])
    top, right, bot, left = range(4)
    constraints_cache = [[[0, 0, 0, 0] for _ in range(cols)] for _ in range(rows)]
    result = []

    # pass 1: left to right
    left_border = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                left_border = 0
            else:
                left_border += 1
            constraints_cache[r][c][left] = left_border
        left_border = 0

    # pass 2: right to left
    right_border = 0
    for r in range(rows):
        for c in range(cols - 1, -1, -1):
            if grid[r][c] == 'X':
                right_border = 0
            else:
                right_border += 1
            constraints_cache[r][c][right] = right_border
        right_border = 0

    # pass 3: left to right
    top_border = 0
    for c in range(cols):
        for r in range(rows):
            if grid[r][c] == 'X':
                top_border = 0
            else:
                top_border += 1
            constraints_cache[r][c][top] = top_border
        top_border = 0

    # pass 4: bot to top
    bot_border = 0
    for c in range(cols):
        for r in range(rows - 1, -1, -1):
            if grid[r][c] == 'X':
                bot_border = 0
            else:
                bot_border += 1
            constraints_cache[r][c][bot] = bot_border

            # Check for valid robots
            if grid[r][c] == 'O' and constraints_cache[r][c] == boundary_constrains:
                result.append([r, c])
        bot_border = 0

    display_twoD_arr(constraints_cache)

    return result if result else None


def display_twoD_arr(twoD_arr):
    for i in range(len(twoD_arr)):
        for j in range(len(twoD_arr[0])):
            print(twoD_arr[i][j], end='|')
        print()


if __name__ == "__main__":
    grid = [['O', 'E', 'E', 'E', 'X'], ['E', 'E', 'X', 'X', 'X'], ['E', 'O', 'X', 'O', 'E'],
            ['X', 'E', 'O', 'X', 'E'], ['E', 'E', 'X', 'X', 'X']]

    display_twoD_arr(grid)
    border_constraints = [3, 1, 3, 2]  # [t, r, b, l]

    print(find_robots(grid, border_constraints))
