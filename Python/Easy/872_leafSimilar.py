# Easy Problem
# Problem 872

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

    leftLeaves: list = []
    rightLeaves: list = []

    def dfs(node: TreeNode, leafList: list) -> None:

        if not node.left and not node.right:
            leafList.append(node.val)
            return

        if node.left:
            dfs(node.left, leafList)

        if node.right:
            dfs(node.right, leafList)
    
    dfs(root1, leftLeaves)
    dfs(root2, rightLeaves)

    return leftLeaves == rightLeaves


if __name__ == "__main__":
    tree1 = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    tree2 = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

    print(leafSimilar(tree1, tree2))

    