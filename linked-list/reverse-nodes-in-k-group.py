# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while count < k and curr:
            curr = curr.next
            count += 1
        if count == k:
            reversed_head = self.reverse(head, k)
            head.next = self.reverseKGroup(curr, k)
            return reversed_head
        else:
            return head

    def reverse(self,node, k):
        temp_head = None
        while k > 0:
            temp = node.next
            node.next = temp_head
            temp_head = node
            node = temp
            k -= 1
        return temp_head
