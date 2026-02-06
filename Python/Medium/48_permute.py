# Medium Problem
# Problem 48

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    
    res = []
    
    def explore(perm: List[int], remaining: List[int]) -> None:

        if not remaining:
            res.append(perm)
            return

        for val in remaining:
            rem = remaining.copy()
            rem.remove(val)
            explore(perm + [val], rem)

    explore([], nums)

    return res