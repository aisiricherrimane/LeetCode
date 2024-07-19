# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return (True, 0)
            left_b, left_h = helper(node.left)
            right_b, right_h = helper(node.right)
            curr_b = left_b and right_b and abs(left_h - right_h) <= 1
            curr_h = 1 + max(left_h, right_h)
            return (curr_b, curr_h)  # Added return statement

        return helper(root)[0]