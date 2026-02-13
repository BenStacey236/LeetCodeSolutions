# Medium Problem
# Problem 39

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    
    res: List[List[int]] = []

    def explore(combo: List[int], total: int) -> None:

        if total == target:
            res.append(combo)
            return

        if total >= target:
            return

        for val in candidates:
            if combo and val < combo[-1]:
                continue

            explore(combo + [val], total + val)

    explore([], 0)

    return res