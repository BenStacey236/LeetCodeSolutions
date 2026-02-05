# Easy Problem
# Problem 88

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    res = []

    while m or n:
        if not m:
            res.append(nums2.pop(0))
            n -= 1
            continue

        if not n:
            res.append(nums1.pop(0))
            m -= 1
            continue

        if nums1[0] <= nums2[0]:
            res.append(nums1.pop(0))
            m-=1

        else:
            res.append(nums2.pop(0))
            n-=1

    nums1.clear()
    nums1 += res

if __name__ == "__main__":
    
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    n, m = 3, 3
    
    merge(nums1, n, nums2, m)
    print(nums1)