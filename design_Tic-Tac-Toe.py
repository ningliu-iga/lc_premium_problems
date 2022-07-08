from typing import List


# build a n*n grid, after placing the move, check if current row has all the marks from the current player,
# also check current column, diagonal, and back diagonal
class TicTacToe1:
    def __init__(self, n):
        self.grid = [[''] * n for _ in range(n)]

    # O(n) time, O(n^2) space
    def move(self, row, col, player):
        mark = 'x' if player == 1 else 'o'
        self.grid[row][col] = mark
        n = len(self.grid)
        check_row = sum(self.grid[row][i] == mark for i in range(n))
        check_col = sum(self.grid[i][col] == mark for i in range(n))
        check_diag1 = sum(self.grid[i][i] == mark for i in range(n)) if row == col else 0
        check_diag2 = sum(self.grid[i][n - 1 - i] == mark for i in range(n)) if row + col == n - 1 else 0
        return player if check_row == n or check_col == n or check_diag1 == n or check_diag2 == n else 0


class TicTacToe:
    def __init__(self, n):
        self.rows, self.cols, self.diag1, self.diag2, self.n = [0] * n, [0] * n, 0, 0, n

    # assign the value of 1 for player 1 and -1 for player 2
    # O(1) time, O(n) space
    def move(self, row, col, player):
        offset = 1 if player == 1 else -1
        self.rows[row] += offset
        self.cols[col] += offset
        if row == col:
            self.diag1 += offset
        if row + col == self.n - 1:
            self.diag2 += offset
        if self.n in (self.rows[row], self.cols[col], self.diag1, self.diag2):
            return 1
        elif -self.n in (self.rows[row], self.cols[col], self.diag1, self.diag2):
            return 2
        else:
            return 0


if __name__ == '__main__':
    toe = TicTacToe(3)
    out = []
    out += toe.move(0, 0, 1), toe.move(0, 2, 2), toe.move(2, 2, 1), \
           toe.move(1, 1, 2), toe.move(2, 0, 1), toe.move(1, 0, 2), \
           toe.move(2, 1, 1)

    expect = [0,0,0,0,0,0,1]
    if expect == out:
        print('Accepted')
    else:
        print('Wrong')
        print(out)
