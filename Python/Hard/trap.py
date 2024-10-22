# Hard Problem
# Problem 42

def trap(heights: list[int]) -> int:
    trapped = 0
    maxLefts = {}
    maxRights = {}
    
    maxL = 0
    maxR = 0
    for i, height in enumerate(heights):
        r = len(heights) - i - 1
        maxR = max(maxR, heights[r])
        maxL = max(maxL, height)
        
        maxLefts[i] = maxL
        maxRights[r] = maxR

    for i, height in enumerate(heights):
        toTrap = min(maxLefts[i], maxRights[i]) - height
        if toTrap > 0: trapped += toTrap

    return trapped


input = [0,1,0,2,1,0,1,3,2,1,2,1]

if __name__ == "__main__":
    print(trap(input))