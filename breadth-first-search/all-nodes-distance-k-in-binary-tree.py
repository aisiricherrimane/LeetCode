# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def set_parent(node, p):
            if node:
                node.parent = p
                set_parent(node.left, node)
                set_parent(node.right, node)
        set_parent(root, None)

        res = []
        visited = set()

        def dfs(node, k):
            if not node or node in visited:
                return
            if k == 0:
                res.append(node.val)
                return
            
            visited.add(node)
            dfs(node.parent, k - 1)
            dfs(node.left, k - 1)
            dfs(node.right, k - 1)
        
        dfs(target, k)

        return res

        