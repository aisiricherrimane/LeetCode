# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sametree(root, subRoot):
            return True
        return self.sametree(root.left, subRoot) or self.sametree(root.right, subRoot)

    def sametree(self, p, q):
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.sametree(p.right, q.right) and self.sametree(p.left, q.left)
        
        else:
            return False
        

        