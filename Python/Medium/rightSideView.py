# Medium Problem
# Problem 199

from typing import Optional, List

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    to_visit: list[tuple[TreeNode, int]] = [(root, 0)]
    visited_levels: set[int] = set()
    res: list[int] = []

    def dfs(node: tuple[TreeNode, int]) -> None:
        treeNode, level = node

        if treeNode.right:
            to_visit.append((treeNode.right, level + 1))
            dfs((treeNode.right, level + 1))

        if treeNode.left:
            to_visit.append((treeNode.left, level + 1))
            dfs((treeNode.left, level + 1))

    dfs(to_visit[0])

    while to_visit:
        curr, level = to_visit.pop(0)

        if level not in visited_levels:
            res.append(curr.val)

        visited_levels.add(level)

    return res


if __name__ == "__main__":
    
    tree1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    tree2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))

    print(rightSideView(tree1))
    print(rightSideView(tree2))