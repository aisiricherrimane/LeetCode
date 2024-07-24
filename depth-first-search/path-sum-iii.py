# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        def helper(root, check, isNew):
            if not root:
                return 
            if check - root.val == 0:
                self.paths += 1
            helper(root.left, check - root.val, False)
            helper(root.right, check - root.val, False)

            if isNew:
                helper(root.left, targetSum , True)
                helper(root.right, targetSum , True)
        helper(root, targetSum, True)
        return self.paths

            
        