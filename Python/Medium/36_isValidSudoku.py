# Medium Problem
# Problem 36

def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        row = [i for i in row if i != '.']
        if len(set(row)) < len(row):
            return False
    
    for num in range(9):
        column = [row[num] for row in board if row[num] != '.']
        if len(set(column)) < len(column):
            return False

    for row in range(3):
        for column in range(3):
            square = [board[r][c] for r in range(row*3, (row+1)*3) for c in range(column*3, (column+1)*3) if board[r][c] != '.']
            if len(set(square)) < len(square):
                return False

    return True


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

if __name__ == "__main__":
    print(isValidSudoku(board))