# Medium Problem

def productExceptSelfNoDiv(nums: list[int]) -> list[int]:
    prefixes = [1]
    suffixes = []

    for i, num in enumerate(nums):
        posti = len(nums) - i - 1
        if i != 0:
            prefixes.append(prefixes[i] * num)
        else:
            prefixes.append(num)

        if posti != (len(nums) - 1):
            suffixes.append(suffixes[i-1] * nums[posti])
        else:
            suffixes.append(nums[posti])

    suffixes = [1] + list(reversed(suffixes)) + [1]

    return [prefixes[i-1]*suffixes[i+1] for i in range(1, len(nums)+1)]


input = [1,2,3,4]

if __name__ == "__main__":
    print(productExceptSelfNoDiv(input))