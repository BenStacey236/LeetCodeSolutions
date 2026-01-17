# Medium Problem
# Problem 198

from typing import List
from collections import defaultdict

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    memo = defaultdict(lambda: 0)
    memo[0] = nums[0]
    memo[1] = nums[1]

    for house in range(2, len(nums)):
        memo[house] = max(nums[house] + memo[house-2], nums[house] + memo[house-3])

    return max(memo[len(nums)-1], memo[len(nums)-2])


if __name__ == "__main__":
    input1 = [1,2,3,1]
    input2 = [2,7,9,3,1]

    print(rob(input1))
    print(rob(input2))