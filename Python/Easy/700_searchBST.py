# Easy Problem
# Problem 700

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    curr = root

    while True:

        if not curr:
            return None

        if curr.val == val:
            return curr

        if curr.val < val:
            curr = curr.right
            continue

        if curr.val > val:
            curr = curr.left
            continue
