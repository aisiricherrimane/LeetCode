# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def good(node, maxval):
            if not node:
                return 
            if node.val >= maxval:
                self.good += 1
                maxval = max(maxval, node.val)
            good(node.left, maxval)
            good(node.right, maxval)
        good(root, root.val)
        return self.good