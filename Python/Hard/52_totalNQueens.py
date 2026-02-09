# Hard Problem
# Problem 52

from typing import List


def print_board(board: List[List[int]]) -> None:
    for row in board:
        for cell in row:
            print(cell, end="")
        print()

    print()


def totalNQueens(n: int) -> int:

    def place_piece(board: List[List[int]], x: int, y: int) -> List[List[int]]:
        newBoard = []
        for r in range(n):
            newRow = []
            for c in range(n):
                if r == y or c == x or abs(r-y) == abs(c-x):
                    newRow.append(1)
                else:
                    newRow.append(board[r][c])
            newBoard.append(newRow)

        return newBoard

    def explore(board: List[List[int]], remaining: int, count: int) -> int:

        if remaining == 0:
            return count + 1

        y = n-remaining
        for x, cell in enumerate(board[y]):
            if cell == 1: continue

            count = explore(place_piece(board, x, y), remaining-1, count)

        return count

    return explore([[0 for _ in range(n)] for _ in range(n)], n, 0)

if __name__ == "__main__":
    
    n = 5
    print(totalNQueens(n))