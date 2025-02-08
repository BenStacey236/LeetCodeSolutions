# Medium Problem
# Problem 1679


def maxOperations(nums: list[int], k: int) -> int:
    values = {}
    numOperations = 0

    for num in nums:
        difference = k - num
        if difference in values and values[difference] != 0:
            numOperations += 1
            values[difference] -= 1
        elif num in values:
            values[num] += 1
        else:
            values[num] = 1

    return numOperations


input = [2,2,2,3,1,1,4,1]
k = 4

if __name__ == "__main__":
    print(maxOperations(input, k))