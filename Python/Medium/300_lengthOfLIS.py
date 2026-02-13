# Medium Problem
# Problem 300

from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    
    numsLen = len(nums)
    memo: dict[int, int] = {}

    def longestSub(index: int, length: int, prev: int = None) -> int:
        
        if index >= numsLen:
            return length

        if index in memo:
            return memo[index] + length
        
        maxLen = length
        for i in range(index+1, numsLen):
            if nums[i] <= nums[index]:
                continue

            maxLen = max(maxLen, longestSub(i, 1, nums[index]))

        memo[index] = maxLen
        return length + maxLen

    maxLen = 0
    for i in range(numsLen):
        maxLen = max(maxLen, longestSub(i, 1))

    return maxLen - 1