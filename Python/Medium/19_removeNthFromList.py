# Medium Problem
# Problem 19

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:

    if not head.next:
        return None

    origin = head

    length = 1
    while head.next:
        length += 1
        head = head.next

    head = origin
    n = length - n

    if n == 0:
        return head.next

    counter = 0
    prev = head
    while counter < n:
        if counter == n-1:
            prev = head

        head = head.next
        counter += 1

    prev.next = head.next

    return origin