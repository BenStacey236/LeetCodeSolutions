# Easy problem
# Problem 21

import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    
    currentL = list1
    currentR = list2

    if list1.val <= list2.val:
        newHead = list1
        currentL = newHead.next
        currentR = list2
    else:
        newHead = list2
        currentL = list1
        currentR = newHead.next

    additionNode = newHead

    while currentL or currentR:
        leftVal = math.inf if not currentL else currentL.val
        rightVal = math.inf if not currentR else currentR.val

        if leftVal <= rightVal:
            additionNode.next = currentL
            currentL = currentL.next
        else:
            additionNode.next = currentR
            currentR = currentR.next

        additionNode = additionNode.next

    return newHead

list1 = ListNode(val=5, next=None)
list2 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))

if __name__ == "__main__":
    merged = mergeTwoLists(list1, list2)
    
    print("[", end="")
    while merged.next:
        print(f"{merged.val}, ", end="")
        merged = merged.next
    print(f"{merged.val}]")
