# Medium Problem
# Problem 198

from typing import List
from collections import defaultdict

def rob(nums: List[int]) -> int:
        
    if len(nums) == 1:
        return nums[0]

    skipped = 0
    prev = nums[0]

    for i in range(1, len(nums)):
        skipped, prev = prev, max(prev, nums[i] + skipped)

    return prev


if __name__ == "__main__":
    input1 = [1,2,3,1]
    input2 = [2,7,9,3,1]

    print(rob(input1))
    print(rob(input2))