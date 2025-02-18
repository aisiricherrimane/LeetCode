# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def set_parent(node, parent):
            if not node:
                return 
            node.parent = parent
            set_parent(node.left, node)
            set_parent(node.right, node)
        set_parent(root, None)
        
        p1 = p
        p2 = q

        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p
        return p1

        