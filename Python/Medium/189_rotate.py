# Medium Problem
# Problem 189

from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]