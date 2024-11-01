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
        temp = {}

        def dfs(root):
            if root in temp:
                return temp[root]
            copy = Node(root.val)
            temp[root] = copy
            for nei in root.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        dfs(node)
        return temp[node]
