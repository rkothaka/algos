class TicTacToe:
    EMPTY_SLOT = '_'
    PLAYER_1_SYMBOL = 'X'
    PLAYER_2_SYMBOL = 'O'
    PLACEMENT = [EMPTY_SLOT, PLAYER_1_SYMBOL, PLAYER_2_SYMBOL]

    def __init__(self, n: int):
        self.n = n
        self.board = [[self.EMPTY_SLOT for _ in range(n)] for _ in range(n)]
        self.num_moves = 0

    def is_full(self):
        return self.num_moves == self.n ** 2

    def winner_found(self, row, col):
        return any(self.check_row(row), self.check_col(col), self.check_diagonal(row, col))

    def check_row(self, row):
        first = self.board[row][0]
        if first == self.EMPTY_SLOT:
            return False

        for col in range(1, self.n):
            if first != self.board[row][col]:
                return False
        return True

    def check_col(self, col):
        first = self.board[0][col]
        if first == self.EMPTY_SLOT:
            return False

        for row in range(1, self.n):
            if first != self.board[row][col]:
                return False
        return True

    def check_diagonal(self, row, col):
        if row != col:
            return False

        first = self.board[0][0]
        if first == self.EMPTY_SLOT:
            return False

        for i in range(1, self.n):
            if first != self.board[i][i]:
                return False
        return True

    # TODO diagonal2

    def move(self, row: int, col: int, player: int) -> int:
        if self.is_full():
            return 0

        if self.board[row][col] == self.EMPTY_SLOT:
            self.board[row][col] = self.PLACEMENT[player]
            self.num_moves += 1

        return 1 if self.winner_found() else 0
