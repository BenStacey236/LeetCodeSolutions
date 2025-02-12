# Easy Problem
# Problem 2215

from collections import Counter

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    nums1Dict = Counter(nums1)
    nums2Set = set()

    for num in nums2:
        if num in nums1Dict and nums1Dict[num] > 0:
            nums1Dict[num] = 0
        
        elif num not in nums1Dict:
            nums2Set.add(num)

    return [[num for (num, count) in nums1Dict.items() if count > 0], list(nums2Set)]



nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

if __name__ == "__main__":
    print(findDifference(nums1, nums2))