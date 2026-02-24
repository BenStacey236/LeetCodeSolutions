# Medium Problem
# Problem 98

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:

    toVisit: List[tuple[TreeNode, tuple[int, int]]] = [(root, (-float('inf'), float('inf')))]

    def explore(node: TreeNode, bounds: tuple[int, int]) -> None:
        
        if node.left:
            toVisit.append((node.left, (bounds[0], node.val)))

        if node.right:
            toVisit.append((node.right, (node.val, bounds[1])))

    while toVisit:

        node, (lower, upper) = toVisit.pop()

        if not (lower < node.val < upper):
            return False

        explore(node, (lower, upper))

    return True