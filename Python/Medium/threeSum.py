# Medium Problem

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    prev = None
    results = []

    for i, num in enumerate(nums):
        if num > 0:
            return results

        if num == prev:
            continue
        prev = num
        
        target = -num
        frontP, backP = i+1, len(nums) - 1

        while frontP < backP:
            if nums[frontP] + nums[backP] == target:
                results.append([num, nums[frontP], nums[backP]])
                frontP += 1
                while nums[frontP] == nums[frontP - 1] and frontP < backP:
                    frontP += 1
            
            elif nums[frontP] + nums[backP] < target:
                frontP += 1

            else:
                backP -= 1

    return results


input = [-1,0,1,2,-1,-4]

if __name__ == "__main__":
    print(threeSum(input))