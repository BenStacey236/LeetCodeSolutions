# Easy Problem
# Problem 141

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
        
    slow, fast = head, head

    if not head:
        return False

    started = False
    while slow and fast:

        if started and slow == fast:
            return True

        if not started:
            started = True
        
        fast = fast.next
        if not fast:
            return False
        fast = fast.next
        slow = slow.next

    return False