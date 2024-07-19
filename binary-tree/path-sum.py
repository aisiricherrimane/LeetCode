# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, total):
            if not root:
                return False
            total += root.val
            if not root.right and not root.left:
                if total == targetSum:
                    return True
            return dfs(root.right, total) or dfs(root.left, total)


        if not root:
            return False
        return dfs(root, 0)

        