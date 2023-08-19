from typing import Optional


def can_win(pile1: int, pile2: int) -> Optional[bool]:
    rows, cols = pile1 + 1, pile2 + 1

    result = [[None for _ in range(cols)] for _ in range(rows)]
    # base cases
    result[1][0] = result[1][1] = result[0][1] = True
    result[2][0] = result[0][2] = False

    def dp(i, j):
        if result[i][j] is not None:
            return result[i][j]

        result[i][j] = not all(dp(x, y) for x, y in
                               zip((i - 1, i, i - 1), (j, j - 1, j - 1))
                               if x >= 0 and y >= 0)
        return result[i][j]

    dp(rows - 1, cols - 1)
    return result[rows - 1][cols - 1]


if __name__ == "__main__":
    print(can_win(10, 10))
