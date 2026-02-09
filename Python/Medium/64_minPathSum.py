# Medium Problem
# Problem 64

from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    
    m, n = len(grid), len(grid[0])
    memo: dict[tuple[int, int], int] = {}

    def explore(x: int, y: int) -> int:
        
        if (x, y) in memo:
            return memo[(x, y)]

        if y == m-1 and x == n-1:
            return grid[y][x]

        down, right = float('inf'), float('inf')
        if y != m-1:
            down = explore(x, y + 1)
        if x != n-1:
            right = explore(x + 1, y)

        res = grid[y][x] + min(down, right)
        memo[(x, y)] = res
        return res

    return explore(0, 0)