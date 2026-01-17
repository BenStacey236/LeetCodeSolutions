# Easy Problem
# Problem 746

from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    memo = {0: cost[0], 1: cost[1]}

    for floor in range(2, len(cost)):
        
        floorCost = min(cost[floor] + memo[floor - 1], cost[floor] + memo[floor - 2])
        
        memo[floor] = floorCost

    return min(memo[len(cost)-1], memo[len(cost)-2])


if __name__ == "__main__":
    stairs = [1,100,1,1,1,100,1,1,100,1]

    print(minCostClimbingStairs(stairs))