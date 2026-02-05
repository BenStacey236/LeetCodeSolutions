# Easy Problem
# Problem 141

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    visited: set[ListNode] = set()

    curr = head
    while curr:
        if curr in visited:
            return True

        visited.add(curr)
        curr = curr.next

    return False