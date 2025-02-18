# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def helper(node):
            if not node:
                return 0

            leftmax = helper(node.left)
            rightmax = helper(node.right)

            self.res = max(self.res, leftmax + rightmax)

            return 1 + max(leftmax, rightmax)
        helper(root)
        return self.res