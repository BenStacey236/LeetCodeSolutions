# Easy Problem
# Problem 206

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    if not head:
        return None
    currentNode = head
    prev = None
    
    while currentNode and currentNode.next:
        next = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = next

    currentNode.next = prev

    return currentNode
    

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))

if __name__ == "__main__":
    newHead = reverseList(head)

    while newHead.next:
        print(newHead.val)
        newHead = newHead.next

    print(newHead.val)