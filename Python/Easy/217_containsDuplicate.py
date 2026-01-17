# Easy problem
# Problem 217

def containsDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)


if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1]))