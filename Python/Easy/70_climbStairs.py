# Easy Problem
# Problem 70

def climbStairs(n: int) -> int:

    memo: dict[int, int] = {}

    def combinations(level: int) -> int:

        if level in memo:
            return memo[level]

        if level == 1:
            return 1

        if level == 2:
            return 2

        res = combinations(level-1) + combinations(level-2)
        memo[level] = res
        return res

    return combinations(n)


if __name__ == "__main__":

    print(climbStairs(4))