# Easy Problem
# Problem 100

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    def equalNode(node1: TreeNode, node2: TreeNode) -> bool:

        if not node1 and not node2:
            return True

        if (node1 != None) ^ (node2 != None):
            return False

        if (node1.left != None) ^ (node2.left != None):
            return False

        if (node1.right != None) ^ (node2.right != None):
            return False

        if node1.val != node2.val:
            return False

        return equalNode(node1.left, node2.left) and equalNode(node1.right, node2.right)

    return equalNode(p, q)