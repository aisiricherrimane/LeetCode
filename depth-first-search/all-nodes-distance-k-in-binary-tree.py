# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def parent(node, par):
            if node:
                node.parent = par
                parent(node.left, node)
                parent(node.right, node)
        parent(root, None)

        answer = []
        visited = set()
        def closest(node, dist):
            if not node or node in visited:
                return 
            visited.add(node)
            if dist == k:
                answer.append(node.val)
                return
            closest(node.parent, dist + 1)
            closest(node.right, dist + 1)
            closest(node.left, dist + 1)
        closest(target, 0)

        return answer
            
            
        
        