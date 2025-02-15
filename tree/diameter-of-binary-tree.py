# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        def dfs(node):
            if not node:
                return 0
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)

            self.length = max(self.length, leftmax + rightmax)

            return 1 + max(leftmax, rightmax)
        dfs(root)
        return self.length
            
