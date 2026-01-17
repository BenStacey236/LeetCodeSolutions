# Medium Problem
# Problem 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    num1 = l1.val
    num2 = l2.val

    current = l1
    count = 1
    while current.next:
        current = current.next
        num1 += current.val * 10**count
        count += 1

    current = l2
    count = 1
    while current.next:
        current = current.next
        num1 += current.val * 10**count
        count += 1

    total = str(num1 + num2)
    head = ListNode()
    current = head
    for i, digit in enumerate(reversed(total)):
        current.val = int(digit)
        
        if i != len(total)-1:
            current.next = ListNode()
            current = current.next

    return head