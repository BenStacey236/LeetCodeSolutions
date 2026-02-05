# Medium Problem
# Problem 200

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    
    visited: set[tuple[int, int]] = set()
    numIslands: int = 0

    def dfs(pos: tuple[int, int]) -> None:
        visited.add(pos)
        x, y = pos

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newX = x + dx
            newY = y + dy
            if 0 <= newX < len(grid[0]) and 0 <= newY < len(grid):
                if (newX, newY) not in visited and grid[newY][newX] == "1":
                    dfs((newX, newY))

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "1" and (x, y) not in visited:
                numIslands += 1
                dfs((x, y))

    return numIslands