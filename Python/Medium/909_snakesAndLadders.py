# Medium Problem
# Problem 909

from typing import List

def snakesAndLadders(board: List[List[int]]) -> int:
    
    n = len(board)
    nSquared = n ** 2
    toVisit: list[tuple[int, int]] = [(1, 0)]
    visited: set[tuple[int, int]] = set()

    def cellToPos(cell: int) -> tuple[int, int]:
        
        y = ((cell-1) // n)

        if y % 2 == 0:
            x = ((cell-1) % n)
        else:
            x = n - ((cell-1) % n) - 1

        return (x, n-y-1)

    def bfs(square: tuple[int, int]) -> None:
        cell, numRolls = square

        visited.add(cell)

        for roll in range(1,7):
            newCell = cell + roll
            if newCell > nSquared:
                break

            x, y = cellToPos(newCell)
            if board[y][x] != -1:
                newCell = board[y][x]

            toVisit.append((newCell, numRolls + 1))


    while toVisit:

        cell, rolls = toVisit.pop(0)

        if cell in visited:
            continue

        if cell == nSquared:
            return rolls

        bfs((cell, rolls))

    return -1