# Medium Problem
# Problem 2352

from typing import List

def equalPairs(grid: List[List[int]]) -> int:
    patterns = {}
    pairs = 0

    for row in grid:
        pattern = ','.join([str(i) for i in row])
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1

    for col in range(len(grid)):
        pattern = ','.join([str(row[col]) for row in grid])
        if pattern in patterns:
            pairs += patterns[pattern]

    return pairs


input = [[3,2,1],[1,7,6],[2,7,7]]
input2 = [[13, 13], [13, 13]]

if __name__ == "__main__":
    print(equalPairs(input))
    print(equalPairs(input2))