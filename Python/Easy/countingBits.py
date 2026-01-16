# Easy Problem
# Problem 338

from typing import List

def countBits(n: int) -> List[int]:
    
    res = []

    for num in range(n + 1):
        ones = 0

        binary = bin(num)[2:]
        for i in binary:
            if i == '1':
                ones += 1

        res.append(ones)

    return res



if __name__ == "__main__":

    n = 5

    print(countBits(n))