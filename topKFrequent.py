# Medium Problem

def topKFrequent(nums: list[int], k: int) -> list[int]:
    numberFrequencies = {number:nums.count(number) for number in set(nums)}

    maxes = []
    for _ in range(0, k):
        maxValue = 0
        for key, value in numberFrequencies.items():
            if value > maxValue:
                maxValue = value
                maxKey = key
            
        maxes.append(maxKey)
        numberFrequencies.pop(maxKey)

    return maxes


if __name__ == "__main__":
    print(topKFrequent([1, 2], 2))
    
    