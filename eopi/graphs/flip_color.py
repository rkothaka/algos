from typing import List
import random


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]

    def flip_color_helper(a: int, b: int) -> None:
        if not (0 <= a < len(image) and 0 <= b < len(image[a]) and image[a][b] != color):
            return

        image[a][b] = ~color
        for next_x, next_y in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
            flip_color_helper(next_x, next_y)

    flip_color_helper(x, y)


def generate_maze(rows: int, cols: int, blocked: float) -> List[List[bool]]:
    maze = [[False for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            maze[row][col] = (random.random() <= blocked)

    return maze


def print_maze(maze: List[List[bool]]):
    for row in maze:
        print(" ".join(str(cell) for cell in row))


if __name__ == '__main__':
    image = generate_maze(5, 5, 0.5)
    print_maze(image)
    print()
    flip_color(2, 2, image)
    print_maze(image)

