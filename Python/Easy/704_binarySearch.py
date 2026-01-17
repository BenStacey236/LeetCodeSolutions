# Easy Problem
# Problem 704

def search(nums: list[int], target: int) -> int:
    frontP, backP = 0, len(nums) - 1

    while frontP <= backP:
        mid = (frontP + backP) // 2
        print(frontP, backP, mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            frontP = mid + 1
        else:
            backP = mid - 1

    return -1


input = [-1,0,3,5,9,12]
target = 2

if __name__ == "__main__":
    print(search(input, target))