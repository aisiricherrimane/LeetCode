"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        adj = {}
        def dfs(root):
            if root in adj:
                return adj[root]

            temp = Node(root.val)
            adj[root] = temp

            for neiN in root.neighbors:
                adj[root].neighbors.append(dfs(neiN))
            return temp
    
        return dfs(node)
      

