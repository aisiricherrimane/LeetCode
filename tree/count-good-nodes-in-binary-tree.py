# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(node, greater):
            if not node:
                return

            if node.val >= greater:
                self.good += 1

            dfs(node.right, max(node.val,greater))
            dfs(node.left, max(node.val, greater))
        
        dfs(root, float('-inf'))
        return self.good
        