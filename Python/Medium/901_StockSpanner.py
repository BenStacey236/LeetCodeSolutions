# Medium Problem
# Problem 901

from typing import List

class StockSpanner:

    def __init__(self):
        self.prices: List[int] = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        counter: int = 0

        for p in reversed(self.prices):
            if p <= price:
                counter += 1

            else:
                return counter

        return counter