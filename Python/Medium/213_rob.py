# Medium Problem
# Problem 213

from typing import List

def rob(nums: List[int]) -> int:
    
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])

    def houseRobber(houses: List[int]) -> int:

        length = len(houses)

        prev = houses[0]
        curr = max(houses[0], houses[1])

        for i in range(2, length):
            new = max(curr, houses[i] + prev)
            prev = curr
            curr = new

        return curr

    return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))
