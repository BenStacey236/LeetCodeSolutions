# Medium Problem
# Problem 209

from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    
    l, r = 0, 0

    total = sum(nums[l:r+1])
    minSize = float('inf')
    while r < len(nums):
        if total < target:
            r += 1
            if r >= len(nums):
                break
            total += nums[r]

        else:
            minSize = min(minSize, r-l+1)
            total -= nums[l]
            l += 1

    return minSize if minSize != float('inf') else 0


if __name__ == "__main__":

    target = 15
    nums = [1, 2, 3, 4, 5]

    print(minSubArrayLen(target, nums))