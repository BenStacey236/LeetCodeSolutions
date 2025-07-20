# Medium Problem
# Problem 215

from typing import List
from queue import PriorityQueue

def findKthLargest(nums: List[int], k: int) -> int:
    pQueue = PriorityQueue(maxsize=k)

    for num in nums:
        if not pQueue.full():
            pQueue.put_nowait(num)

        else:
            bottom = pQueue.get_nowait()

            if num > bottom:
                pQueue.put_nowait(num)
            else:
                pQueue.put_nowait(bottom)

    return pQueue.get_nowait()


if __name__ == "__main__":
    print(findKthLargest([3,2,1,5,6,4], 2))