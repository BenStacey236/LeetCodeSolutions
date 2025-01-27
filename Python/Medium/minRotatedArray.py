# Medium Problem
# Problem 153

def findMin(nums: list[int]) -> int:
    frontP, backP = 0, len(nums) - 1

    while frontP < backP:
        mid = (frontP + backP) // 2
        if nums[mid] < nums[frontP]:
            backP = mid - 1
        else:
            frontP = mid + 1

    return nums[frontP]


input = [7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6]

if __name__ == "__main__":
    print(findMin(input))