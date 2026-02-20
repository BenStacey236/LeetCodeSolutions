# Medium Problem
# Problem 129

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumNumbers(root: Optional[TreeNode]) -> int:
    
    toVisit: List[tuple[TreeNode, int]] = [(root, 0)]

    def dfs(entry: tuple[TreeNode, int]) -> None:
        
        node, depth = entry

        if node.right:
            toVisit.append((node.right, depth + 1))

        if node.left:
            toVisit.append((node.left, depth + 1))

    total = 0
    prevDepth = -1
    path = []

    while toVisit:

        node, depth = toVisit.pop()

        if depth <= prevDepth:
            for i in range(prevDepth-depth+1):
                path.pop()

        prevDepth = depth

        dfs((node, depth))

        path.append(str(node.val))

        if not node.left and not node.right:
            total += int(''.join(path))

    return total