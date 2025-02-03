# Medium Problem
# Problem 334

import math


def increasingTriplet(nums: list[int]) -> bool:
    l, mid, r = math.inf, math.inf, math.inf
    
    for i, num in enumerate(nums):
        if num > mid:
            return True

        elif num <= l:
            l = num

        else:
            mid = num

    return False