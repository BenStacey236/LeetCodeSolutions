# Hard Problem
# Problem 149

from typing import List

def maxPoints(points: List[List[int]]) -> int:

    def explore(startPoint: tuple[int, int], gradient: float) -> int:
        
        nodes = 1

        x1, y1 = startPoint
        for x2, y2 in points:
            if x1 == x2 and y1 == y2:
                continue

            dx = x2 - x1
            if gradient == float('inf') and dx == 0:
                nodes += 1
                continue

            if dx == 0:
                continue

            m = (y2-y1) / dx
            if m == gradient:
                nodes += 1

        return nodes


    maxLine: int = 1

    for x1, y1 in points:
        exploredGradients: set[float] = set()

        for x2, y2 in points:
            if x1 == x2 and y1 == y2:
                continue

            dx = x2 - x1
            if dx != 0:
                gradient = (y2-y1) / dx
            else:
                gradient = float('inf')

            if gradient in exploredGradients:
                continue

            maxLine = max(maxLine, explore((x1, y1), gradient))

    return maxLine