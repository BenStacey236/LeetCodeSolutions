# Hard Problem
# Problem 42

def trapMemory(heights: list[int]) -> int:
    trapped = 0
    maxL, maxR = 0, 0

    frontP, backP = 0, len(heights) - 1
    while frontP < backP:
        maxL = max(maxL, heights[frontP])
        maxR = max(maxR, heights[backP])

        if heights[frontP] < heights[backP]:
            frontP += 1
            toTrap =  maxL - heights[frontP]
            if toTrap > 0:
                trapped += toTrap

        else:
            backP -= 1
            toTrap = maxR - heights[backP]
            if toTrap > 0:
                trapped += toTrap

    return trapped


input = [0,1,0,2,1,0,1,3,2,1,2,1]

if __name__ == "__main__":
    print(trapMemory(input))