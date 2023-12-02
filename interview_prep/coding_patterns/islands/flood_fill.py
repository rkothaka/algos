from typing import NamedTuple, Deque, List, Set
from collections import deque


class Location(NamedTuple):
    row: int
    column: int


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def successors(loc: Location, pixel_val: int) -> List[Location]:
            locations: List[Location] = []

            if loc.row + 1 < len(image) and image[loc.row + 1][loc.column] == pixel_val:
                locations.append(Location(loc.row + 1, loc.column))
            if loc.row - 1 >= 0 and image[loc.row - 1][loc.column] == pixel_val:
                locations.append(Location(loc.row - 1, loc.column))

            if loc.column + 1 < len(image[0]) and image[loc.row][loc.column + 1] == pixel_val:
                locations.append(Location(loc.row, loc.column + 1))
            if loc.column - 1 >= 0 and image[loc.row][loc.column - 1] == pixel_val:
                locations.append(Location(loc.row, loc.column - 1))

            return locations

        def flood_fill_helper(start: Location) -> None:
            # explored is where we've been
            explored: Set[Location] = set()
            pixel_color = image[start.row][start.column]

            # frontier is where we've yet to go
            frontier: Deque[Location] = deque()
            frontier.append(start)

            # iterate through each island start
            while frontier:
                current_loc: Location = frontier.pop()
                image[current_loc.row][current_loc.column] = color

                # check where we can go next and haven't explored
                for child in successors(current_loc, pixel_color):
                    if child in explored:  # skip children we already explored
                        continue
                    explored.add(child)
                    frontier.append(child)

        flood_fill_helper(Location(sr, sc))
        return image
