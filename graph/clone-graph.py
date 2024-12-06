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
        clone = defaultdict(list)

        def dfs(root):
            if root in clone:
                return clone[root]
            temp = Node(root.val)
            clone[root] = temp
            for neiN in root.neighbors:
                clone[root].neighbors.append(dfs(neiN))
            return temp
        
        return dfs(node)

