# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {}
        res = []
        traversed = set()

        def parent_map(node, parent):
            if not node:
                return 
            parentMap[node] = parent
            parent_map(node.left, node)
            parent_map(node.right, node)
        def getnode(node, away):
            if not node or node in traversed or away > k:
                return 
            traversed.add(node)
            if away == k:
                res.append(node.val)
                return 
            getnode(parentMap[node], away + 1)
            getnode(node.right, away + 1)
            getnode(node.left, away + 1)
        
        parent_map(root, None)
        getnode(target, 0)
        return res

        