# Hard Problem
# Problem 52

from typing import List


def totalNQueens(n: int) -> int:

    def explore(remaining: int, count: int, locations: List[tuple[int, int]]) -> int:

        if remaining == 0:
            return count + 1

        y = n-remaining
        for x in range(n):

            collision = False
            for lx, ly in locations:
                if ly == y or lx == x or abs(ly-y) == abs(lx-x):
                    collision = True
                    break

            if collision:
                continue
            
            count = explore(remaining-1, count, locations + [(x,y)])

        return count

    return explore(n, 0, [])

if __name__ == "__main__":
    
    n = 5
    print(totalNQueens(n))