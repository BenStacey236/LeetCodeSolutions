# Medium Problem

def longestConsecutiveFast(nums: list[int]) -> int:
    starts = []
    numsSet = set(nums)

    for num in numsSet:
        if (num-1) not in numsSet:
            starts.append(num)

    maxLength = 0
    for start in starts:
        length = 1
        current = start
        while True:
            if current + 1 in numsSet:
                length += 1
                current += 1
            else:
                break
        
        if length > maxLength: maxLength = length

    return maxLength


input = [0,3,7,2,5,8,4,6,0,1]

if __name__ == "__main__":
    print(longestConsecutiveFast(input))