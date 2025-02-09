# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        count = 0
        curr = head

        while count < k and curr:
            curr = curr.next
            count += 1

        if count == k:
            reversed_head = self.reverse(head, k)
            head.next = self.reverseKGroup(curr, k)
            return reversed_head
        else:
            return head
    
    def reverse(self, node, k):
        new_head = None
        curr = node

        while k:
            temp = curr.next
            curr.next = new_head
            new_head = curr
            curr = temp
            k -= 1
        return new_head