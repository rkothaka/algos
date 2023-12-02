"""

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


"""

from __future__ import annotations

import random
from collections import deque
from enum import Enum
from typing import TypeVar, Generic, List, Set, Deque, NamedTuple

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = deque()

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        if self.empty:
            raise ValueError('Stack is empty')
        return self._container.popleft()

    def __repr__(self) -> str:
        return repr(self._container)


class Location(NamedTuple):
    row: int
    column: int


class Cell(str, Enum):
    LAND = "1"
    WATER = "0"


class Map:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.29) -> None:
        # initialize basic instance variables
        self._rows: int = rows
        self._columns: int = columns

        # fill the grid with empty cells
        self._grid: List[List[Cell]] = [[Cell.WATER for _ in range(columns)] for _ in range(rows)]
        # populate grid with blocked cells
        self._randomly_fill(rows, columns, sparseness)

    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.LAND

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "|" + "|".join([c.value for c in row]) + "|\n"
        return output

    def successors(self, loc: Location) -> List[Location]:
        locations: List[Location] = []

        if loc.row + 1 < self._rows and self._grid[loc.row + 1][loc.column] != Cell.WATER:
            locations.append(Location(loc.row + 1, loc.column))
        if loc.row - 1 >= 0 and self._grid[loc.row - 1][loc.column] != Cell.WATER:
            locations.append(Location(loc.row - 1, loc.column))

        if loc.column + 1 < self._columns and self._grid[loc.row][loc.column + 1] != Cell.WATER:
            locations.append(Location(loc.row, loc.column + 1))
        if loc.column - 1 >= 0 and self._grid[loc.row][loc.column - 1] != Cell.WATER:
            locations.append(Location(loc.row, loc.column - 1))

        return locations

    def num_islands(self) -> int:
        num_islands = 0

        # explored is where we've been
        explored: Set[Location] = set()

        # iterate through each island start
        for r in range(self._rows):
            for c in range(self._columns):
                cur = Location(r, c)
                if cur not in explored and self._grid[cur.row][cur.column] == Cell.LAND:
                    # Found new un-explored land
                    # print(cur)  # to check when a new island is detected
                    explored.add(cur)
                    num_islands += 1

                    # frontier is where we've yet to go
                    frontier: Queue[T] = Queue()
                    frontier.push(cur)

                    # keep going while there is more to explore for this island
                    while not frontier.empty:
                        current_loc: Location = frontier.pop()

                        # check where we can go next and haven't explored
                        for child in self.successors(current_loc):
                            if child in explored:  # skip children we already explored
                                continue
                            explored.add(child)
                            frontier.push(child)

        return num_islands


if __name__ == "__main__":
    grid = Map(10, 10, 0.7)
    print(grid)
    print(f"number of islands: {grid.num_islands()}")
