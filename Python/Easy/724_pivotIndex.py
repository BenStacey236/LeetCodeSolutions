# Easy Problem
# Problem 724

def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    currentTotal = 0
    
    for i, num in enumerate(nums):
        if currentTotal == total-currentTotal-num:
            return i
        
        else:
            currentTotal += num
        
    return -1


input = [1,7,3,6,5,6]

if __name__ == "__main__":
    print(pivotIndex(input))