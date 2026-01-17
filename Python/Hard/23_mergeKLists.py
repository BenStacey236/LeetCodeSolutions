# Hard Problem
# Problem 23

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
    def findMin(lists: List[Optional[ListNode]]) -> tuple[int, int]:
        vals = []

        for i, list in enumerate(lists):
            if list:
                vals.append((list.val, i))

        if not vals:
            return None

        return min(vals, key = lambda x : x[0])

    res = None
    curr = None

    while True:
        minimum = findMin(lists)

        if not minimum:
            break

        val, iList = minimum
        if not res:
            res = ListNode(val)
            curr = res

        else:
            curr.next = ListNode(val)
            curr = curr.next

        node = lists[iList]
        lists[iList] = node.next

    return res


if __name__ == "__main__":

    print(mergeKLists([[]]))

    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]

    node = mergeKLists(lists)

    while node:
        print(node.val)
        node = node.next