# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return same(p.left, q.right) and same(p.right, q.left)
            else:
                return False
        
        if not root:
            return True
        p = root.left
        q = root.right
        return same(p, q)
            

        