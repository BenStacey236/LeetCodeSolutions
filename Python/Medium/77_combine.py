# Medium Problem
# Problem 77

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    
    res = []

    def explore(combo: list[int]) -> None:

        if len(combo) == k:
            res.append(combo)
            return

        for i in range(1, n + 1):
            if combo and i <= combo[-1]:
                continue

            explore(combo + [i])

    explore([])

    return res