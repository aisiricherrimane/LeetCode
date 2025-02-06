# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def parent_add(cur, parent):
            if cur:
                cur.parent = parent
                parent_add(cur.right, cur)
                parent_add(cur.left, cur)

        parent_add(root, None)

        answer = []
        visited = set()

        def dfs(cur, dist):
            if not cur or cur in visited:
                return
            visited.add(cur)
            if dist == 0:
                answer.append(cur.val)
                return 
            dfs(cur.parent, dist - 1)
            dfs(cur.right, dist - 1)
            dfs(cur.left, dist - 1)
        
        dfs(target, k)
        return answer 
        