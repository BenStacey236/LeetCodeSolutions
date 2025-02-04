# Easy Problem
# Problem 283

def moveZeroes(nums: list[int]) -> None:
    l, r = 0, len(nums)-1

    while l < r:
        if nums[l] == 0:
            nums.pop(l)
            nums.append(0)

        if nums[r] == 0:
            r -= 1

        else:
            l += 1

        
input = [0]

if __name__ == "__main__":
    moveZeroes(input)
    print(input)