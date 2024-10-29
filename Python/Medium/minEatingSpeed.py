# Medium Problem
# Problem 875

from math import ceil

def minEatingSpeed(piles: list[int], h: int) -> int:
    minK, maxK = 1, max(piles)

    def calcEatingTime(k: int):
        total = 0
        for pile in piles:
            total += ceil(pile / k)
        return total
    
    while minK <= maxK:
        mid = (minK + maxK) // 2
        timeToEat = calcEatingTime(mid)
        if timeToEat > h:
            minK = mid + 1
        else:
            maxK = mid - 1

    return minK


input = [1,1,1,999999999]
hours = 10

if __name__ == "__main__":
    print(minEatingSpeed(input, hours))