# Medium Problem
# Problem 153

def findMin(nums: list[int]) -> int:
    for i in range(len(nums) - 2):
        if nums[i] > nums[i+1]:
            return nums[i+1]
        
    return nums[0]


input = [5, 6, 7, 0, 1, 2, 3, 4]

if __name__ == "__main__":
    print(findMin(input))