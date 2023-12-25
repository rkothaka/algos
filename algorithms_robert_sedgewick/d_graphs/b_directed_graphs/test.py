def is_valid(x, y, grid):
    # Check if the given coordinates are within the grid boundaries
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def dfs(x, y, grid, distances):
    if not is_valid(x, y, grid):
        return

    if distances[x][y] != float('inf'):
        return

    distances[x][y] = 0

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, grid) and grid[new_x][new_y] != 1:
            dfs(new_x, new_y, grid, distances)
            distances[x][y] = min(distances[x][y], distances[new_x][new_y] + 1)


def compute_distances(grid):
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Blocker cell
                dfs(i, j, grid, distances)

    return distances


# Example usage
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]

distances = compute_distances(grid)
for row in distances:
    print(row)
