# Easy Problem
# Problem 27

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    
    k = len(nums)

    i = 0
    while True:

        if i >= len(nums):
            return k

        if nums[i] == val:
            nums.pop(i)
            k -= 1
            i -= 1

        i += 1

    return k