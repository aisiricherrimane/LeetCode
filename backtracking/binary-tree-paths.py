# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, currpath):
            if not root:
                return 
            currpath.append(str(root.val))
            if not root.right and not root.left:
                paths.append('->'.join(currpath))
            helper(root.right, currpath)
            helper(root.left, currpath)
            currpath.pop()

        paths = []
        helper(root, [])
        return paths
        