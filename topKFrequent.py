# Medium Problem

def topKFrequent(nums: list[int], k: int) -> list[int]:
    numSet = set(nums)

    while len(numSet) != k:
        toRemove = []
        for item in numSet:
            if item not in nums:
                toRemove.append(item)
            else:
                nums.remove(item)

        for num in toRemove:
            numSet.remove(num)

    return list(numSet)

    
if __name__ == "__main__":
    print(topKFrequent([5,3,1,1,1,3,73,1], 2))
    
    