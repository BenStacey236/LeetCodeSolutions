# Medium Problem
# Problem 289

from typing import List

def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    height = len(board)
    width = len(board[0])

    newGrid = []
    for y, row in enumerate(board):
        newRow = []
        for x, cell in enumerate(row):
            
            neighboursAlive = 0
            for nx, ny in [(x-1,y+1), (x,y+1), (x+1,y+1), (x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x+1,y-1)]:

                if 0 <= nx < width and 0 <= ny < height and board[ny][nx] == 1:
                    neighboursAlive += 1
                
            if cell == 1:
                if neighboursAlive < 2 or neighboursAlive > 3:
                    newRow.append(0)

                else:
                    newRow.append(1)

            else:
                if neighboursAlive == 3:
                    newRow.append(1)
                else:
                    newRow.append(0)

        newGrid.append(newRow)

    for bRow, newRow in zip(board, newGrid):
        for (i, _), newCell in zip(enumerate(bRow), newRow):
            bRow[i] = newCell