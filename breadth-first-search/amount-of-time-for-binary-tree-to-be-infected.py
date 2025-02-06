# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        stack = [(root, None)]
        while stack:
            n, p = stack.pop()
            if p:
                graph[p.val].append(n.val)
                graph[n.val].append(p.val)
            if n.left:
                stack.append((n.left, n))
            if n.right:
                stack.append((n.right, n))
            
        ans = -1
        seen = set()
        seen.add(start)
        q = deque([start])

        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            ans += 1
        return ans
