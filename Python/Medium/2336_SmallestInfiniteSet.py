# Medium Problem
# Problem 2336

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.counter = 1
        self.repushed = []
        self.repushedSet = set()

    def popSmallest(self) -> int:
        if not self.repushed:
            val = self.counter
            self.counter += 1
            return val
        
        minRepushed = heapq.heappop(self.repushed)

        if minRepushed < self.counter:
            self.repushedSet.remove(minRepushed)
            return minRepushed

        elif minRepushed == self.counter:
            self.repushedSet.remove(minRepushed)
            self.counter += 1
            return minRepushed

        else:
            heapq.heappush(self.repushed, minRepushed)
            val = self.counter
            self.counter += 1
            return val


    def addBack(self, num: int) -> None:
        if num not in self.repushedSet:
            heapq.heappush(self.repushed, num)
            self.repushedSet.add(num)


if __name__ == "__main__":
    smallestInfiniteSet = SmallestInfiniteSet()

    print(smallestInfiniteSet.addBack(2))
    print(smallestInfiniteSet.popSmallest())
    print(smallestInfiniteSet.popSmallest())
    print(smallestInfiniteSet.popSmallest())
    print(smallestInfiniteSet.addBack(1))
    print(smallestInfiniteSet.popSmallest())
    print(smallestInfiniteSet.popSmallest())
    print(smallestInfiniteSet.popSmallest())