# Easy Problem
# Problem 104

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:

    def dfs(node: TreeNode, depth: int = 1) -> int:

        if not node.left and not node.right:
            return depth

        if not node.left:
            return dfs(node.right, depth + 1)

        if not node.right:
            return dfs(node.left, depth + 1)

        return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
    
    return dfs(root)


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

    print(maxDepth(tree))