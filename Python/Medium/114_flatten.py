# Medium Problem
# Problem 114

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    if not root:
        return None

    toVisit: List[TreeNode] = []

    def dfs(node: TreeNode) -> None:
        toVisit.append(node)

        if node.left:
            dfs(node.left)

        if node.right:
            dfs(node.right)

    dfs(root)

    prev = root
    node = toVisit.pop(0)
    prev.left = None
    prev.right = None
    while toVisit:
        node = toVisit.pop(0)

        new = TreeNode(node.val)
        prev.right = new
        prev = new