# Medium Problem

def topKFrequent1(nums: list[int], k: int) -> list[int]:
    frequencies = [[] for _ in range(len(nums)+1)]
    count = {}

    for num in nums:
        if num in count:
            count[num] = count[num] + 1
        else:
            count[num] = 1
    
    for n, count in count.items():
        frequencies[count].append(n)
    
    result = []
    for freq in reversed(frequencies):
        for n in freq:
            result.append(n)

            if len(result) == k: 
                return result


input = [1, 1, 1, 2, 2, 3]

if __name__ == "__main__":
    print(topKFrequent1(input, 2))
    
    