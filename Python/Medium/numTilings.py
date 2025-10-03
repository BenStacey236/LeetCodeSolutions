# Medium Problem
# Problem 790

def numTilings(n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        memo[3] = 5

        for i in range(4, n + 1):
            memo[i] = 2 * memo[i-1] + memo[i-3]

        return memo[n] % (10**9 + 7)

if __name__ == "__main__":
    print(numTilings(4))
    print(numTilings(5))