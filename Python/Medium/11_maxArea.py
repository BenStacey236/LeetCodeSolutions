# Medium Problem
# Problem 11

def maxArea(height: list[int]) -> int:
    frontP, backP = 0, len(height) - 1
    maximumArea = 0

    while frontP < backP:
        area = min(height[frontP], height[backP]) * (backP - frontP)
        maximumArea = max(area, maximumArea)

        if height[frontP] < height[backP]:
            frontP += 1
        elif height[frontP] > height[backP]:
            backP -= 1
        else:
            frontP += 1

    return maximumArea


input = [1,3,2,5,25,24,5]

if __name__ == "__main__":
    print(maxArea(input))