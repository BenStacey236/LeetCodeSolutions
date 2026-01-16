# Medium Problem
# Problem 216

from typing import List

def combinationSum3(k: int, n: int) -> List[List[int]]:

    def backtrack(index: int, path: List[int]) -> None:
        
        if len(path) == k and sum(path) == n:
            res.add(tuple(path))
            return

        start = 1 if not path else path[-1]
        for num in range(start, 10):

            if num not in path:
                path.append(num)
                backtrack(index + 1, path)
                path.pop()
        
    res = set()

    backtrack(0, [])

    return [list(combo) for combo in res]


if __name__ == "__main__":
    
    k = 3
    n = 7

    print(combinationSum3(k, n))