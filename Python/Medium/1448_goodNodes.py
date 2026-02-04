# Medium Problem
# Problem 1448

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    
    goodNodes = 1

    toVisit: list[tuple[TreeNode, int]] = []

    def dfs(entry: tuple[TreeNode, int]) -> None:
        node, maxOnPath = entry

        if node.left:
            toVisit.append((node.left, max(maxOnPath, node.val)))

        if node.right:
            toVisit.append((node.right, max(maxOnPath, node.val)))
    
    dfs((root, root.val))

    while toVisit:
        toExplore = toVisit.pop()
        dfs(toExplore)
        node, maxOnPath = toExplore
        if maxOnPath <= node.val:
            goodNodes += 1

    return goodNodes