# Medium Problem
# Problem 1004

def longestOnes(nums: list[int], k: int) -> int:
    frontP = 0
    backP = 0
    maxLen = 0
    maxK = k

    while backP < len(nums):
        print(f'{nums[frontP:backP]} FRONT:{frontP} BACK:{backP} K={k}, len={backP-frontP}, maxLen={maxLen}')
        if k < 0:
            if nums[frontP] == 0:
                k = min(maxK, k + 1)

            frontP += 1
            continue

        if nums[backP] == 0:
            k -= 1

        if k >= 0: maxLen = max(maxLen, (backP - frontP) + 1)

        backP += 1

    return maxLen


input = [0,0,1,1]
k = 1
input2 = [1,1,1,0,0,0,1,1,1,1,0]
k2 = 2
input3 = [0,0,0,1]
k3 = 4

if __name__ == "__main__":
    print(longestOnes(input, k))
    print(longestOnes(input2, k2))
    print(longestOnes(input3, k3))