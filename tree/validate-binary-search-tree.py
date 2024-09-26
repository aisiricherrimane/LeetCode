# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(left, right, node):
            if not node:
                return True
            if node.val > left and node.val < right:
                return check(node.val, right ,node.right) and check(left, node.val, node.left)
            else:
                return False
        return check(float('-inf'), float('inf'), root)
        