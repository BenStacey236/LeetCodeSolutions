# Medium Problem
# Problem 146

from typing import Optional

class ListNode:

    def __init__(self, key: int, value: int):
        self.key: int = key
        self.value: int = value
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None

class LinkedList:

    def __init__(self):
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self.length = 0

    def __str__(self) -> str:
        curr = self.head
        pairs = []
        while curr:
            pairs.append(f"{curr.key}:{curr.value}")
            curr = curr.next
        
        return f"[{", ".join(pairs)}]"

    def prepend(self, node: ListNode) -> None:
        self.length += 1

        if not self.head:
            self.head = node
            self.tail = node
            return

        self.head.prev = node
        node.next = self.head
        self.head = node

    def pop(self, node: ListNode) -> None:
        self.length -= 1

        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
            return

        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return

        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, ListNode] = {}
        self.capacity: int = capacity
        self.recency: LinkedList = LinkedList()
        

    def get(self, key: int) -> int:
        node: ListNode = self.cache.get(key, None)

        if not node:
            return -1

        self.recency.pop(node)
        self.recency.prepend(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.recency.pop(node)
            node.value = value
            self.recency.prepend(node)
            return

        if self.recency.length == self.capacity:
            self.cache.pop(self.recency.tail.key)
            self.recency.pop(self.recency.tail)

            new = ListNode(key, value)
            self.recency.prepend(new)
            self.cache[key] = new
            return

        new = ListNode(key, value)
        self.cache[key] = new
        self.recency.prepend(new)