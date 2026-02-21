# Easy Problem
# Problem 169

from typing import List

def majorityElement(nums: List[int]) -> int:
    res, count = 0, 0

    for num in nums:
        if count == 0:
            res = num
            count = 1
            continue

        if num == res:
            count += 1

        else:
            count -= 1

    return res