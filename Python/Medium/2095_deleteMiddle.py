# Medium Problem
# Problem 2095

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head
    prevSlow = None

    while fast and fast.next:
        fast = fast.next
        if not fast:
            break
        fast = fast.next
        prevSlow = slow
        slow = slow.next

    if not prevSlow:
        return None
    prevSlow.next = slow.next

    return head