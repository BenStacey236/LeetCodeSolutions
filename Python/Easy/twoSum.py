# Easy Problem

def twoSum(nums, target):
    values = {}

    for index, num in enumerate(nums):
        difference = target - num
        if difference in values:
            return [index, values[difference]]
        else:
            values[num] = index

            
if __name__ == "__main__":
    print(twoSum([3, 3], 6))