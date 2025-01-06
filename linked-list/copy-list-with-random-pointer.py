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
        if not head:
            return None
        oldtonew = {}
        curr = head

        while curr:
            temp = Node(curr.val)
            oldtonew[curr] = temp
            curr = curr.next

        curr = head
        while curr:
            copy = oldtonew[curr]
            copy.next = oldtonew.get(curr.next)
            copy.random = oldtonew.get(curr.random)
            curr = curr.next
        
        return oldtonew[head]

        