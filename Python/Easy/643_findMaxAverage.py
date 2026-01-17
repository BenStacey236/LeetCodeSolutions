# Easy Problem
# Problem 643


def findMaxAverage(nums: list[int], k: int) -> float:
    maxTotal = total = sum(nums[:k])

    for i in range(1, len(nums)-k+1):
        total -= nums[i-1]
        total += nums[i+k-1]
        maxTotal = max(total, maxTotal)

    return maxTotal / k


input = [1,12,-5,-6,50,3]
k = 4

if __name__ == "__main__":
    print(findMaxAverage(input, k))