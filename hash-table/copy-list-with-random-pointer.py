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

        temp = {}
        curr = head
        while curr:
            temp[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = temp[curr]
            copy.next = temp.get(curr.next)
            copy.random = temp.get(curr.random)
            curr = curr.next
        return temp[head]
        