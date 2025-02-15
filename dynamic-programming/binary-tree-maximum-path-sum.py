# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def calculate(node):
            if not node:
                return 0

            leftMax = max(0, calculate(node.left))
           
            rightMax = max(0, calculate(node.right))

            self.res = max(self.res, node.val + leftMax + rightMax)

            return (node.val + max(leftMax, rightMax))
        calculate(root)
        return self.res