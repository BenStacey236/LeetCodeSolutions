# Medium Problem
# Problem 322

from typing import List

def coinChange(coins: List[int], amount: int) -> int:

    minCoin = min(coins)
    memo: dict[int, int] = {coin: 1 for coin in coins}
    memo[0] = 0

    def minForAmount(amount: int) -> int:

        if amount in memo:
            return memo[amount]

        if amount < minCoin:
            return -1

        minAmount = float('inf')
        for coin in coins:
            res = minForAmount(amount-coin)
            if res == -1:
                continue

            numCoins = 1 + res
            if numCoins < minAmount:
                minAmount = numCoins

        if minAmount == float('inf'):
            memo[amount] = -1
            return -1

        memo[amount] = minAmount
        return minAmount

    return minForAmount(amount)


if __name__ == "__main__":

    coins = [1, 2, 5]
    amount = 11
    
    print(coinChange(coins, amount))