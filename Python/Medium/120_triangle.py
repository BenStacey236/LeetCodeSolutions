# Medium Problem
# Problem 120

from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    
    levels = len(triangle)
    memo: dict[tuple[int, int], int] = {}

    def explorePaths(level: int, i: int) -> int:

        if (level, i) in memo:
            return memo[(level, i)]

        if level == levels-1:
            return triangle[level][i]

        left = explorePaths(level + 1, i)
        right = explorePaths(level + 1, i + 1)

        res = triangle[level][i] + min(left, right)
        memo[(level, i)] = res
        return res

    return explorePaths(0, 0)
