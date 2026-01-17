# Easy Problem
# Problem 136

from typing import List

def singleNumber(nums: List[int]) -> int:
    
    once = set()
    twice = set()

    for num in nums:
        if num in once:
            twice.add(num)

        once.add(num)

    return once.difference(twice).pop()


if __name__ == "__main__":

    values = [4,1,2,1,2]

    print(singleNumber(values))