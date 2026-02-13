# Easy Problem
# Problem 66

from typing import List

def plusOne(digits: List[int]) -> List[int]:

    r = len(digits) - 1
    digits[r] += 1

    while r > 0 and digits[r] == 10:
        digits[r] = 0
        r -= 1
        digits[r] += 1

    if digits[0] == 10:
        digits[0] = 0
        return [1] + digits

    return digits