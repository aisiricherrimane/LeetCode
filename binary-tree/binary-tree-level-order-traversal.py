# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left) if node.left else None
                    q.append(node.right) if node.left else None
                l   evel.append(node.val)
            res.append(level)
        return res

        