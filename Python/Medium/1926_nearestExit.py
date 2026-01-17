# Medium Problem
# Problem 1926

from typing import List

def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    to_visit: List[tuple[int, int]] = [(tuple(entrance), 0)]
    visited: set[tuple[int, int]] = set(tuple(entrance))
    width, height = len(maze[0]) - 1, len(maze) - 1
    
    def isExit(pos: tuple[int, int]) -> bool:
        y, x = pos

        if pos == tuple(entrance):
            return False

        if not 0 <= y <= height:
            return False
        
        if not 0 <= x <= width:
            return False
        
        if maze[y][x] != '.':
            return False
        
        if (x == 0 or x == width) or (y == 0 or y == height):
            return True
        
        return False

    def bfs(node: tuple[tuple[int, int], int]):
        (ny, nx), d = node

        if isExit((ny, nx)):
            return True

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for y, x in directions:
            if 0 <= (nx + x) <= width and 0 <= (ny + y) <= height:
                if maze[ny + y][nx + x] != '.':
                    continue

                if (ny + y, nx + x) not in visited:
                    to_visit.append(((ny + y, nx + x), d + 1))
                    visited.add((ny + y, nx + x))

    while to_visit:
        next = to_visit.pop(0)
        if bfs(next):
            return next[1]
        
    return -1


if __name__ == "__main__":
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]

    print(nearestExit(maze, entrance))