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
        oldtonew = {}

        def dfs(curr):
            if not curr:
                return None
            if curr in oldtonew:
                return oldtonew[curr]

            copy = Node(curr.val)
            oldtonew[curr] = copy

            for neiN in curr.neighbors:
                copy.neighbors.append(dfs(neiN))

            return copy

        dfs(node)
        return oldtonew[node]