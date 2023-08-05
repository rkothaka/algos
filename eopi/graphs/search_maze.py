import collections
from typing import List
import random

WHITE, BLACK = range(2)
Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate, e: Coordinate) -> List[Coordinate]:
    def search_maze_helper(cur):
        # checks cur is within maze and is a white pixel
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        if any(
                map(
                    search_maze_helper,
                    map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x),
                        (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
            return True

        del path[-1]
        return False

    path: List[Coordinate] = []
    search_maze_helper(s)
    return path


def generate_maze(rows: int, cols: int, blocked: float) -> List[List[int]]:
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if random.random() <= blocked:
                maze[row][col] = 1

    return maze


def print_maze(maze: List[List[int]]):
    for row in maze:
        print(" ".join(str(cell) for cell in row))


if __name__ == '__main__':
    maze = generate_maze(5, 5, 0.3)
    print_maze(maze)
    path = search_maze(maze, Coordinate(0, 0), Coordinate(4, 4))
    print(path)
