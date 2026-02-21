# Medium Problem
# Problem 55

from typing import List

def canJump(nums: List[int]) -> bool:

    dp: List[bool] = [False] * len(nums)
    dp[0] = True

    for i in range(1, len(nums)):
        print(i)
        for j in range(i-1, -1, -1):
            if j + nums[j] >= i and dp[j]:
                dp[i] = True
                break
                
    return dp[-1]