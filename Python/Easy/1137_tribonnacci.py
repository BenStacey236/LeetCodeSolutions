# Easy Problem
# Problem 1137

from collections import defaultdict

def tribonacci(n: int) -> int:
    memo: defaultdict[int, int] = defaultdict(lambda: 0)
    memo[1] = 1
    memo[2] = 1

    for i in range(3, n + 1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[n]


if __name__ == "__main__":
    print(tribonacci(25))