"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_to_deep = {}

        if not head:
            return None
        curr = head
        while curr:
            node_to_deep[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = node_to_deep[curr]
            copy.next = node_to_deep.get(curr.next, None)
            copy.random = node_to_deep.get(curr.random, None)
            curr = curr.next
        return node_to_deep[head]
