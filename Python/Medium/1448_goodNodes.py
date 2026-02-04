# Medium Problem
# Problem 1448

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    
    goodNodes = 1

    toVisit: list[tuple[TreeNode, list[int]]] = []

    def dfs(entry: tuple[TreeNode, list[int]]) -> None:
        node, path = entry

        if node.left:
            toVisit.append((node.left, path + [node.val]))

        if node.right:
            toVisit.append((node.right, path + [node.val]))
    
    dfs((root, []))

    while toVisit:
        node, path = toVisit.pop()
        dfs((node, path))
        if max(path) <= node.val:
            goodNodes += 1

    return goodNodes