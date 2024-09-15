# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes to reverse
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we don't have k nodes, return head as it is
        if count < k:
            return head
        
        # Step 2: Reverse the first k nodes
        prev = None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: Recursively reverse the next k nodes and connect them
        head.next = self.reverseKGroup(curr, k)
        
        # prev is the new head of the reversed list
        return prev
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
